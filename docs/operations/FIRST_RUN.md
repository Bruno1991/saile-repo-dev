# Primeiro uso da estrutura

Na raiz do repositório:

```powershell
python tools/bootstrap_artwork.py
python tools/validate_addons.py
python -m unittest discover -s tests -p "test_*.py" -v
python tools/build_repo.py
```

O último comando gera `site/` com `addons.xml`, checksum, índice HTML e ZIPs versionados.
O `.env` existente permanece somente na máquina de desenvolvimento e não é lido pelo
runtime dos add-ons.
