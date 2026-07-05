#!/usr/bin/env python3
from __future__ import annotations

import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADDON = ROOT / "examples" / "plugin.video.saile.reference"
OUTPUT = ROOT / "examples" / "plugin.video.saile.reference-0.1.0.zip"
EXCLUDED_PARTS = {"__pycache__", ".pytest_cache"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}

with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(ADDON.rglob("*")):
        if path.is_dir():
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        if path.suffix in EXCLUDED_SUFFIXES:
            continue
        arcname = Path(ADDON.name) / path.relative_to(ADDON)
        archive.write(path, arcname.as_posix())

print(OUTPUT)
