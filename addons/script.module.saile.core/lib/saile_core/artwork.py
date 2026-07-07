from __future__ import annotations

import os

ARTWORK_ADDON_ID = "resource.images.saile"
_ALLOWED_SCOPES = frozenset({"common", "sfy", "stv"})


def _resource_root() -> str:
    import xbmcaddon
    import xbmcvfs

    addon_path = xbmcaddon.Addon(ARTWORK_ADDON_ID).getAddonInfo("path")
    return xbmcvfs.translatePath(os.path.join(addon_path, "resources", "media"))


def artwork_path(scope: str, filename: str) -> str:
    """Retorna um asset compartilhado e bloqueia travessia de diretório."""
    if scope not in _ALLOWED_SCOPES:
        raise ValueError(f"Escopo de artwork inválido: {scope}")
    clean_name = os.path.basename(filename)
    if clean_name != filename or not clean_name:
        raise ValueError("Nome de artwork inválido")
    return os.path.join(_resource_root(), scope, clean_name)


def common_art(filename: str) -> str:
    return artwork_path("common", filename)


def stv_art(filename: str) -> str:
    return artwork_path("stv", filename)


def sfy_art(filename: str) -> str:
    return artwork_path("sfy", filename)
