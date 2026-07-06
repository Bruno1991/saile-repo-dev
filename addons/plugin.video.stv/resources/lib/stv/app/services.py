"""Application services coordinate providers, persistence and UI ports.

Keep Kodi imports out of this package so services remain unit-testable.
"""
from __future__ import annotations

import json
import logging

from stv.domain.models import Category, MediaItem
from stv.persistence.database import Database
from stv.providers.xtream.client import XtreamClient


class SyncService:
    def __init__(self, client: XtreamClient, db: Database) -> None:
        self.client = client
        self.db = db

    def sync_live(self) -> None:
        logging.info("Sincronizando TV ao vivo")
        raw_categories = self.client.get_live_categories()
        categories = [
            Category("live", str(c.get("category_id")), str(c.get("category_name")))
            for c in raw_categories if c.get("category_id")
        ]
        self.db.upsert_categories(categories)

        raw_streams = self.client.get_live_streams()
        items = []
        for s in raw_streams:
            if not s.get("stream_id"):
                continue
            items.append(MediaItem(
                media_type="live",
                item_id=str(s["stream_id"]),
                name=str(s.get("name", "")),
                category_id=str(s.get("category_id", "")),
                icon=str(s.get("stream_icon", "")),
                extension="ts",
                payload_json=json.dumps(s)
            ))
        self.db.upsert_media_items(items)

    def sync_vod(self) -> None:
        logging.info("Sincronizando VOD")
        raw_categories = self.client.get_vod_categories()
        categories = [
            Category("vod", str(c.get("category_id")), str(c.get("category_name")))
            for c in raw_categories if c.get("category_id")
        ]
        self.db.upsert_categories(categories)

        raw_streams = self.client.get_vod_streams()
        items = []
        for s in raw_streams:
            if not s.get("stream_id"):
                continue
            items.append(MediaItem(
                media_type="vod",
                item_id=str(s["stream_id"]),
                name=str(s.get("name", "")),
                category_id=str(s.get("category_id", "")),
                icon=str(s.get("stream_icon", "")),
                extension=str(s.get("container_extension", "mp4")),
                payload_json=json.dumps(s)
            ))
        self.db.upsert_media_items(items)
