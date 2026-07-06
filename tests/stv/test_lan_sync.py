import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from stv.persistence.database import Database

class TestLanSync(unittest.TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.db1 = Database(Path(self.temp_dir.name) / "db1.sqlite")
        self.db2 = Database(Path(self.temp_dir.name) / "db2.sqlite")
        self.db1.initialize()
        self.db2.initialize()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_merge_user_data_favorites(self):
        with self.db1.connect() as conn:
            conn.execute("INSERT INTO favorites (media_type, item_id, created_at) VALUES ('live', '10', '2023-01-01 10:00:00')")
            
        data = self.db1.export_user_data()
        self.db2.merge_user_data(data)
        
        with self.db2.connect() as conn:
            favs = conn.execute("SELECT * FROM favorites").fetchall()
            self.assertEqual(len(favs), 1)
            self.assertEqual(favs[0]['item_id'], '10')
            self.assertEqual(favs[0]['created_at'], '2023-01-01 10:00:00')

        with self.db2.connect() as conn:
            conn.execute("UPDATE favorites SET created_at = '2023-01-02 10:00:00' WHERE item_id = '10'")
            
        data2 = self.db2.export_user_data()
        self.db1.merge_user_data(data2)
        
        with self.db1.connect() as conn:
            favs1 = conn.execute("SELECT created_at FROM favorites WHERE item_id = '10'").fetchone()
            self.assertEqual(favs1['created_at'], '2023-01-02 10:00:00')

    def test_merge_user_data_playback(self):
        with self.db1.connect() as conn:
            conn.execute("INSERT INTO playback_progress (media_type, item_id, position, total, updated_at) VALUES ('vod', '100', 50.0, 100.0, '2023-01-01 10:00:00')")
            
        self.db2.merge_user_data(self.db1.export_user_data())
        
        with self.db2.connect() as conn:
            prog = conn.execute("SELECT position, updated_at FROM playback_progress WHERE item_id = '100'").fetchone()
            self.assertEqual(prog['position'], 50.0)
            self.assertEqual(prog['updated_at'], '2023-01-01 10:00:00')

        # Simulando Db2 avançando no filme
        with self.db2.connect() as conn:
            conn.execute("UPDATE playback_progress SET position = 75.0, updated_at = '2023-01-02 10:00:00' WHERE item_id = '100'")

        # Tenta injetar um dado mais VELHO a partir do DB1 para o DB2 (deve ser IGNORADO)
        self.db2.merge_user_data(self.db1.export_user_data())
        
        with self.db2.connect() as conn:
            prog_ignored = conn.execute("SELECT position FROM playback_progress WHERE item_id = '100'").fetchone()
            self.assertEqual(prog_ignored['position'], 75.0) # Permanece 75, não sofreu overwrite do 50

if __name__ == "__main__":
    unittest.main()
