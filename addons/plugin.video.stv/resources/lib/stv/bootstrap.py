from __future__ import annotations

from stv.navigation_contract import HOME_ENTRIES, SECTION_FIXED_ENTRIES, VALID_SECTIONS
from stv.routing import Request


def _icon(scope: str, filename: str) -> str:
    from saile_core.artwork import artwork_path

    return artwork_path(scope, filename)


def _show_home(request: Request, fanart: str) -> None:
    from stv.ui.directory import add_folder, finish_directory

    for label, action, section, scope, filename in HOME_ENTRIES:
        url = request.url(action=action, section=section) if section else request.url(action=action)
        add_folder(request.handle, label, url, _icon(scope, filename), fanart)
    finish_directory(request.handle, "videos")


def _show_section(request: Request, section: str, fanart: str) -> None:
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
        
    # 2. Categorias e itens dinâmicos (Hooks preparados para o SQLite/Xtream)
    # Por hora adicionamos stubs simulando categorias do banco
    dynamic_categories = [
        {"label": f"Categoria 1 ({section})", "action": "category", "id": "1"},
        {"label": f"Categoria 2 ({section})", "action": "category", "id": "2"},
    ]
    for cat in dynamic_categories:
        add_folder(
            request.handle,
            cat["label"],
            request.url(action=cat["action"], section=section, category_id=cat["id"]),
            _icon("common", "check.png"),  # Placeholder artwork
            fanart,
        )

    finish_directory(request.handle, "videos")


def run(argv: list[str]) -> None:
    """Entrypoint estrutural com o contrato oficial de navegação do sTv."""
    import xbmcaddon

    from saile_core.notifications import notify_info

    request = Request.from_argv(argv)
    addon = xbmcaddon.Addon()
    fanart = addon.getAddonInfo("fanart")

    if request.action in {"", "home"}:
        _show_home(request, fanart)
        return

    if request.action == "section":
        section = request.params.get("section", "")
        if section in VALID_SECTIONS:
            _show_section(request, section, fanart)
            return

    if request.action == "sync":
        notify_info("sTv", "Sincronização LAN manual ainda não implementada")
        _show_home(request, fanart)
        return

    if request.action in {"search", "favorites"}:
        notify_info("sTv", "Rota estrutural ainda não implementada")
        section = request.params.get("section", "")
        if section in VALID_SECTIONS:
            _show_section(request, section, fanart)
            return

    _show_home(request, fanart)
