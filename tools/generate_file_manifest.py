#!/usr/bin/env python3
"""Generate a SHA-256 manifest for files under the repository."""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "FILE_MANIFEST.sha256"
EXCLUDED = {".git", ".venv", "__pycache__", "build", "dist"}

lines = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or path == OUT or any(part in EXCLUDED for part in path.parts):
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    lines.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"wrote {OUT} with {len(lines)} entries")
