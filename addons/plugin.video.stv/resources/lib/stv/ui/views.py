from __future__ import annotations

from pathlib import Path

import xbmcaddon
import xbmcgui
import xbmcvfs

from stv.app.services import SyncService
from stv.persistence.database import Database
from stv.providers.xtream.client import XtreamClient
from stv.routing import Request
from stv.ui.directory import add_folder, add_video_item, finish_directory, play_video


def get_db() -> Database:
    addon = xbmcaddon.Addon()
    db_path = Path(xbmcvfs.translatePath(addon.getAddonInfo("profile"))) / "stv.db"
    return Database(db_path)


def get_client() -> XtreamClient:
    addon = xbmcaddon.Addon()
    host = addon.getSetting("xtream_host")
    username = addon.getSetting("xtream_username")
    password = addon.getSetting("xtream_password")
    return XtreamClient(host, username, password)


def render_categories(request: Request, media_type: str) -> None:
    addon = xbmcaddon.Addon()
    media = addon.getAddonInfo("path") + "/resources/media/"
    fanart = addon.getAddonInfo("fanart")

    add_folder(request.handle, "[ Pesquisa ]", request.url(action=f"search_{media_type}"), icon=media + "search.png", fanart=fanart)
    add_folder(request.handle, "[ Favoritos ]", request.url(action=f"favorites_{media_type}"), icon=media + "favorites.png", fanart=fanart)

    db = get_db()
    categories = db.get_categories(media_type)
    for cat in categories:
        add_folder(request.handle, cat.name, request.url(action=f"list_{media_type}", category_id=cat.category_id), fanart=fanart)
    finish_directory(request.handle, "videos")


def render_items(request: Request, media_type: str, category_id: str) -> None:
    db = get_db()
    items = db.get_media_items(media_type, category_id)
    for item in items:
        add_video_item(
            request.handle,
            item.name,
            request.url(action="play", media_type=media_type, item_id=item.item_id, extension=item.extension, name=item.name, icon=item.icon),
            icon=item.icon,
            fanart=item.fanart,
            plot=item.plot,
            is_playable=True
        )
    finish_directory(request.handle, "videos")


def action_play(request: Request) -> None:
    media_type = request.params.get("media_type", "live")
    item_id = request.params.get("item_id", "")
    extension = request.params.get("extension", "")
    name = request.params.get("name", "")
    icon = request.params.get("icon", "")

    client = get_client()
    url = client.stream_url(media_type, item_id, extension)
    play_video(request.handle, url, name, icon)


def action_sync() -> None:
    xbmcgui.Dialog().notification("sTv", "Iniciando sincronização...")
    try:
        client = get_client()
        db = get_db()
        db.initialize()
        service = SyncService(client, db)
        service.sync_live()
        service.sync_vod()
        xbmcgui.Dialog().notification("sTv", "Sincronização concluída!")
    except Exception as e:
        xbmcgui.Dialog().notification("sTv", f"Erro: {e}")


def action_sync_lan() -> None:
    import hashlib
    from stv.infrastructure.lan_sync import discover_and_sync

    addon = xbmcaddon.Addon()
    host = addon.getSetting("xtream_host").strip().lower()
    username = addon.getSetting("xtream_username").strip()
    host_hash = hashlib.sha256(f"{host}:{username}".encode("utf-8")).hexdigest()
    
    dialog = xbmcgui.DialogProgress()
    dialog.create("sTv", "Buscando dispositivos na rede local...")
    
    try:
        db = get_db()
        synced_count = discover_and_sync(host_hash, db, timeout=3.0)
        dialog.close()
        xbmcgui.Dialog().notification("sTv", f"Sincronizado com {synced_count} dispositivo(s)!")
    except Exception as e:
        dialog.close()
        xbmcgui.Dialog().notification("sTv", f"Erro no sync LAN: {e}")
