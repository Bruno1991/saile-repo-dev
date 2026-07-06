from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(__file__)
LIB_DIR = os.path.join(ROOT, "resources", "lib")
VENDOR_DIR = os.path.join(LIB_DIR, "vendor")
for path in (VENDOR_DIR, LIB_DIR):
    if path not in sys.path:
        sys.path.insert(0, path)

from sfy.bootstrap import run  # noqa: E402


if __name__ == "__main__":
    run(sys.argv)
