from __future__ import annotations

import time

from stv.app.services import AppContainer
from stv.domain.models import Category, MediaItem


def _parse_categories(media_type: str, generation_id: int, data: object) -> list[Category]:
    if not isinstance(data, list):
        return []
    
    categories = []
    for item in data:
        if not isinstance(item, dict):
            continue
        category_id = str(item.get("category_id", ""))
        name = str(item.get("category_name", ""))
        parent_id = str(item.get("parent_id", "0"))
        
        if category_id and name:
            categories.append(Category(
                category_id=category_id,
                name=name,
                parent_id=parent_id,
                media_type=media_type,
                generation_id=generation_id,
            ))
    return categories


def _parse_streams(media_type: str, generation_id: int, data: object) -> list[MediaItem]:
    if not isinstance(data, list):
        return []
    
    items = []
    for item in data:
        if not isinstance(item, dict):
            continue
        
        # Xtream API uses different keys depending on the type
        item_id = str(item.get("stream_id") or item.get("series_id") or "")
        name = str(item.get("name", ""))
        category_id = str(item.get("category_id", ""))
        
        icon = str(item.get("stream_icon") or item.get("cover") or "")
        extension = str(item.get("container_extension", ""))
        plot = str(item.get("plot", ""))
        
        if item_id and name:
            items.append(MediaItem(
                media_type=media_type,
                item_id=item_id,
                name=name,
                category_id=category_id,
                icon=icon,
                extension=extension,
                plot=plot,
                generation_id=generation_id,
            ))
    return items


def _get_actions(section: str) -> tuple[str, str]:
    mapping = {
        "live": ("get_live_categories", "get_live_streams"),
        "vod": ("get_vod_categories", "get_vod_streams"),
        "series": ("get_series_categories", "get_series"),
    }
    return mapping.get(section, ("", ""))

def ensure_categories_loaded(app: AppContainer, section: str) -> None:
    categories = app.catalog.get_categories(section)
    if categories:
        return  # Já carregado

    cat_action, _ = _get_actions(section)
    if not cat_action:
        return

    generation_id = int(time.time())
    data = app.xtream.request(cat_action)
    parsed = _parse_categories(section, generation_id, data)
    if parsed:
        app.catalog.upsert_categories(parsed)
        # Note: we do not clean obsolete here yet, because we only do full sync of categories once per session/cache expiry.

def ensure_streams_loaded(app: AppContainer, section: str, category_id: str) -> None:
    items = app.catalog.get_media_items(section, category_id)
    if items:
        return  # Já carregado

    _, stream_action = _get_actions(section)
    if not stream_action:
        return

    generation_id = int(time.time())
    data = app.xtream.request(stream_action, category_id=category_id)
    parsed = _parse_streams(section, generation_id, data)
    if parsed:
        app.catalog.upsert_media_items(parsed)
