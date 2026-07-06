from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADDONS = ROOT / "addons"
EXPECTED = {"repository.srepo", "plugin.video.stv", "plugin.audio.sfy"}


def validate_addon(addon_dir: Path) -> list[str]:
    errors: list[str] = []
    xml_path = addon_dir / "addon.xml"
    if not xml_path.is_file():
        return [f"{addon_dir.name}: addon.xml ausente"]
    try:
        root = ET.parse(xml_path).getroot()
    except ET.ParseError as exc:
        return [f"{addon_dir.name}: XML inválido: {exc}"]
    if root.tag != "addon":
        errors.append(f"{addon_dir.name}: raiz XML deve ser <addon>")
    if root.attrib.get("id") != addon_dir.name:
        errors.append(f"{addon_dir.name}: id do addon.xml não coincide com a pasta")
    for attr in ("id", "name", "version", "provider-name"):
        if not root.attrib.get(attr):
            errors.append(f"{addon_dir.name}: atributo obrigatório ausente: {attr}")
    for asset in ("icon.png", "fanart.jpg"):
        if not (addon_dir / asset).is_file():
            errors.append(f"{addon_dir.name}: {asset} ausente")
    for extension in root.findall("extension"):
        library = extension.attrib.get("library")
        if library and not (addon_dir / library).is_file():
            errors.append(f"{addon_dir.name}: entrypoint ausente: {library}")
    settings = addon_dir / "resources" / "settings.xml"
    if settings.is_file():
        try:
            settings_root = ET.parse(settings).getroot()
            if settings_root.tag != "settings":
                errors.append(f"{addon_dir.name}: resources/settings.xml inválido")
        except ET.ParseError as exc:
            errors.append(f"{addon_dir.name}: settings.xml inválido: {exc}")
    return errors


def main() -> int:
    actual = {path.name for path in ADDONS.iterdir() if path.is_dir()}
    errors = [f"Add-on obrigatório ausente: {addon_id}" for addon_id in sorted(EXPECTED - actual)]
    for addon_id in sorted(EXPECTED & actual):
        errors.extend(validate_addon(ADDONS / addon_id))
    if errors:
        print("Validação falhou:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Add-ons válidos: " + ", ".join(sorted(EXPECTED)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
