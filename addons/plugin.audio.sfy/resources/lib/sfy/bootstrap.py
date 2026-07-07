from __future__ import annotations

from sfy.navigation_contract import HOME_ENTRIES
from sfy.routing import Request


def _show_home(request: Request, fanart: str) -> None:
    from saile_core.artwork import artwork_path
    from sfy.app.services import ChartsService
    from sfy.ui.directory import add_folder, finish_directory

    # 1. Fixed navigation items
    for label, action, scope, filename in HOME_ENTRIES:
        add_folder(
            request.handle,
            label,
            request.url(action=action),
            artwork_path(scope, filename),
            fanart,
        )

    # 2. Dynamic content below the fixed items
    charts_service = ChartsService()
    for chart in charts_service.get_home_charts():
        add_folder(
            request.handle,
            chart.title,
            request.url(action="resolve", url=chart.url),
            chart.thumbnail,
            fanart,
        )

    finish_directory(request.handle, "songs")


def run(argv: list[str]) -> None:
    """Entrypoint estrutural com o contrato oficial de navegação do sFy."""
    import xbmcaddon

    from saile_core.notifications import notify_info

    request = Request.from_argv(argv)
    addon = xbmcaddon.Addon()
    fanart = addon.getAddonInfo("fanart")

    if request.action in {"", "home"}:
        _show_home(request, fanart)
        return

    if request.action == "sync":
        notify_info("sFy", "Sincronização LAN manual ainda não implementada")
    else:
        notify_info("sFy", "Rota estrutural ainda não implementada")
    _show_home(request, fanart)
