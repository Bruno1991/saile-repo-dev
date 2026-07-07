from __future__ import annotations

import hashlib
import html
import shutil
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADDONS_DIR = ROOT / "addons"
SITE_DIR = ROOT / "site"
ZIPS_DIR = SITE_DIR / "zips"
EXCLUDED_NAMES = {"__pycache__", ".pytest_cache", ".DS_Store", "Thumbs.db"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".db", ".sqlite", ".log"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def should_include(path: Path) -> bool:
    if any(part in EXCLUDED_NAMES or part.startswith(".") for part in path.parts):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    if path.name.startswith(".env"):
        return False
    return True


def zip_addon(addon_dir: Path, version: str) -> Path:
    destination_dir = ZIPS_DIR / addon_dir.name
    destination_dir.mkdir(parents=True, exist_ok=True)
    zip_path = destination_dir / f"{addon_dir.name}-{version}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in sorted(addon_dir.rglob("*")):
            if source.is_file() and should_include(source.relative_to(addon_dir)):
                archive.write(source, Path(addon_dir.name) / source.relative_to(addon_dir))
    for asset_name in ("icon.png", "fanart.jpg", f"changelog-{version}.txt"):
        source = addon_dir / asset_name
        if source.is_file():
            shutil.copy2(source, destination_dir / asset_name)
    zip_path.with_suffix(zip_path.suffix + ".sha256").write_text(
        sha256(zip_path) + "\n", encoding="utf-8"
    )
    return zip_path


def build_addons_xml(addon_roots: list[ET.Element]) -> bytes:
    root = ET.Element("addons")
    for addon in addon_roots:
        root.append(addon)
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_index(packages: list[tuple[str, str, Path]]) -> str:
    repo_zip = None
    repo_version = None
    other_addons = []
    for addon_id, version, zip_path in packages:
        href = (zip_path.name if addon_id == "repository.srepo" else zip_path.relative_to(SITE_DIR).as_posix())
        if addon_id == "repository.srepo":
            repo_zip = href
            repo_version = version
        else:
            other_addons.append((addon_id, version, href))
            
    cards_html = ""
    for addon_id, version, href in other_addons:
        cards_html += f'''
        <a href="{html.escape(href)}" class="card">
            <h3>{html.escape(addon_id)}</h3>
            <span class="version">v{html.escape(version)}</span>
        </a>'''

    return f"""<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>SAILE Ecosystem - sRepo</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <canvas id="bg-canvas"></canvas>
    <div class="container">
        <header>
            <h1>sRepo</h1>
            <p class="subtitle">Repositório estático Kodi para o ecossistema SAILE</p>
            {"<a href=\"" + html.escape(str(repo_zip)) + "\" class=\"hero-btn\">Download Repository v" + html.escape(str(repo_version)) + "</a>" if repo_zip else ""}
        </header>
        
        <div class="grid">
            {cards_html}
        </div>
        
        <div class="footer-links">
            <a href="SHA256SUMS">Ver SHA256SUMS</a>
        </div>
    </div>
    
    <script src="script.js"></script>
</body>
</html>"""


def main() -> int:
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    ZIPS_DIR.mkdir(parents=True)
    (SITE_DIR / ".nojekyll").write_text("", encoding="utf-8")

    # Copy site templates if they exist
    TEMPLATE_DIR = ROOT / "tools" / "site_template"
    if TEMPLATE_DIR.exists():
        shutil.copytree(TEMPLATE_DIR, SITE_DIR, dirs_exist_ok=True)

    roots: list[ET.Element] = []
    packages: list[tuple[str, str, Path]] = []
    for addon_dir in sorted(path for path in ADDONS_DIR.iterdir() if path.is_dir()):
        root = ET.parse(addon_dir / "addon.xml").getroot()
        addon_id = root.attrib["id"]
        version = root.attrib["version"]
        zip_path = zip_addon(addon_dir, version)
        roots.append(root)
        packages.append((addon_id, version, zip_path))
        if addon_id == "repository.srepo":
            shutil.copy2(zip_path, SITE_DIR / zip_path.name)

    addons_xml = build_addons_xml(roots)
    (SITE_DIR / "addons.xml").write_bytes(addons_xml)
    (SITE_DIR / "addons.xml.md5").write_text(
        hashlib.md5(addons_xml).hexdigest() + "\n", encoding="utf-8"
    )
    sums = [f"{sha256(path)}  {path.relative_to(SITE_DIR).as_posix()}" for _, _, path in packages]
    (SITE_DIR / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")
    (SITE_DIR / "index.html").write_text(build_index(packages), encoding="utf-8")
    print(f"Site gerado em {SITE_DIR} com {len(packages)} add-ons.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
