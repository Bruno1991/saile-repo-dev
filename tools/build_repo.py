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


CSS_TEMPLATE = """
:root {
    --bg: #0d0f12;
    --surface: rgba(255, 255, 255, 0.05);
    --surface-hover: rgba(255, 255, 255, 0.1);
    --primary: #4facfe;
    --secondary: #00f2fe;
    --text: #e2e8f0;
    --text-muted: #94a3b8;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: 'Outfit', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 60px 20px;
    background-image: radial-gradient(circle at top right, rgba(79,172,254,0.15), transparent 40%),
                      radial-gradient(circle at bottom left, rgba(0,242,254,0.1), transparent 40%);
    background-attachment: fixed;
}
main {
    width: 100%;
    max-width: 800px;
    animation: fadeIn 0.8s ease-out;
}
header {
    text-align: center;
    margin-bottom: 50px;
}
h1 {
    font-size: 3.5rem;
    font-weight: 600;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}
p.subtitle {
    font-size: 1.2rem;
    color: var(--text-muted);
    font-weight: 300;
}
.container {
    background: var(--surface);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
}
.addon-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.addon-item {
    transition: all 0.3s ease;
}
.addon-link {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 24px;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 14px;
    text-decoration: none;
    color: var(--text);
    border: 1px solid rgba(255, 255, 255, 0.02);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.addon-link:hover {
    background: var(--surface-hover);
    transform: translateY(-4px);
    border-color: rgba(255, 255, 255, 0.15);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}
.addon-name {
    font-weight: 600;
    font-size: 1.3rem;
    letter-spacing: 0.5px;
}
.addon-version {
    background: rgba(79, 172, 254, 0.15);
    color: var(--secondary);
    padding: 6px 14px;
    border-radius: 24px;
    font-size: 0.9rem;
    font-weight: 600;
    border: 1px solid rgba(79, 172, 254, 0.2);
}
.meta-links {
    margin-top: 40px;
    display: flex;
    justify-content: center;
    gap: 30px;
}
.meta-link {
    color: var(--text-muted);
    text-decoration: none;
    font-size: 0.95rem;
    font-weight: 400;
    transition: color 0.3s;
    display: flex;
    align-items: center;
    gap: 6px;
}
.meta-link:hover {
    color: var(--primary);
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
"""

def build_index(packages: list[tuple[str, str, Path]]) -> str:
    rows = []
    for addon_id, version, zip_path in packages:
        href = (zip_path.name if addon_id == "repository.srepo" else zip_path.relative_to(SITE_DIR).as_posix())
        rows.append(
            f'<li class="addon-item"><a class="addon-link" href="{html.escape(href)}">'
            f'<span class="addon-name">{html.escape(addon_id)}</span>'
            f'<span class="addon-version">v{html.escape(version)}</span></a></li>'
        )
    
    html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="description" content="sRepo - Repositório estático Kodi para sTv e sFy. Baixe seus add-ons diretamente.">
    <title>sRepo - Kodi Addons</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <header>
            <h1 id="repo-title">sRepo</h1>
            <p class="subtitle">Repositório estático Kodi para sTv e sFy</p>
        </header>
        <div class="container">
            <ul class="addon-list">
                {rows_html}
            </ul>
        </div>
        <div class="meta-links">
            <a href="addons.xml" class="meta-link" id="link-addons-xml">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                addons.xml
            </a>
            <a href="SHA256SUMS" class="meta-link" id="link-addons-sums">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                SHA256SUMS
            </a>
        </div>
    </main>
</body>
</html>"""
    
    return html_template.replace("{rows_html}", "\n".join(rows))


def main() -> int:
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    ZIPS_DIR.mkdir(parents=True)
    (SITE_DIR / ".nojekyll").write_text("", encoding="utf-8")

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
    (SITE_DIR / "style.css").write_text(CSS_TEMPLATE, encoding="utf-8")
    print(f"Site gerado em {SITE_DIR} com {len(packages)} add-ons.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
