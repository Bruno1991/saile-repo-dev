from __future__ import annotations

import xbmc


PREFIX = "[plugin.video.saile.reference]"


def info(message: str) -> None:
    xbmc.log(f"{PREFIX} {message}", xbmc.LOGINFO)


def error(message: str) -> None:
    xbmc.log(f"{PREFIX} {message}", xbmc.LOGERROR)
