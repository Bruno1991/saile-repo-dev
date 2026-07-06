import os
import tempfile
import unittest

from stv.domain.models import Category, MediaItem
from stv.persistence.database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test.db")
        self.db = Database(self.db_path)
        self.db.initialize()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_initialize_creates_tables(self):
        with self.db.connect() as conn:
            row = conn.execute("SELECT version FROM schema_version").fetchone()
            self.assertEqual(row["version"], 1)

    def test_upsert_categories(self):
        categories = [
            Category("live", "cat1", "Category 1"),
            Category("live", "cat2", "Category 2"),
        ]
        self.db.upsert_categories(categories)
        cats = self.db.get_categories("live")
        self.assertEqual(len(cats), 2)
        self.assertEqual(cats[0].name, "Category 1")

        # Test update on conflict
        updated_categories = [
            Category("live", "cat1", "Category 1 Updated"),
        ]
        self.db.upsert_categories(updated_categories)
        cats = self.db.get_categories("live")
        self.assertEqual(cats[0].name, "Category 1 Updated")
        self.assertEqual(len(cats), 2)

    def test_upsert_media_items(self):
        items = [
            MediaItem("live", "id1", "Item 1", "cat1", extension="m3u8"),
            MediaItem("live", "id2", "Item 2", "cat1"),
        ]
        self.db.upsert_media_items(items)
        fetched_items = self.db.get_media_items("live", "cat1")
        self.assertEqual(len(fetched_items), 2)
        self.assertEqual(fetched_items[0].name, "Item 1")
        self.assertEqual(fetched_items[0].extension, "m3u8")

        # Test update on conflict
        updated_items = [
            MediaItem("live", "id1", "Item 1 Updated", "cat1", extension="ts"),
        ]
        self.db.upsert_media_items(updated_items)
        fetched_items = self.db.get_media_items("live", "cat1")
        self.assertEqual(fetched_items[0].name, "Item 1 Updated")
        self.assertEqual(fetched_items[0].extension, "ts")
        self.assertEqual(len(fetched_items), 2)


if __name__ == "__main__":
    unittest.main()
