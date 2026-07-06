from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from stv.domain.models import Category, MediaItem


SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS schema_version (version INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS categories (
    media_type TEXT NOT NULL,
    category_id TEXT NOT NULL,
    name TEXT NOT NULL,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (media_type, category_id)
);
CREATE TABLE IF NOT EXISTS media_items (
    media_type TEXT NOT NULL,
    item_id TEXT NOT NULL,
    category_id TEXT NOT NULL DEFAULT '',
    name TEXT NOT NULL,
    icon TEXT NOT NULL DEFAULT '',
    fanart TEXT NOT NULL DEFAULT '',
    plot TEXT NOT NULL DEFAULT '',
    extension TEXT NOT NULL DEFAULT '',
    payload_json TEXT NOT NULL DEFAULT '{}',
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (media_type, item_id)
);
CREATE INDEX IF NOT EXISTS idx_media_items_category
ON media_items(media_type, category_id, name COLLATE NOCASE);
CREATE TABLE IF NOT EXISTS favorites (
    media_type TEXT NOT NULL,
    item_id TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (media_type, item_id)
);
CREATE TABLE IF NOT EXISTS playback_progress (
    media_type TEXT NOT NULL,
    item_id TEXT NOT NULL,
    position REAL NOT NULL DEFAULT 0,
    total REAL NOT NULL DEFAULT 0,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (media_type, item_id)
);
"""


class Database:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.path, timeout=10)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA journal_mode = WAL")
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript(SCHEMA)
            row = connection.execute("SELECT COUNT(*) AS total FROM schema_version").fetchone()
            if row["total"] == 0:
                connection.execute("INSERT INTO schema_version(version) VALUES (1)")

    def upsert_categories(self, categories: list[Category]) -> None:
        with self.connect() as conn:
            conn.executemany(
                """
                INSERT INTO categories (media_type, category_id, name, updated_at)
                VALUES (:media_type, :category_id, :name, CURRENT_TIMESTAMP)
                ON CONFLICT(media_type, category_id) DO UPDATE SET
                    name = excluded.name,
                    updated_at = excluded.updated_at
                """,
                [{"media_type": c.media_type, "category_id": c.category_id, "name": c.name} for c in categories]
            )

    def upsert_media_items(self, items: list[MediaItem]) -> None:
        with self.connect() as conn:
            conn.executemany(
                """
                INSERT INTO media_items (media_type, item_id, category_id, name, icon, fanart, plot, extension, payload_json, updated_at)
                VALUES (:media_type, :item_id, :category_id, :name, :icon, :fanart, :plot, :extension, :payload_json, CURRENT_TIMESTAMP)
                ON CONFLICT(media_type, item_id) DO UPDATE SET
                    category_id = excluded.category_id,
                    name = excluded.name,
                    icon = excluded.icon,
                    fanart = excluded.fanart,
                    plot = excluded.plot,
                    extension = excluded.extension,
                    payload_json = excluded.payload_json,
                    updated_at = excluded.updated_at
                """,
                [{
                    "media_type": i.media_type,
                    "item_id": i.item_id,
                    "category_id": i.category_id,
                    "name": i.name,
                    "icon": i.icon,
                    "fanart": i.fanart,
                    "plot": i.plot,
                    "extension": i.extension,
                    "payload_json": i.payload_json
                } for i in items]
            )

    def get_categories(self, media_type: str) -> list[Category]:
        with self.connect() as conn:
            cursor = conn.execute(
                "SELECT media_type, category_id, name FROM categories WHERE media_type = ? ORDER BY name COLLATE NOCASE",
                (media_type,)
            )
            return [Category(**dict(row)) for row in cursor]

    def get_media_items(self, media_type: str, category_id: str) -> list[MediaItem]:
        with self.connect() as conn:
            cursor = conn.execute(
                """
                SELECT media_type, item_id, name, category_id, icon, fanart, plot, extension, payload_json 
                FROM media_items 
                WHERE media_type = ? AND category_id = ? 
                ORDER BY name COLLATE NOCASE
                """,
                (media_type, category_id)
            )
            return [MediaItem(**dict(row)) for row in cursor]

    def export_user_data(self) -> dict[str, list[dict]]:
        with self.connect() as conn:
            favs = [dict(row) for row in conn.execute("SELECT * FROM favorites").fetchall()]
            prog = [dict(row) for row in conn.execute("SELECT * FROM playback_progress").fetchall()]
            return {"favorites": favs, "playback_progress": prog}

    def merge_user_data(self, remote_data: dict[str, list[dict]]) -> None:
        favs = remote_data.get("favorites", [])
        prog = remote_data.get("playback_progress", [])
        
        with self.connect() as conn:
            if favs:
                conn.executemany(
                    """
                    INSERT INTO favorites (media_type, item_id, created_at)
                    VALUES (:media_type, :item_id, :created_at)
                    ON CONFLICT(media_type, item_id) DO UPDATE SET
                        created_at = excluded.created_at
                    WHERE excluded.created_at > favorites.created_at
                    """,
                    favs
                )
            if prog:
                conn.executemany(
                    """
                    INSERT INTO playback_progress (media_type, item_id, position, total, updated_at)
                    VALUES (:media_type, :item_id, :position, :total, :updated_at)
                    ON CONFLICT(media_type, item_id) DO UPDATE SET
                        position = excluded.position,
                        total = excluded.total,
                        updated_at = excluded.updated_at
                    WHERE excluded.updated_at > playback_progress.updated_at
                    """,
                    prog
                )
