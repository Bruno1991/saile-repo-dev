#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera zips, addons.xml, addons.xml.md5 e index.html para GitHub Pages."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ADDON_DIRS = [ROOT / "plugin.video.saile.mc", ROOT / "repository.saile"]
EXCLUDES = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".git",
}
BLOCKED_SUFFIXES = {".db", ".sqlite", ".sqlite3", ".log", ".pyc", ".pyo", ".tmp", ".bak"}
BLOCKED_NAMES = {".env"}


def read_addon_meta(addon_dir: Path):
    tree = ET.parse(addon_dir / "addon.xml")
    root = tree.getroot()
    return root.attrib["id"], root.attrib["version"], root.attrib.get("name", root.attrib["id"])


def should_include(path: Path) -> bool:
    parts = set(path.parts)
    if parts & EXCLUDES:
        return False
    if path.name in BLOCKED_NAMES:
        return False
    if path.suffix.lower() in BLOCKED_SUFFIXES:
        return False
    return True


def zip_addon(addon_dir: Path, out_dir: Path) -> Path:
    addon_id, version, _ = read_addon_meta(addon_dir)
    target_dir = out_dir / addon_id
    target_dir.mkdir(parents=True, exist_ok=True)
    zip_path = target_dir / f"{addon_id}-{version}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in addon_dir.rglob("*"):
            if path.is_file() and should_include(path):
                arcname = addon_dir.name + "/" + str(path.relative_to(addon_dir)).replace(os.sep, "/")
                zf.write(path, arcname)
    return zip_path


def build_addons_xml(addon_dirs):
    chunks = ['<?xml version="1.0" encoding="UTF-8"?>', '<addons>']
    for addon_dir in addon_dirs:
        text = (addon_dir / "addon.xml").read_text(encoding="utf-8").strip()
        text = re.sub(r"^<\?xml[^>]+>\s*", "", text)
        chunks.append(text)
    chunks.append("</addons>")
    return "\n".join(chunks) + "\n"


def write_index(repo_url: str, zip_paths):
    rows = []
    for zp in zip_paths:
        rel = zp.relative_to(ROOT).as_posix()
        rows.append(f'<li><a href="{rel}">{rel}</a></li>')
    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Saile Media Center Repository</title>
<style>
body {{ font-family: Arial, sans-serif; background:#111827; color:#f9fafb; margin:40px; }}
a {{ color:#93c5fd; }}
.card {{ max-width:900px; background:#1f2937; padding:24px; border-radius:16px; }}
code {{ background:#374151; padding:2px 6px; border-radius:6px; }}
</style>
</head>
<body>
<div class="card">
<h1>Saile Media Center Repository</h1>
<p>Fonte Kodi/GitHub Pages: <code>{repo_url}</code></p>
<p>Arquivos principais:</p>
<ul>
{''.join(rows)}
</ul>
<p>Para instalar no Kodi, instale primeiro o zip do <code>repository.saile</code> e depois instale o Saile Media Center pelo repositório.</p>
</div>
</body>
</html>
"""
    (ROOT / "index.html").write_text(html, encoding="utf-8")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-url", default="https://bruno1991.github.io/saile-repo-dev/", help="URL base do GitHub Pages")
    args = parser.parse_args(argv)

    out_dir = ROOT / "zips"
    out_dir.mkdir(exist_ok=True)
    zip_paths = []
    for addon_dir in ADDON_DIRS:
        if not (addon_dir / "addon.xml").exists():
            raise SystemExit(f"addon.xml não encontrado em {addon_dir}")
        zip_paths.append(zip_addon(addon_dir, out_dir))

    addons_xml = build_addons_xml(ADDON_DIRS)
    (ROOT / "addons.xml").write_text(addons_xml, encoding="utf-8")
    md5 = hashlib.md5(addons_xml.encode("utf-8")).hexdigest()
    (ROOT / "addons.xml.md5").write_text(md5, encoding="utf-8")
    write_index(args.repo_url.rstrip("/") + "/", zip_paths)

    print("Repositório gerado:")
    print("- addons.xml")
    print("- addons.xml.md5")
    print("- index.html")
    for zp in zip_paths:
        print("-", zp.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
