# sRepo — ecossistema SAILE para Kodi

Monorepo local-first que distribui e desenvolve sTv e sFy por um repositório Kodi hospedado estaticamente no GitHub Pages.

## Add-ons ativos

```text
addons/
├── repository.srepo/
├── resource.images.saile/
├── script.module.saile.core/
├── plugin.video.stv/
└── plugin.audio.sfy/
```

- `repository.srepo`: instala e atualiza o ecossistema.
- `resource.images.saile`: nove ícones fixos compartilhados.
- `script.module.saile.core`: caminhos, artwork, notificações, erros e capacidades.
- `plugin.video.stv`: TV ao vivo, VOD e séries via Xtream.
- `plugin.audio.sfy`: busca e playlists musicais com resolução pelo yt-dlp.

## Navegação oficial

### sFy

```text
Buscar → Minhas Playlists → Sincronizar Dados → conteúdo dinâmico
```

### sTv

```text
Home: TV ao Vivo → VOD → Séries → Sincronizar Dados
Cada seção: Buscar → Favoritos → conteúdo dinâmico
```

A sincronização LAN é sempre manual.

## Artwork compartilhado

```text
resource.images.saile/resources/media/
├── common/
│   ├── search.png
│   ├── erro.png
│   ├── check.png
│   └── sync.png
├── sfy/
│   └── minhas_playlists.png
└── stv/
    ├── live.png
    ├── vod.png
    ├── series.png
    └── favoritos.png
```

Cada add-on ainda mantém `icon.png` e `fanart.jpg` próprios. Capas, pôsteres e thumbnails de conteúdo são dinâmicos.

## Atualização de uma árvore anterior

Depois de extrair este pacote sobre a raiz, execute uma vez:

```powershell
python tools/migrate_v2_shared_artwork.py
python tools/bootstrap_artwork.py
```

O primeiro comando remove somente as antigas pastas de ícones duplicados dos plugins; não toca em `.env`, `.vscode`, bancos ou código de domínio.

## Validação

```powershell
python tools/validate_addons.py
python tools/secret_scan.py
python -m unittest discover -s tests -p "test_*.py" -v
python tools/build_repo.py
```

## Estado

A arquitetura, os módulos compartilhados, a navegação e o empacotamento estão estruturados. Xtream completo, TMDB, reprodução real, yt-dlp multiplataforma e sincronização LAN ainda devem ser implementados e testados em etapas, conforme o roadmap.

## Ordem de leitura do agente

1. `AGENTS.md`
2. `PROJECT_CONSTITUTION.md`
3. `ROADMAP_ARCHITECTURE.md`
4. `REPOSITORY_BLUEPRINT.md`
5. `documentation/architecture/ECOSYSTEM_MODULES.md`
6. `documentation/ui/NAVIGATION_CONTRACT.md`
7. `documentation/ui/ARTWORK_CATALOG.md`
8. `SECURITY_AND_ENV_POLICY.md`
9. `SKILLS_INDEX.md`
