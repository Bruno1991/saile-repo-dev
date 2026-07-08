from __future__ import annotations


def add_folder(handle: int, label: str, url: str, icon: str = "", fanart: str = "", is_folder: bool = True) -> None:
    import xbmcgui
    import xbmcplugin

    item = xbmcgui.ListItem(label=label)
    item.setArt({"icon": icon, "thumb": icon, "fanart": fanart})
    xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=item, isFolder=is_folder)


def finish_directory(handle: int, content: str) -> None:
    import xbmcplugin

    xbmcplugin.setContent(handle, content)
    xbmcplugin.endOfDirectory(handle, succeeded=True, cacheToDisc=False)
