#!/usr/bin/env python3
"""Inspect a SAILE repository and report health without modifying it."""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check_addon(path: Path, expected_id: str) -> list[str]:
    issues: list[str] = []
    xml = path / "addon.xml"
    if not path.exists():
        issues.append(f"missing directory: {path.name}")
        return issues
    if not xml.exists():
        issues.append(f"missing {xml.relative_to(ROOT)}")
        return issues
    try:
        root = ET.parse(xml).getroot()
    except ET.ParseError as exc:
        issues.append(f"invalid XML {xml}: {exc}")
        return issues
    if root.attrib.get("id") != expected_id:
        issues.append(f"unexpected addon id in {xml}: {root.attrib.get('id')!r}")
    if not root.attrib.get("version"):
        issues.append(f"missing version in {xml}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-release", action="store_true")
    args = parser.parse_args()
    issues: list[str] = []
    warnings: list[str] = []

    addon_path = ROOT / "plugin.video.saile.mc"
    repository_path = ROOT / "repository.saile"
    if addon_path.exists():
        issues += check_addon(addon_path, "plugin.video.saile.mc")
    else:
        warnings.append("real SAILE add-on is not present; this may be the standalone engineering package")
    if repository_path.exists():
        issues += check_addon(repository_path, "repository.saile")
    else:
        warnings.append("repository add-on is not present")

    py_files = [p for p in ROOT.rglob("*.py") if not any(x in p.parts for x in (".git", ".venv", "build", "dist"))]
    for path in py_files:
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except Exception as exc:
            issues.append(f"python syntax error {path.relative_to(ROOT)}: {exc}")

    forbidden_parts = {".env", ".git", "__pycache__"}
    for zpath in ROOT.rglob("*.zip"):
        try:
            with zipfile.ZipFile(zpath) as zf:
                for name in zf.namelist():
                    parts = set(Path(name).parts)
                    if parts & forbidden_parts or name.endswith((".pyc", ".log", ".db")):
                        issues.append(f"forbidden file in {zpath.relative_to(ROOT)}: {name}")
        except zipfile.BadZipFile:
            issues.append(f"invalid ZIP: {zpath.relative_to(ROOT)}")

    print(f"python files inspected: {len(py_files)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for issue in issues:
        print(f"ISSUE: {issue}")

    if args.strict_release and (issues or warnings):
        return 1
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
