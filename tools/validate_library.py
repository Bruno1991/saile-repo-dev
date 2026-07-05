#!/usr/bin/env python3
from __future__ import annotations

import compileall
import json
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
REQUIRED_FRONTMATTER = {"name", "title", "description", "domain", "triggers"}


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: frontmatter ausente")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: frontmatter não finalizado")
    lines = text[4:end].splitlines()
    result: dict[str, object] = {}
    current_list: str | None = None
    for line in lines:
        if re.match(r"^[a-z_]+:\s*$", line):
            current_list = line.split(":", 1)[0]
            result[current_list] = []
        elif line.startswith("  - ") and current_list:
            value = line[4:].strip().strip('"')
            cast = result[current_list]
            assert isinstance(cast, list)
            cast.append(value)
        elif ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
            current_list = None
    missing = REQUIRED_FRONTMATTER - result.keys()
    if missing:
        raise ValueError(f"{path}: campos ausentes: {sorted(missing)}")
    return result


def main() -> int:
    errors: list[str] = []
    names: set[str] = set()
    manifests: list[dict[str, object]] = []

    for path in sorted(SKILLS.glob("*/*/SKILL.md")):
        try:
            meta = parse_frontmatter(path)
            name = str(meta["name"])
            if name in names:
                raise ValueError(f"nome duplicado: {name}")
            names.add(name)
            body = path.read_text(encoding="utf-8")
            if len(body.splitlines()) < 20:
                raise ValueError("skill curta demais")
            manifests.append({"path": str(path.relative_to(ROOT)), **meta})
        except Exception as exc:
            errors.append(str(exc))

    for xml_path in [
        ROOT / "examples/plugin.video.saile.reference/addon.xml",
        ROOT / "examples/plugin.video.saile.reference/resources/settings.xml",
        ROOT / "templates/addon.xml.template",
        ROOT / "templates/settings.xml.template",
    ]:
        try:
            ET.parse(xml_path)
        except Exception as exc:
            errors.append(f"{xml_path}: XML inválido: {exc}")

    example = ROOT / "examples/plugin.video.saile.reference"
    if not compileall.compile_dir(str(example), quiet=1, force=True):
        errors.append("Falha na compilação sintática do exemplo Python")
    for cache_dir in example.rglob("__pycache__"):
        shutil.rmtree(cache_dir, ignore_errors=True)

    (ROOT / "LIBRARY_MANIFEST.json").write_text(
        json.dumps({"skill_count": len(manifests), "skills": manifests}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    if errors:
        print("VALIDAÇÃO FALHOU")
        for item in errors:
            print(f"- {item}")
        return 1

    print(f"VALIDAÇÃO OK: {len(manifests)} skills, XML válido e Python compilado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
