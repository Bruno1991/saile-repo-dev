from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class VideoItem:
    item_id: str
    title: str
    plot: str = ""
    thumb: str = ""
    stream_url: Optional[str] = None
