from __future__ import annotations

import sqlite3
from typing import Sequence

from stv.domain.models import Category, MediaItem
from stv.persistence.database import Database


class CatalogRepository:
    def __init__(self, db: Database) -> None:
        self.db = db

    def upsert_categories(self, categories: Sequence[Category]) -> None:
        sql = """
        INSERT INTO categories (media_type, category_id, name, parent_id, generation_id, updated_at)
        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT (media_type, category_id) DO UPDATE SET
            name = excluded.name,
            parent_id = excluded.parent_id,
            generation_id = excluded.generation_id,
            updated_at = CURRENT_TIMESTAMP
        """
        data = [
            (c.media_type, c.category_id, c.name, c.parent_id, c.generation_id)
            for c in categories
        ]
        with self.db.connect() as connection:
            connection.executemany(sql, data)

    def upsert_media_items(self, items: Sequence[MediaItem]) -> None:
        sql = """
        INSERT INTO media_items (
            media_type, item_id, category_id, name, icon, fanart, plot, extension, generation_id, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT (media_type, item_id) DO UPDATE SET
            category_id = excluded.category_id,
            name = excluded.name,
            icon = excluded.icon,
            fanart = excluded.fanart,
            plot = excluded.plot,
            extension = excluded.extension,
            generation_id = excluded.generation_id,
            updated_at = CURRENT_TIMESTAMP
        """
        data = [
            (i.media_type, i.item_id, i.category_id, i.name, i.icon, i.fanart, i.plot, i.extension, i.generation_id)
            for i in items
        ]
        with self.db.connect() as connection:
            connection.executemany(sql, data)

    def get_categories(self, media_type: str) -> list[Category]:
        sql = "SELECT * FROM categories WHERE media_type = ? ORDER BY name COLLATE NOCASE"
        with self.db.connect() as connection:
            rows = connection.execute(sql, (media_type,)).fetchall()
        
        return [
            Category(
                category_id=row["category_id"],
                name=row["name"],
                parent_id=row["parent_id"],
                media_type=row["media_type"],
                generation_id=row["generation_id"],
            )
            for row in rows
        ]

    def get_media_items(self, media_type: str, category_id: str) -> list[MediaItem]:
        sql = "SELECT * FROM media_items WHERE media_type = ? AND category_id = ? ORDER BY name COLLATE NOCASE"
        with self.db.connect() as connection:
            rows = connection.execute(sql, (media_type, category_id)).fetchall()
        
        return [
            MediaItem(
                media_type=row["media_type"],
                item_id=row["item_id"],
                name=row["name"],
                category_id=row["category_id"],
                icon=row["icon"],
                fanart=row["fanart"],
                plot=row["plot"],
                extension=row["extension"],
                generation_id=row["generation_id"],
            )
            for row in rows
        ]

    def clean_obsolete_categories(self, media_type: str, current_generation: int) -> int:
        sql = "DELETE FROM categories WHERE media_type = ? AND generation_id < ?"
        with self.db.connect() as connection:
            cursor = connection.execute(sql, (media_type, current_generation))
            return cursor.rowcount

    def clean_obsolete_items(self, media_type: str, current_generation: int) -> int:
        sql = "DELETE FROM media_items WHERE media_type = ? AND generation_id < ?"
        with self.db.connect() as connection:
            cursor = connection.execute(sql, (media_type, current_generation))
            return cursor.rowcount

    def update_playback_progress(self, media_type: str, item_id: str, position: float, total: float) -> None:
        sql = """
        INSERT INTO playback_progress (media_type, item_id, position, total, updated_at)
        VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT (media_type, item_id) DO UPDATE SET
            position = excluded.position,
            total = excluded.total,
            updated_at = CURRENT_TIMESTAMP
        """
        with self.db.connect() as connection:
            connection.execute(sql, (media_type, item_id, position, total))

    def get_playback_progress(self, media_type: str, item_id: str) -> dict | None:
        sql = "SELECT position, total FROM playback_progress WHERE media_type = ? AND item_id = ?"
        with self.db.connect() as connection:
            row = connection.execute(sql, (media_type, item_id)).fetchone()
            if row:
                return {"position": row["position"], "total": row["total"]}
            return None

    def is_cache_valid(self, media_type: str, ttl_hours: int = 12) -> bool:
        sql = "SELECT max(updated_at) as last_update FROM categories WHERE media_type = ?"
        with self.db.connect() as connection:
            row = connection.execute(sql, (media_type,)).fetchone()
            if not row or not row["last_update"]:
                return False
            
            check_sql = "SELECT (julianday('now') - julianday(?)) * 24 as diff_hours"
            diff_row = connection.execute(check_sql, (row["last_update"],)).fetchone()
            if diff_row and diff_row["diff_hours"] <= ttl_hours:
                return True
            return False
