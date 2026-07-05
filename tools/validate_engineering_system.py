#!/usr/bin/env python3
"""Validate the SAILE engineering-system structure without external dependencies."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "AGENT_CONSTITUTION.md",
    "SAILE_MASTER_SPEC.md",
    "PROJECT_STATUS.md",
    "SKILLS_INDEX.md",
    "docs/00-governance/DOCUMENT_UPDATE_MATRIX.md",
    "docs/01-architecture/SYSTEM_ARCHITECTURE.md",
    "docs/02-providers/PROVIDER_CONTRACT.md",
    "docs/03-data/MIGRATION_POLICY.md",
    "docs/04-quality/QUALITY_GATES.md",
    "docs/05-security/THREAT_MODEL.md",
    "docs/06-operations/BUILD_AND_RELEASE.md",
    "docs/07-agent/TASK_EXECUTION_PROTOCOL.md",
    "docs/08-adrs/ADR_INDEX.md",
]
FORBIDDEN_TEXT = re.compile(r"\b(lorem ipsum|changeme-secret|real[-_ ]?password)\b", re.I)
SECRET_PATTERNS = [
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED:
        path = ROOT / rel
        if not path.is_file() or path.stat().st_size < 40:
            errors.append(f"missing or empty required file: {rel}")

    skill_files = sorted((ROOT / ".agents" / "skills").glob("**/SKILL.md"))
    if not skill_files:
        errors.append("no SKILL.md files found")
    names: set[str] = set()
    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append(f"missing frontmatter: {path.relative_to(ROOT)}")
            continue
        match = re.search(r"^name:\s*(.+)$", text, re.M)
        if not match:
            errors.append(f"missing skill name: {path.relative_to(ROOT)}")
        else:
            name = match.group(1).strip()
            if name in names:
                errors.append(f"duplicate skill name: {name}")
            names.add(name)

    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in {".git", ".venv"} for part in path.parts):
            continue
        if path.suffix.lower() in {".md", ".py", ".yml", ".yaml", ".json", ".xml", ".toml"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if path.resolve() != Path(__file__).resolve():
                if FORBIDDEN_TEXT.search(text):
                    errors.append(f"forbidden placeholder/secret marker: {path.relative_to(ROOT)}")
                for pattern in SECRET_PATTERNS:
                    if pattern.search(text):
                        errors.append(f"possible secret: {path.relative_to(ROOT)}")
        if path.suffix.lower() == ".xml":
            try:
                ET.parse(path)
            except ET.ParseError as exc:
                errors.append(f"invalid XML {path.relative_to(ROOT)}: {exc}")
        if path.suffix.lower() == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

    print(f"skills: {len(skill_files)}")
    print(f"required documents: {len(REQUIRED)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("SAILE engineering system validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
