import unittest
from unittest.mock import MagicMock
from stv.providers.xtream.client import XtreamClient
from stv.infrastructure.http import HttpClient


class TestXtreamClient(unittest.TestCase):
    def setUp(self):
        self.mock_http = MagicMock(spec=HttpClient)
        self.client = XtreamClient("http://example.com", "user", "pass", self.mock_http)

    def test_get_live_categories(self):
        self.mock_http.get_json.return_value = [{"category_id": "1", "category_name": "Test"}]
        cats = self.client.get_live_categories()
        self.assertEqual(len(cats), 1)
        self.assertEqual(cats[0]["category_name"], "Test")
        self.mock_http.get_json.assert_called_once()
        url = self.mock_http.get_json.call_args[0][0]
        self.assertIn("action=get_live_categories", url)
        self.assertIn("username=user", url)
        self.assertIn("password=pass", url)

    def test_stream_url(self):
        url = self.client.stream_url("live", "123")
        self.assertEqual(url, "http://example.com/live/user/pass/123.ts")

        url_vod = self.client.stream_url("vod", "456", "mkv")
        self.assertEqual(url_vod, "http://example.com/movie/user/pass/456.mkv")


if __name__ == "__main__":
    unittest.main()
