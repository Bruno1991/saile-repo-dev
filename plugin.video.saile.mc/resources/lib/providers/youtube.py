# -*- coding: utf-8 -*-
"""Provider YouTube Data API via yt-dlp para SaileFy."""

from __future__ import absolute_import

import os
import sys
import xbmc
from kodi import ADDON

PROVIDER = "youtube"
YTDLP_URL = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp"


def _get_yt_dlp():
    """Tenta importar yt_dlp, baixando o zipapp se necessário."""
    try:
        import yt_dlp
        return yt_dlp
    except ImportError:
        pass
    
    # Kodi add-on data dir
    addon_data_dir = xbmc.translatePath(ADDON.getAddonInfo("profile"))
    if not os.path.exists(addon_data_dir):
        os.makedirs(addon_data_dir)
        
    dest = os.path.join(addon_data_dir, "yt-dlp.zip")
    if not os.path.exists(dest):
        import urllib.request
        xbmc.log("[Saile] Baixando yt-dlp para %s" % dest, xbmc.LOGINFO)
        try:
            urllib.request.urlretrieve(YTDLP_URL, dest)
        except Exception as e:
            xbmc.log("[Saile] Falha ao baixar yt-dlp: %s" % e, xbmc.LOGERROR)
            return None
            
    if dest not in sys.path:
        sys.path.insert(0, dest)
        
    try:
        import yt_dlp
        return yt_dlp
    except ImportError:
        xbmc.log("[Saile] Falha ao importar yt-dlp do zipapp", xbmc.LOGERROR)
        return None


def search(query, max_results=25):
    """Busca vídeos de música usando yt-dlp."""
    yt_dlp = _get_yt_dlp()
    if not yt_dlp:
        return []
        
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': False
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            res = ydl.extract_info("ytsearch%d:%s" % (int(max_results), query), download=False)
            if 'entries' in res:
                return [_normalize_item(x) for x in res['entries']]
    except Exception as e:
        xbmc.log("[Saile] Erro no yt-dlp search: %s" % e, xbmc.LOGERROR)
        
    return []


def top_brazil():
    """Consulta top Brasil por termo explícito."""
    return search("top músicas Brasil", 25)


def top_world():
    """Consulta top mundo por termo explícito."""
    return search("global top music", 25)


def category_query(category):
    """Consulta por categoria musical."""
    return search(category + " music", 25)


def _normalize_item(item):
    video_id = item.get("id") or ""
    artwork = ""
    thumbnails = item.get("thumbnails") or []
    if thumbnails:
        # Pega a melhor resolução
        artwork = thumbnails[-1].get("url", "")
        
    return {
        "id": video_id,
        "title": item.get("title") or "Música",
        "plot": item.get("description") or "",
        "artwork": artwork,
        "channel": item.get("uploader") or item.get("channel") or "",
        "published_at": "",
    }


def playback_url(item):
    """Retorna URL compatível com o addon oficial do YouTube no Kodi."""
    video_id = item.get("id") or item.get("external_id") or ""
    if not video_id:
        return ""
    return "plugin://plugin.video.youtube/play/?video_id=" + video_id
