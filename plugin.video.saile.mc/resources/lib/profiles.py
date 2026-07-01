# -*- coding: utf-8 -*-
"""Perfis e controle dos pais."""

from __future__ import absolute_import

from kodi import xbmcgui, notify
from settings import parent_pin, is_pin_valid
import storage


def bootstrap():
    """Inicializa banco e perfis padrão."""
    storage.init_db()
    storage.ensure_default_profiles()


def verify_pin_if_needed():
    """Pede PIN se existir PIN válido configurado."""
    pin = parent_pin()
    if not pin:
        return True
    if not is_pin_valid(pin):
        notify("PIN configurado é inválido. Use 4 a 6 números.", "warning")
        return False
    typed = xbmcgui.Dialog().input("Digite o PIN", type=xbmcgui.INPUT_NUMERIC, option=xbmcgui.ALPHANUM_HIDE_INPUT)
    if typed == pin:
        return True
    notify("PIN incorreto.", "error")
    return False


def profile_allows(profile, app_id):
    """Verifica se o perfil pode acessar o app."""
    if not profile:
        return False
    if profile.get("kind") == "kids" and app_id in ("sailefy", "storrent"):
        return False
    return True


def get(profile_id):
    """Obtém perfil por id."""
    try:
        return storage.get_profile(int(profile_id))
    except Exception:
        return None


def list_all():
    """Lista todos os perfis."""
    return storage.list_profiles()
