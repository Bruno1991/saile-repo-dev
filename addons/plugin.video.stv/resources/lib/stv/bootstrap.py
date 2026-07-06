from __future__ import annotations

from stv.routing import Request


def run(argv: list[str]) -> None:
    """Kodi entrypoint. Kodi-only imports stay inside the runtime boundary."""
    import xbmcaddon
    import xbmcgui
    import xbmcplugin

    from stv.ui.directory import add_folder, finish_directory

    request = Request.from_argv(argv)
    addon = xbmcaddon.Addon()
    media = addon.getAddonInfo("path") + "/resources/media/"

    # This bootstrap is intentionally small: it proves installation, routing and artwork.
    # Feature implementation belongs in app/providers/persistence modules.
    if request.action == "open_settings":
        addon.openSettings()
        return

    from stv.ui.views import render_categories, render_items, action_play, action_sync, get_db

    if request.action in ("home", ""):
        get_db().initialize()
        entries = (
            ("TV ao vivo", "live", "live_tv.png"),
            ("Filmes (VOD)", "vod", "vod.png"),
            ("Séries", "series", "series.png"),
            ("Busca", "search", "search.png"),
            ("Favoritos", "favorites", "favorites.png"),
            ("Continuar assistindo", "continue", "continue_watching.png"),
            ("Sincronizar catálogo Xtream", "sync", "sync.png"),
            ("Sincronizar aparelhos (LAN)", "sync_lan", "sync.png"),
            ("Configurações", "open_settings", "settings.png"),
        )
        for label, action, icon in entries:
            add_folder(request.handle, label, request.url(action=action), media + icon, addon.getAddonInfo("fanart"))
        finish_directory(request.handle, "videos")
        return

    if request.action == "sync":
        action_sync()
        return

    if request.action == "sync_lan":
        from stv.ui.views import action_sync_lan
        action_sync_lan()
        return

    if request.action in ("live", "vod"):
        render_categories(request, request.action)
        return

    if request.action in ("list_live", "list_vod"):
        media_type = "live" if request.action == "list_live" else "vod"
        render_items(request, media_type, request.params.get("category_id", ""))
        return

    if request.action == "play":
        action_play(request)
        return

    xbmcgui.Dialog().notification("sTv", "Rota estrutural ainda não implementada")
