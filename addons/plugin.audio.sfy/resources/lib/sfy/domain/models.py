from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Track:
    track_id: str
    title: str
    artist: str = ""
    album: str = ""
    thumbnail: str = ""
    webpage_url: str = ""
    duration: float = 0.0
