# Inventário do repositório organizado

Este inventário descreve a estrutura final pronta para ser extraída na raiz de
`saile-repo-dev`. `.env` e `.vscode/` não fazem parte do pacote.

## Add-ons criados

| ID | Versão inicial | Estado estrutural |
|---|---:|---|
| `repository.srepo` | `1.0.0` | Manifesto de repositório, icon, fanart e ZIP de instalação |
| `plugin.video.stv` | `0.1.0` | Bootstrap Kodi, arquitetura modular, Xtream/TMDB/SQLite e artes |
| `plugin.audio.sfy` | `0.1.0` | Bootstrap Kodi, arquitetura modular, yt-dlp/SQLite e artes |

## Contagem por área

| Área | Arquivos |
|---|---:|
| `.agents` | 100 |
| `.env.example` | 1 |
| `.github` | 4 |
| `.gitignore` | 1 |
| `addons` | 86 |
| `AGENTS.md` | 1 |
| `artwork` | 40 |
| `COMPATIBILITY_MATRIX.md` | 1 |
| `docs` | 13 |
| `examples` | 4 |
| `LICENSE` | 1 |
| `Makefile` | 1 |
| `OFFICIAL_REFERENCE_MAP.md` | 1 |
| `PACKAGE_INVENTORY.md` | 1 |
| `PROJECT_CONSTITUTION.md` | 1 |
| `pyproject.toml` | 1 |
| `README.md` | 1 |
| `REPOSITORY_BLUEPRINT.md` | 1 |
| `ROADMAP_ARCHITECTURE.md` | 1 |
| `ROADMAP_TRACEABILITY_MATRIX.md` | 1 |
| `schemas` | 3 |
| `SECURITY_AND_ENV_POLICY.md` | 1 |
| `site` | 21 |
| `skills-manifest.json` | 1 |
| `SKILLS_INDEX.md` | 1 |
| `STRUCTURE_MANIFEST.json` | 1 |
| `templates` | 5 |
| `tests` | 6 |
| `tools` | 7 |
| `TREE_FINAL.txt` | 1 |

## Ferramentas operacionais

- `tools/bootstrap_artwork.py`: copia as 38 artes genéricas aos add-ons.
- `tools/validate_addons.py`: valida IDs, XML, entrypoints e assets.
- `tools/secret_scan.py`: bloqueia padrões conhecidos de segredos.
- `tools/build_repo.py`: gera `site/`, `addons.xml`, checksum e ZIPs.
- `tools/vendor_ytdlp.py`: prepara a dependência vendorizada do sFy.
- `tools/clean_build.py`: remove saídas geradas.
- `tools/print_tree.py`: imprime a árvore do projeto.

## Verificações executadas

- XML dos três add-ons validado.
- `settings.xml` dos plugins validado como XML.
- 38 arquivos de artwork copiados.
- Testes unitários executados com sucesso.
- Build estático do GitHub Pages gerado com três ZIPs.
- Varredura de segredos concluída sem achados.
- Conteúdo dos ZIPs verificado sem `.env`, SQLite, logs, `__pycache__` ou `.pyc`.

A lista completa está em `STRUCTURE_MANIFEST.json` e a árvore em `TREE_FINAL.txt`.
