# Inventário do pacote V2

## Resumo

- Add-ons ativos: **5**
- Skills: **105**
- Documentos Markdown: **163**
- Artes fixas compartilhadas: **9**
- ZIPs Kodi gerados em `site/zips/`: **5**
- Arquivos totais no pacote (antes do manifesto final): **330**

## Add-ons

- `plugin.audio.sfy`
- `plugin.video.stv`
- `repository.srepo`
- `resource.images.saile`
- `script.module.saile.core`

## Decisões incorporadas

- `resource.images.saile` centraliza exatamente nove artes fixas.
- `script.module.saile.core` contém apenas infraestrutura compartilhada.
- sFy: Buscar → Minhas Playlists → Sincronizar Dados.
- sTv home: TV ao Vivo → VOD → Séries → Sincronizar Dados.
- sTv seções: Buscar → Favoritos → conteúdo dinâmico.
- Sincronização LAN é manual e não compartilha SQLite.
- Módulo yt-dlp independente depende de prova técnica multiplataforma.
- Serviço contínuo, PVR avançado e canal beta estão adiados.

## Validações executadas

```text
5 add-ons válidos
9 artes compartilhadas válidas
10 testes unitários aprovados
0 segredos conhecidos encontrados
5 ZIPs Kodi gerados
```

## Ferramentas operacionais

- `tools/migrate_v2_shared_artwork.py`
- `tools/bootstrap_artwork.py`
- `tools/validate_addons.py`
- `tools/secret_scan.py`
- `tools/build_repo.py`
- `tools/clean_build.py`
- `tools/print_tree.py`
- `tools/vendor_ytdlp.py`

A lista de arquivos e hashes está em `STRUCTURE_MANIFEST.json`.
