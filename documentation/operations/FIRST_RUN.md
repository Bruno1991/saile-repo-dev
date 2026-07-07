# Primeiro uso da estrutura V2

Na raiz do repositório:

```powershell
python tools/migrate_v2_shared_artwork.py
python tools/bootstrap_artwork.py
python tools/validate_addons.py
python tools/secret_scan.py
python -m unittest discover -s tests -p "test_*.py" -v
python tools/build_repo.py
```

A migração é necessária uma única vez ao atualizar a estrutura anterior. O build gera cinco ZIPs e o índice estático em `site/`.
