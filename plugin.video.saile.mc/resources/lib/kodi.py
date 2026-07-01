# -*- coding: utf-8 -*-
"""Compatibilidade com Kodi e fallback leve para testes de sintaxe fora do Kodi."""

from __future__ import absolute_import

import os

try:
    import xbmc  # type: ignore
    import xbmcaddon  # type: ignore
    import xbmcgui  # type: ignore
    import xbmcplugin  # type: ignore
    import xbmcvfs  # type: ignore
    KODI = True
except Exception:  # pragma: no cover
    KODI = False

    class _DummyAddon(object):
        def __init__(self):
            self._settings = {}

        def getAddonInfo(self, key):
            if key == "path":
                return os.getcwd()
            if key == "profile":
                return os.path.join(os.getcwd(), "profile")
            return ""

        def getSetting(self, key):
            return self._settings.get(key, "")

        def setSetting(self, key, value):
            self._settings[key] = value

        def openSettings(self):
            print("openSettings")

    class _DummyDialog(object):
        def notification(self, title, message, icon=None, time=3000):
            print("NOTIFICATION:", title, message)

        def ok(self, title, message):
            print("OK:", title, message)

        def input(self, heading, type=None, option=None):
            return ""

        def yesno(self, heading, line1, line2="", line3=""):
            return False

    class _DummyListItem(object):
        def __init__(self, label=""):
            self.label = label

        def setArt(self, art):
            pass

        def setInfo(self, media_type, info):
            pass

        def setProperty(self, key, value):
            pass

    class _DummyPlugin(object):
        SORT_METHOD_LABEL = 1

        def addDirectoryItem(self, handle, url, listitem, isFolder=True):
            print("ITEM:", getattr(listitem, "label", ""), url, isFolder)

        def endOfDirectory(self, handle, succeeded=True):
            print("END", handle, succeeded)

        def setResolvedUrl(self, handle, succeeded, listitem):
            print("RESOLVE", handle, succeeded, getattr(listitem, "label", ""))

        def addSortMethod(self, handle, sortMethod):
            pass

    class _DummyVfs(object):
        def translatePath(self, path):
            return path

    class _DummyXbmc(object):
        LOGINFO = 1
        LOGWARNING = 2
        LOGERROR = 3

        def log(self, msg, level=1):
            print("LOG", level, msg)

    class _DummyGui(object):
        NOTIFICATION_INFO = "info"
        NOTIFICATION_WARNING = "warning"
        NOTIFICATION_ERROR = "error"
        INPUT_NUMERIC = 0
        ALPHANUM_HIDE_INPUT = 1
        ListItem = _DummyListItem
        Dialog = _DummyDialog

    xbmc = _DummyXbmc()
    xbmcaddon = type("xbmcaddon", (), {"Addon": _DummyAddon})
    xbmcgui = _DummyGui()
    xbmcplugin = _DummyPlugin()
    xbmcvfs = _DummyVfs()

ADDON = xbmcaddon.Addon()
ADDON_ID = "plugin.video.saile.mc"
ADDON_NAME = "Saile Media Center"


def translate(path):
    """Converte caminho especial do Kodi para caminho real."""
    try:
        return xbmcvfs.translatePath(path)
    except AttributeError:
        return xbmcvfs.translatePath(path).decode("utf-8")


def addon_path(*parts):
    """Retorna caminho absoluto dentro do addon."""
    return os.path.join(ADDON.getAddonInfo("path"), *parts)


def profile_path(*parts):
    """Retorna caminho absoluto no perfil gravável do addon."""
    base = translate(ADDON.getAddonInfo("profile"))
    if not os.path.isdir(base):
        os.makedirs(base, exist_ok=True)
    return os.path.join(base, *parts)


def get_setting(key, default=""):
    """Lê setting do Kodi com fallback."""
    value = ADDON.getSetting(key)
    return value if value not in (None, "") else default


def set_setting(key, value):
    """Grava setting do Kodi."""
    ADDON.setSetting(key, value)


def notify(message, level="info"):
    """Mostra notificação no Kodi."""
    icon = xbmcgui.NOTIFICATION_INFO
    if level == "warning":
        icon = xbmcgui.NOTIFICATION_WARNING
    elif level == "error":
        icon = xbmcgui.NOTIFICATION_ERROR
    xbmcgui.Dialog().notification(ADDON_NAME, message, icon, 4000)


def info(message):
    xbmc.log("[SaileMC] " + str(message), xbmc.LOGINFO)


def warning(message):
    xbmc.log("[SaileMC] " + str(message), xbmc.LOGWARNING)


def error(message):
    xbmc.log("[SaileMC] " + str(message), xbmc.LOGERROR)
