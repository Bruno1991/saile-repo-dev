from __future__ import annotations

import sys
import os

# Ensure bundled ytmusicapi is accessible before importing it
_lib_path = os.path.dirname(os.path.dirname(__file__))
if _lib_path not in sys.path:
    sys.path.insert(0, _lib_path)

try:
    from ytmusicapi import YTMusic
    import yt_dlp
except ImportError:
    YTMusic = None
    yt_dlp = None


class YtmClient:
    def __init__(self) -> None:
        if YTMusic is None or yt_dlp is None:
            raise RuntimeError("Dependências ytmusicapi ou yt-dlp ausentes.")
        self.ytm = YTMusic()

    def search_songs(self, query: str, limit: int = 20) -> list[dict]:
        results = self.ytm.search(query, filter="songs", limit=limit)
        parsed = []
        for song in results:
            video_id = song.get("videoId")
            if not video_id:
                continue
                
            title = song.get("title", "Desconhecido")
            artists = ", ".join(a.get("name") for a in song.get("artists", []))
            album = song.get("album", {}).get("name") if song.get("album") else ""
            
            thumbnails = song.get("thumbnails", [])
            thumb_url = thumbnails[-1].get("url") if thumbnails else ""
            
            duration = song.get("duration_seconds", 0)
            
            parsed.append({
                "track_id": video_id,
                "title": title,
                "artist": artists,
                "album": album,
                "thumbnail": thumb_url,
                "duration": duration,
                "webpage_url": f"https://music.youtube.com/watch?v={video_id}"
            })
        return parsed

    def resolve_stream(self, video_id: str) -> str:
        url = f"https://music.youtube.com/watch?v={video_id}"
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'skip_download': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info.get("url")
            
        if not audio_url:
            raise ValueError(f"Não foi possível resolver stream para: {video_id}")
            
        return audio_url
