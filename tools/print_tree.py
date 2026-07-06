from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {".git", "site", "__pycache__", ".pytest_cache"}


def walk(path: Path, prefix: str = "") -> None:
    entries = [item for item in sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower())) if item.name not in EXCLUDE]
    for index, item in enumerate(entries):
        last = index == len(entries) - 1
        branch = "└── " if last else "├── "
        print(prefix + branch + item.name + ("/" if item.is_dir() else ""))
        if item.is_dir():
            walk(item, prefix + ("    " if last else "│   "))


print(ROOT.name + "/")
walk(ROOT)
