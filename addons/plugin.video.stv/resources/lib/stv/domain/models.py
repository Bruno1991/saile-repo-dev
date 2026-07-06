from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    media_type: str
    category_id: str
    name: str


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
    payload_json: str = "{}"
