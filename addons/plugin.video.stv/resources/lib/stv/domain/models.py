from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    category_id: str
    name: str
    parent_id: str = "0"
    media_type: str = "live"
    generation_id: int = 0


@dataclass(frozen=True)
class MediaItem:
    media_type: str
    item_id: str
    name: str
    category_id: str = ""
    icon: str = ""
    fanart: str = ""
    plot: str = ""
    extension: str = ""
    generation_id: int = 0
