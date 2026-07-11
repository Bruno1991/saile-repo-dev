import sys
import os

LIB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "addons", "plugin.video.stv", "resources", "lib")
if LIB_DIR not in sys.path:
    sys.path.insert(0, LIB_DIR)

import unittest
from stv.persistence.database import Database
from stv.persistence.repository import CatalogRepository
from stv.domain.models import Category


import tempfile
from pathlib import Path

class PersistenceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db = Database(Path(self.temp_dir.name) / "test.db")
        self.db.initialize()
        self.repo = CatalogRepository(self.db)

    def tearDown(self):
        self.temp_dir.cleanup()
        
    def test_playback_progress(self):
        self.repo.update_playback_progress("vod", "123", 10.5, 100.0)
        progress = self.repo.get_playback_progress("vod", "123")
        self.assertIsNotNone(progress)
        self.assertEqual(progress["position"], 10.5)
        self.assertEqual(progress["total"], 100.0)

    def test_cache_ttl_logic(self):
        self.assertFalse(self.repo.is_cache_valid("live", 12))
        
        cat = Category(category_id="1", name="News", media_type="live", generation_id=1)
        self.repo.upsert_categories([cat])
        
        self.assertTrue(self.repo.is_cache_valid("live", 12))
        
        with self.db.connect() as conn:
            conn.execute("UPDATE categories SET updated_at = datetime('now', '-24 hours')")
            
        self.assertFalse(self.repo.is_cache_valid("live", 12))
        self.assertTrue(self.repo.is_cache_valid("live", 48))
