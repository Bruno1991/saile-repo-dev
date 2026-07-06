from __future__ import annotations

from sfy.routing import Request


def run(argv: list[str]) -> None:
    """Kodi entrypoint for the structural sFy bootstrap."""
    import xbmcaddon
    import xbmcgui

    from sfy.ui.directory import add_folder, finish_directory

    request = Request.from_argv(argv)
    addon = xbmcaddon.Addon()
    media = addon.getAddonInfo("path") + "/resources/media/"

    if request.action == "open_settings":
        addon.openSettings()
        return

    if request.action not in {"home", ""}:
        xbmcgui.Dialog().notification("sFy", "Rota estrutural ainda não implementada")

    entries = (
        ("[ Pesquisa ]", "search", "search.png"),
        ("[ Minhas Playlists ]", "playlists", "playlists.png"),
        ("Top Brasil", "top_brazil", "top_brazil.png"),
        ("Top Mundo", "top_world", "top_world.png"),
        ("Categorias", "categories", "categories.png"),
        ("Favoritos", "favorites", "favorites.png"),
        ("Histórico", "history", "history.png"),
        ("Configurações", "open_settings", "settings.png"),
    )
    for label, action, icon in entries:
        add_folder(request.handle, label, request.url(action=action), media + icon, addon.getAddonInfo("fanart"))
    finish_directory(request.handle, "songs")
