import socket
import threading
import json
import time
import struct
import logging
from typing import Optional

from stv.persistence.database import Database

UDP_PORT = 42100
TCP_PORT = 42101

class LanSyncServer:
    def __init__(self, host_hash: str, db: Database):
        self.host_hash = host_hash
        self.db = db
        self.running = False
        self._udp_thread: Optional[threading.Thread] = None
        self._tcp_thread: Optional[threading.Thread] = None

    def start(self) -> None:
        self.running = True
        self._udp_thread = threading.Thread(target=self._run_udp_server, daemon=True)
        self._tcp_thread = threading.Thread(target=self._run_tcp_server, daemon=True)
        self._udp_thread.start()
        self._tcp_thread.start()

    def stop(self) -> None:
        self.running = False

    def _run_udp_server(self) -> None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("", UDP_PORT))
        sock.settimeout(1.0)
        while self.running:
            try:
                data, addr = sock.recvfrom(1024)
                msg = data.decode('utf-8')
                if msg == f"sTv-sync-discover:{self.host_hash}":
                    sock.sendto(f"sTv-sync-response:{TCP_PORT}".encode('utf-8'), addr)
            except socket.timeout:
                continue
            except Exception:
                pass
        sock.close()

    def _run_tcp_server(self) -> None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("", TCP_PORT))
        sock.listen(5)
        sock.settimeout(1.0)
        while self.running:
            try:
                conn, addr = sock.accept()
                self._handle_tcp_client(conn)
            except socket.timeout:
                continue
            except Exception:
                pass
        sock.close()

    def _handle_tcp_client(self, conn: socket.socket) -> None:
        try:
            data = self.db.export_user_data()
            payload = json.dumps(data).encode('utf-8')
            conn.sendall(struct.pack('!I', len(payload)))
            conn.sendall(payload)
        finally:
            conn.close()

def discover_and_sync(host_hash: str, db: Database, timeout: float = 2.0) -> int:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(timeout)
    
    msg = f"sTv-sync-discover:{host_hash}".encode('utf-8')
    sock.sendto(msg, ('<broadcast>', UDP_PORT))
    
    peers = set()
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            data, addr = sock.recvfrom(1024)
            resp = data.decode('utf-8')
            if resp.startswith("sTv-sync-response:"):
                port = int(resp.split(":")[1])
                peers.add((addr[0], port))
        except socket.timeout:
            break
        except Exception:
            pass
            
    sock.close()
    
    synced_count = 0
    # Determine our own local IP to avoid syncing with ourselves
    local_ip = socket.gethostbyname(socket.gethostname())
    
    for ip, port in peers:
        if ip in ("127.0.0.1", "localhost", local_ip):
            continue
            
        try:
            tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_sock.settimeout(3.0)
            tcp_sock.connect((ip, port))
            
            length_data = tcp_sock.recv(4)
            if len(length_data) == 4:
                length = struct.unpack('!I', length_data)[0]
                payload_data = bytearray()
                while len(payload_data) < length:
                    chunk = tcp_sock.recv(min(4096, length - len(payload_data)))
                    if not chunk:
                        break
                    payload_data.extend(chunk)
                
                remote_data = json.loads(payload_data.decode('utf-8'))
                db.merge_user_data(remote_data)
                synced_count += 1
            tcp_sock.close()
        except Exception as e:
            logging.error(f"Failed to sync with {ip}:{port}: {e}")
            
    return synced_count
