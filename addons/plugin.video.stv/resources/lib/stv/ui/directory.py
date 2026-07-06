from __future__ import annotations


def add_folder(handle: int, label: str, url: str, icon: str = "", fanart: str = "") -> None:
    import xbmcgui
    import xbmcplugin

    item = xbmcgui.ListItem(label=label)
    item.setArt({"icon": icon, "thumb": icon, "fanart": fanart})
    xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=item, isFolder=True)


def finish_directory(handle: int, content: str) -> None:
    import xbmcplugin

    xbmcplugin.setContent(handle, content)
    xbmcplugin.endOfDirectory(handle, succeeded=True, cacheToDisc=False)


def add_video_item(handle: int, label: str, url: str, icon: str = "", fanart: str = "", plot: str = "", is_playable: bool = False) -> None:
    import xbmcgui
    import xbmcplugin

    item = xbmcgui.ListItem(label=label)
    item.setArt({"icon": icon, "thumb": icon, "fanart": fanart, "poster": icon})
    
    info = item.getVideoInfoTag()
    info.setTitle(label)
    info.setPlot(plot)
    info.setMediaType("video")

    if is_playable:
        item.setProperty("IsPlayable", "true")

    xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=item, isFolder=not is_playable)


def play_video(handle: int, url: str, label: str, icon: str = "") -> None:
    import xbmcgui
    import xbmcplugin

    item = xbmcgui.ListItem(path=url, label=label)
    item.setArt({"icon": icon, "thumb": icon})
    xbmcplugin.setResolvedUrl(handle, True, item)
