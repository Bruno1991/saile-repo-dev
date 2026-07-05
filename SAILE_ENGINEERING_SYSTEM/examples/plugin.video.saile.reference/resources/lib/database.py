from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from typing import Iterator

import xbmcaddon
import xbmcvfs


SCHEMA = """
CREATE TABLE IF NOT EXISTS playback_history (
    item_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    played_at INTEGER NOT NULL
);
"""


def database_path() -> str:
    addon = xbmcaddon.Addon()
    profile = xbmcvfs.translatePath(addon.getAddonInfo("profile"))
    if not xbmcvfs.exists(profile):
        xbmcvfs.mkdirs(profile)
    return os.path.join(profile, "reference.db")


@contextmanager
def connect() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(database_path(), timeout=5.0)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute("PRAGMA busy_timeout = 5000")
        conn.executescript(SCHEMA)
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def record_playback(item_id: str, title: str, played_at: int) -> None:
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO playback_history(item_id, title, played_at)
            VALUES (?, ?, ?)
            ON CONFLICT(item_id) DO UPDATE SET
                title = excluded.title,
                played_at = excluded.played_at
            """,
            (item_id, title, played_at),
        )
