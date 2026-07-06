from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ResolvedAudio:
    url: str
    title: str
    artist: str
    thumbnail: str
    webpage_url: str
    headers: dict[str, str]


class YtDlpResolver:
    def __init__(self, format_selector: str = "bestaudio/best") -> None:
        self.format_selector = format_selector

    @staticmethod
    def _module() -> Any:
        try:
            import yt_dlp
        except ImportError as exc:
            raise RuntimeError(
                "yt-dlp não está empacotado. Execute tools/vendor_ytdlp.py antes do build."
            ) from exc
        return yt_dlp

    def search(self, query: str, limit: int = 20) -> list[dict[str, object]]:
        yt_dlp = self._module()
        options = {"quiet": True, "no_warnings": True, "extract_flat": True, "skip_download": True}
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(f"ytsearch{limit}:{query}", download=False)
        return list((info or {}).get("entries") or [])

    def resolve(self, webpage_url: str) -> ResolvedAudio:
        yt_dlp = self._module()
        options = {
            "quiet": True,
            "no_warnings": True,
            "skip_download": True,
            "noplaylist": True,
            "format": self.format_selector,
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(webpage_url, download=False)
            clean = ydl.sanitize_info(info)
        return ResolvedAudio(
            url=str(clean.get("url") or ""),
            title=str(clean.get("title") or ""),
            artist=str(clean.get("artist") or clean.get("uploader") or ""),
            thumbnail=str(clean.get("thumbnail") or ""),
            webpage_url=str(clean.get("webpage_url") or webpage_url),
            headers={str(k): str(v) for k, v in (clean.get("http_headers") or {}).items()},
        )
