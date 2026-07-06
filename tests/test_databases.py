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


def get_table_names(database_path: Path) -> set[str]:
    """
    Retorna os nomes das tabelas e garante que a conexão SQLite
    seja realmente fechada antes da remoção do diretório temporário.
    """
    with closing(sqlite3.connect(database_path)) as connection:
        cursor = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            """
        )
        return {str(row[0]) for row in cursor.fetchall()}


class DatabaseTests(unittest.TestCase):
    def test_stv_schema_initializes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database_path = Path(directory) / "stv.db"

            StvDatabase(database_path).initialize()

            table_names = get_table_names(database_path)

            self.assertIn("schema_version", table_names)
            self.assertIn("categories", table_names)
            self.assertIn("media_items", table_names)
            self.assertIn("favorites", table_names)
            self.assertIn("playback_progress", table_names)

    def test_sfy_schema_initializes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database_path = Path(directory) / "sfy.db"

            SfyDatabase(database_path).initialize()

            table_names = get_table_names(database_path)

            self.assertIn("schema_version", table_names)
            self.assertIn("tracks", table_names)
            self.assertIn("favorites", table_names)
            self.assertIn("playlists", table_names)
            self.assertIn("playlist_tracks", table_names)
            self.assertIn("playback_history", table_names)


if __name__ == "__main__":
    unittest.main()