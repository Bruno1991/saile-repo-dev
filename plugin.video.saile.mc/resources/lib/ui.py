# -*- coding: utf-8 -*-
"""Renderização de menus Kodi."""

from __future__ import absolute_import

import json
import urllib.parse

from kodi import xbmcgui, xbmcplugin, addon_path


def build_url(base_url, action, **params):
    """Monta URL do plugin."""
    params["action"] = action
    return base_url + "?" + urllib.parse.urlencode(params)


def art(name):
    """Retorna caminho de arte local."""
    return addon_path("art", name)


def add_directory(handle, base_url, label, action, icon="settings.png", params=None, is_folder=True, info=None):
    """Adiciona item de diretório."""
    params = params or {}
    li = xbmcgui.ListItem(label=label)
    icon_path = art(icon)
    li.setArt({"icon": icon_path, "thumb": icon_path})
    li.setInfo("video", info or {"title": label})
    url = build_url(base_url, action, **params)
    xbmcplugin.addDirectoryItem(handle, url, li, isFolder=is_folder)


def add_playable(handle, base_url, label, action, play_url, icon="settings.png", params=None, info=None, context_menu=None):
    """Adiciona item reproduzível."""
    params = params or {}
    params["play_url"] = play_url
    li = xbmcgui.ListItem(label=label)
    icon_path = icon if str(icon).startswith(("http://", "https://")) else art(icon)
    li.setArt({"icon": icon_path, "thumb": icon_path})
    li.setInfo("video", info or {"title": label})
    li.setProperty("IsPlayable", "true")
    if context_menu:
        li.addContextMenuItems(context_menu)
    url = build_url(base_url, action, **params)
    xbmcplugin.addDirectoryItem(handle, url, li, isFolder=False)


def end(handle):
    """Finaliza diretório."""
    xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_LABEL)
    xbmcplugin.endOfDirectory(handle)


def encode_payload(payload):
    """Codifica payload pequeno para query string."""
    return urllib.parse.quote(json.dumps(payload or {}, ensure_ascii=False).encode("utf-8"))


def decode_payload(value):
    """Decodifica payload da query string."""
    if not value:
        return {}
    try:
        if isinstance(value, bytes):
            value = value.decode("utf-8")
        return json.loads(urllib.parse.unquote(value))
    except Exception:
        return {}
