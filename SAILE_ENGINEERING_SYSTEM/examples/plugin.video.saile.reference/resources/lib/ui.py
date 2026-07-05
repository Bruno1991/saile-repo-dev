from __future__ import annotations

from typing import Iterable

import xbmcgui
import xbmcplugin

from .models import VideoItem


def show_home(handle: int, base_url: str, build_url, items: Iterable[VideoItem]) -> None:
    xbmcplugin.setPluginCategory(handle, "SAILE Reference")
    xbmcplugin.setContent(handle, "videos")

    directory_items = []
    for video in items:
        list_item = xbmcgui.ListItem(label=video.title, offscreen=True)
        list_item.setProperty("IsPlayable", "true")
        list_item.setArt({"thumb": video.thumb, "icon": video.thumb})
        try:
            info_tag = list_item.getVideoInfoTag()
            info_tag.setTitle(video.title)
            info_tag.setPlot(video.plot)
        except AttributeError:
            list_item.setInfo("video", {"title": video.title, "plot": video.plot})

        url = build_url(base_url, "play", item_id=video.item_id)
        directory_items.append((url, list_item, False))

    xbmcplugin.addDirectoryItems(handle, directory_items, totalItems=len(directory_items))
    xbmcplugin.endOfDirectory(handle, succeeded=True)


def resolve_playback(handle: int, stream_url: str) -> None:
    item = xbmcgui.ListItem(path=stream_url)
    xbmcplugin.setResolvedUrl(handle, True, item)


def resolve_failure(handle: int, message: str) -> None:
    xbmcgui.Dialog().notification("SAILE Reference", message, xbmcgui.NOTIFICATION_ERROR, 5000)
    xbmcplugin.setResolvedUrl(handle, False, xbmcgui.ListItem())
