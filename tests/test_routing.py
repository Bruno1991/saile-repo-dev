from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "addons" / "plugin.video.stv" / "resources" / "lib"))
sys.path.insert(0, str(ROOT / "addons" / "plugin.audio.sfy" / "resources" / "lib"))

from sfy.routing import Request as SfyRequest
from stv.routing import Request as StvRequest


class RoutingTests(unittest.TestCase):
    def test_stv_request(self) -> None:
        request = StvRequest.from_argv(["plugin://plugin.video.stv/", "7", "?action=live&category_id=2"])
        self.assertEqual(request.handle, 7)
        self.assertEqual(request.action, "live")
        self.assertIn("category_id=2", request.url(action="items", category_id=2))

    def test_sfy_request(self) -> None:
        request = SfyRequest.from_argv(["plugin://plugin.audio.sfy/", "8", "?action=search"])
        self.assertEqual(request.handle, 8)
        self.assertEqual(request.action, "search")


if __name__ == "__main__":
    unittest.main()
