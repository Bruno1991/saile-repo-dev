import xbmc
import xbmcgui
import xbmcaddon
import os
import socket
import threading
import json
import hashlib
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import shutil
from lib import storage

UDP_PORT = 19991
HTTP_PORT = 19992
DISCOVERY_MAGIC = "SAILE_SYNC_DISCOVER"

def get_auth_token():
    addon = xbmcaddon.Addon()
    pwd = addon.getSetting("xtream_password") or "saile_default_pass"
    return hashlib.md5(pwd.encode('utf-8')).hexdigest()

class SyncHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        token = self.headers.get("Authorization")
        if token != get_auth_token():
            self.send_response(401)
            self.end_headers()
            return
            
        if self.path == "/download":
            db_path = storage.DB_PATH
            if not os.path.exists(db_path):
                self.send_response(404)
                self.end_headers()
                return
            
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.send_header('Content-Disposition', 'attachment; filename="saile.db"')
            self.end_headers()
            with open(db_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

def run_http_server():
    server_address = ('', HTTP_PORT)
    httpd = HTTPServer(server_address, SyncHTTPHandler)
    httpd.timeout = 1
    # Run for 2 minutes max
    end_time = time.time() + 120
    while time.time() < end_time and not xbmc.abortRequested:
        httpd.handle_request()
    httpd.server_close()

def run_udp_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', UDP_PORT))
    sock.settimeout(1)
    
    end_time = time.time() + 120
    my_token = get_auth_token()
    my_name = xbmc.getInfoLabel("System.FriendlyName") or "SaileTV"
    
    while time.time() < end_time and not xbmc.abortRequested:
        try:
            data, addr = sock.recvfrom(1024)
            msg = data.decode('utf-8')
            if msg.startswith(DISCOVERY_MAGIC):
                parts = msg.split('|')
                if len(parts) > 1 and parts[1] == my_token:
                    # Token matches, respond
                    resp = f"SAILE_SYNC_REPLY|{my_name}"
                    sock.sendto(resp.encode('utf-8'), addr)
        except socket.timeout:
            pass
        except Exception:
            pass
    sock.close()

def server_sync():
    """Inicia o servidor de sincronização por 2 minutos."""
    dialog = xbmcgui.DialogProgress()
    dialog.create("Saile Sync", "Modo Servidor Ativo (2 min)...\nAguardando clientes na rede local.")
    
    t_http = threading.Thread(target=run_http_server)
    t_udp = threading.Thread(target=run_udp_listener)
    
    t_http.start()
    t_udp.start()
    
    end_time = time.time() + 120
    while time.time() < end_time and not xbmc.abortRequested:
        if dialog.iscanceled():
            break
        rem = int(end_time - time.time())
        dialog.update(int((120 - rem) / 120.0 * 100), "Modo Servidor Ativo", f"Tempo restante: {rem} segundos...")
        xbmc.sleep(1000)
        
    dialog.close()

def discover_devices():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(2)
    
    my_token = get_auth_token()
    msg = f"{DISCOVERY_MAGIC}|{my_token}"
    sock.sendto(msg.encode('utf-8'), ('<broadcast>', UDP_PORT))
    
    devices = []
    start = time.time()
    while time.time() - start < 3:
        try:
            data, addr = sock.recvfrom(1024)
            text = data.decode('utf-8')
            if text.startswith("SAILE_SYNC_REPLY"):
                name = text.split('|')[1] if '|' in text else "Saile"
                devices.append({"ip": addr[0], "name": name})
        except socket.timeout:
            break
        except Exception:
            pass
    sock.close()
    return devices

def client_sync(ip=None):
    """Cliente descobre ou usa IP para baixar o banco."""
    token = get_auth_token()
    
    if not ip:
        devices = discover_devices()
        if not devices:
            xbmcgui.Dialog().ok("Saile Sync", "Nenhum servidor encontrado na rede local.\nVerifique se o modo Servidor está ativo no outro dispositivo.")
            return
        
        if len(devices) == 1:
            ip = devices[0]["ip"]
        else:
            opts = [f"{d['name']} ({d['ip']})" for d in devices]
            idx = xbmcgui.Dialog().select("Selecione o Servidor", opts)
            if idx < 0: return
            ip = devices[idx]["ip"]
            
    url = f"http://{ip}:{HTTP_PORT}/download"
    req = urllib.request.Request(url)
    req.add_header('Authorization', token)
    
    dialog = xbmcgui.DialogProgress()
    dialog.create("Saile Sync", "Baixando banco de dados...")
    
    try:
        response = urllib.request.urlopen(req, timeout=5)
        temp_path = storage.DB_PATH + ".tmp"
        with open(temp_path, 'wb') as f:
            shutil.copyfileobj(response, f)
            
        # Substitui o banco
        storage.close_connections()
        shutil.move(temp_path, storage.DB_PATH)
        
        dialog.close()
        xbmcgui.Dialog().ok("Saile Sync", "Sincronização concluída com sucesso!\nO Kodi será reiniciado/atualizado.")
        xbmc.executebuiltin("Container.Refresh")
    except Exception as e:
        dialog.close()
        xbmcgui.Dialog().ok("Erro no Sync", f"Falha ao conectar ou baixar:\n{str(e)}")
