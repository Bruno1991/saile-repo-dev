from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "addons" / "plugin.audio.sfy" / "resources" / "lib" / "vendor" / "yt_dlp"


def main() -> int:
    parser = argparse.ArgumentParser(description="Copia uma instalação local do pacote yt_dlp para o sFy.")
    parser.add_argument("--source", required=True, type=Path, help="Pasta do pacote Python yt_dlp")
    args = parser.parse_args()
    source = args.source.resolve()
    if source.name != "yt_dlp" or not (source / "__init__.py").is_file():
        raise SystemExit("--source deve apontar para a pasta do pacote yt_dlp")
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)
    shutil.copytree(source, DESTINATION, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    print(f"yt_dlp copiado para {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
