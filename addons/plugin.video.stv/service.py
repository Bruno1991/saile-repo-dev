import os
import sys
import hashlib
import xbmc
import xbmcaddon
from pathlib import Path
import xbmcvfs

LIB_DIR = os.path.join(os.path.dirname(__file__), "resources", "lib")
if LIB_DIR not in sys.path:
    sys.path.insert(0, LIB_DIR)

from stv.infrastructure.lan_sync import LanSyncServer
from stv.persistence.database import Database

def get_db(addon) -> Database:
    db_path = Path(xbmcvfs.translatePath(addon.getAddonInfo("profile"))) / "stv.db"
    return Database(db_path)

def get_host_hash(addon) -> str:
    host = addon.getSetting("xtream_host").strip().lower()
    username = addon.getSetting("xtream_username").strip()
    return hashlib.sha256(f"{host}:{username}".encode('utf-8')).hexdigest()

if __name__ == "__main__":
    addon = xbmcaddon.Addon()
    db = get_db(addon)
    host_hash = get_host_hash(addon)
    
    server = LanSyncServer(host_hash, db)
    server.start()
    
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            break
            
    server.stop()
