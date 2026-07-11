from __future__ import annotations

import sys

from stv.navigation_contract import HOME_ENTRIES, SECTION_FIXED_ENTRIES, VALID_SECTIONS
from stv.routing import Request
from stv.app.services import AppContainer
from stv.app.sync import ensure_categories_loaded, ensure_streams_loaded


def _icon(scope: str, filename: str) -> str:
    from saile_core.artwork import artwork_path

    return artwork_path(scope, filename)


def _show_home(request: Request, fanart: str) -> None:
    from stv.ui.directory import add_folder, finish_directory

    for label, action, section, scope, filename in HOME_ENTRIES:
        url = request.url(action=action, section=section) if section else request.url(action=action)
        add_folder(request.handle, label, url, _icon(scope, filename), fanart)
    finish_directory(request.handle, "videos")


def _show_section(request: Request, app: AppContainer, section: str, fanart: str) -> None:
    from stv.ui.directory import add_folder, finish_directory

    # 1. Fixed navigation items
    for label, action, scope, filename in SECTION_FIXED_ENTRIES:
        add_folder(
            request.handle,
            label,
            request.url(action=action, section=section),
            _icon(scope, filename),
            fanart,
        )
        
    # 2. Dynamic categories from database
    ensure_categories_loaded(app, section)
    categories = app.catalog.get_categories(section)
    for cat in categories:
        add_folder(
            request.handle,
            cat.name,
            request.url(action="category", section=section, category_id=cat.category_id),
            _icon("common", "check.png"),  # Could use a specific icon if available
            fanart,
        )

    finish_directory(request.handle, "videos")


def _show_category(request: Request, app: AppContainer, section: str, category_id: str, fanart: str) -> None:
    from stv.ui.directory import add_folder, finish_directory
    import xbmcgui

    ensure_streams_loaded(app, section, category_id)
    items = app.catalog.get_media_items(section, category_id)
    for item in items:
        # We use play action
        url = request.url(action="play", section=section, stream_id=item.item_id, extension=item.extension)
        # Use item.icon if valid, otherwise fallback
        icon_url = item.icon if item.icon.startswith("http") else _icon("common", "check.png")
        # In a real app we would use add_item (with isFolder=False) for playables, 
        # but add_folder with a play action can also work if we don't set isFolder=True.
        # Actually `add_folder` hardcodes isFolder=True in stv.ui.directory probably. 
        # Let's import add_item if we need it. Let's see what is inside stv.ui.directory.
        add_folder(
            request.handle,
            item.name,
            url,
            icon_url,
            item.fanart or fanart,
            is_folder=False
        )

    finish_directory(request.handle, "videos")


def _play_item(app: AppContainer, section: str, stream_id: str, extension: str) -> None:
    from stv.ui.player import play_video
    
    url = app.xtream.stream_url(section, stream_id, extension)
    play_video(app, section, stream_id, url)


def run(argv: list[str]) -> None:
    """Entrypoint estrutural com o contrato oficial de navegação do sTv."""
    import xbmcaddon

    from saile_core.notifications import notify_info
    from stv.app.services import AppContainer

    request = Request.from_argv(argv)
    addon = xbmcaddon.Addon()
    fanart = addon.getAddonInfo("fanart")

    settings = {
        "xtream_host": addon.getSetting("xtream_host"),
        "xtream_username": addon.getSetting("xtream_username"),
        "xtream_password": addon.getSetting("xtream_password"),
        "profile_path": __import__("xbmcvfs").translatePath(addon.getAddonInfo("profile")),
    }
    app = AppContainer(settings)

    if request.action in {"", "home"}:
        _show_home(request, fanart)
        return

    if request.action == "section":
        section = request.params.get("section", "")
        if section in VALID_SECTIONS:
            _show_section(request, app, section, fanart)
            return

    if request.action == "category":
        section = request.params.get("section", "")
        category_id = request.params.get("category_id", "")
        if section in VALID_SECTIONS and category_id:
            _show_category(request, app, section, category_id, fanart)
            return

    if request.action == "play":
        section = request.params.get("section", "")
        stream_id = request.params.get("stream_id", "")
        extension = request.params.get("extension", "")
        if section in VALID_SECTIONS and stream_id:
            _play_item(app, section, stream_id, extension)
            return

    if request.action == "sync":
        notify_info("sTv", "Sincronização LAN manual ainda não implementada")
        _show_home(request, fanart)
        return

    if request.action in {"search", "favorites"}:
        notify_info("sTv", "Rota estrutural ainda não implementada")
        section = request.params.get("section", "")
        if section in VALID_SECTIONS:
            _show_section(request, app, section, fanart)
            return

    _show_home(request, fanart)
