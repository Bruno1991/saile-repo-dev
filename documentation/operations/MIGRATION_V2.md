# Migração para módulos compartilhados V2

1. Preserve `.env` e `.vscode`.
2. Extraia o pacote na raiz do repositório.
3. Execute:

```powershell
python tools/migrate_v2_shared_artwork.py
python tools/bootstrap_artwork.py
python tools/validate_addons.py
python -m unittest discover -s tests -p "test_*.py" -v
python tools/build_repo.py
```

A migração remove somente as antigas pastas duplicadas `resources/media` dos plugins e suas fontes genéricas. Os `icon.png` e `fanart.jpg` próprios permanecem.
