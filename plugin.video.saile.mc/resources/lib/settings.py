# -*- coding: utf-8 -*-
"""Leitura e validação das configurações do addon."""

from __future__ import absolute_import

import re
from kodi import ADDON, get_setting, notify


def open_settings():
    """Abre a tela de configurações do Kodi."""
    ADDON.openSettings()


def parent_pin():
    """Retorna o PIN configurado, ou string vazia."""
    return get_setting("parent_pin", "").strip()


def is_pin_valid(pin):
    """Valida PIN numérico com 4 a 6 dígitos."""
    return bool(re.match(r"^\d{4,6}$", pin or ""))


def xtream_config():
    """Retorna configuração Xtream."""
    return {
        "host": get_setting("xtream_host", "").strip().rstrip("/"),
        "username": get_setting("xtream_username", "").strip(),
        "password": get_setting("xtream_password", "").strip(),
    }


def youtube_config():
    """Retorna configuração YouTube."""
    return {
        "region": get_setting("youtube_region", "BR").strip() or "BR",
    }


def rapidapi_config():
    """Retorna configuração da RapidAPI e TMDB."""
    return {
        "key": get_setting("rapidapi_key", "").strip(),
        "tmdb_key": get_setting("tmdb_api_key", "").strip(),
    }


def require_xtream():
    """Valida credenciais Xtream."""
    cfg = xtream_config()
    if not cfg["host"] or not cfg["username"] or not cfg["password"]:
        notify("Configure Host, usuário e senha do Xtream.", "warning")
        open_settings()
        return None
    return cfg


def require_rapidapi():
    """Valida chave da RapidAPI."""
    cfg = rapidapi_config()
    if not cfg["key"]:
        notify("Configure a RapidAPI Key.", "warning")
        open_settings()
        return None
    return cfg
