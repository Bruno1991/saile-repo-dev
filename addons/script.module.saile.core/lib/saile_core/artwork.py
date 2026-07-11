from __future__ import annotations

import os

ARTWORK_ADDON_ID = "resource.images.saile"
_ALLOWED_SCOPES = frozenset({"common", "sfy", "stv"})


def _resource_root() -> str:
    return "resource://resource.images.saile/media"


def artwork_path(scope: str, filename: str) -> str:
    """Retorna um asset compartilhado absoluto do sistema de arquivos."""
    return artwork_absolute_path(scope, filename)


def artwork_absolute_path(scope: str, filename: str) -> str:
    """Retorna o caminho absoluto de um asset no sistema de arquivos."""
    import xbmcaddon
    if scope not in _ALLOWED_SCOPES:
        raise ValueError(f"Escopo de artwork inválido: {scope}")
    clean_name = os.path.basename(filename)
    addon_path = xbmcaddon.Addon("resource.images.saile").getAddonInfo("path")
    # Kodi AddonInfo path might come as a unicode string in Py3 and uses OS path separators
    return os.path.join(addon_path, "resources", "media", scope, clean_name)


def common_art(filename: str) -> str:
    return artwork_path("common", filename)


def stv_art(filename: str) -> str:
    return artwork_path("stv", filename)


def sfy_art(filename: str) -> str:
    return artwork_path("sfy", filename)
