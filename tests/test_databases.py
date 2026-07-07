from __future__ import annotations

import sqlite3
import sys
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STV_LIB = ROOT / "addons" / "plugin.video.stv" / "resources" / "lib"
SFY_LIB = ROOT / "addons" / "plugin.audio.sfy" / "resources" / "lib"
sys.path.insert(0, str(STV_LIB))
sys.path.insert(0, str(SFY_LIB))

from sfy.persistence.database import Database as SfyDatabase
from stv.persistence.database import Database as StvDatabase


def table_names(path: Path) -> set[str]:
    with closing(sqlite3.connect(path)) as connection:
        return {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}


class DatabaseTests(unittest.TestCase):
    def test_stv_schema_initializes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stv.db"
            StvDatabase(path).initialize()
            names = table_names(path)
            self.assertTrue({"schema_version", "categories", "media_items", "favorites", "playback_progress"} <= names)

    def test_sfy_schema_initializes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sfy.db"
            SfyDatabase(path).initialize()
            names = table_names(path)
            self.assertTrue({"schema_version", "tracks", "playlists", "playlist_tracks", "playback_history"} <= names)


if __name__ == "__main__":
    unittest.main()
