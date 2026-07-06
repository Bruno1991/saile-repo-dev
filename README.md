# sRepo — monorepo organizado

Este pacote já está estruturado para ser extraído diretamente na raiz de `saile-repo-dev`.
Ele não inclui nem altera `.env` ou `.vscode/`. Os três add-ons vivem em `addons/`, as
skills em `.agents/skills/`, as artes genéricas em `artwork/generic/` e o GitHub Pages é
gerado em `site/` por `tools/build_repo.py`.

> Estado atual: scaffold estrutural instalável, com menus iniciais, validação, testes e build
> do repositório. As regras de negócio completas de Xtream, TMDB e sFy continuam sendo
> implementadas pelo agente seguindo a biblioteca de skills.

## Comandos iniciais

```powershell
python tools/bootstrap_artwork.py
python tools/validate_addons.py
python -m unittest discover -s tests -p "test_*.py" -v
python tools/build_repo.py
```

---

# Mega Biblioteca de Skills — sRepo / sTv / sFy

Este pacote é a base operacional para um agente de programação responsável por um monorepo Kodi local-first com três add-ons:

- `repository.srepo`: repositório Kodi e distribuição pelo GitHub Pages.
- `plugin.video.stv`: IPTV pessoal via API Xtream, com TV ao vivo, VOD, séries, favoritos, busca e continuar assistindo.
- `plugin.audio.sfy`: streaming de música usando a API Python do yt-dlp, com navegação inspirada em serviços de música, tops, categorias, playlists, favoritos e busca.

A pasta `.agents/skills` contém **100 skills executáveis como instruções de engenharia**. Ela não é o local do código de produção. O agente deve criar os add-ons em `addons/` conforme o blueprint deste pacote.

## Ordem de leitura do agente

1. `AGENTS.md`
2. `PROJECT_CONSTITUTION.md`
3. `ROADMAP_ARCHITECTURE.md`
4. `REPOSITORY_BLUEPRINT.md`
5. `SECURITY_AND_ENV_POLICY.md`
6. `SKILLS_INDEX.md`
7. `docs/ui/ARTWORK_CATALOG.md` quando a tarefa envolver interface ou scaffolding
8. A skill específica da tarefa

## Princípios centrais

- Tudo roda no dispositivo do usuário; não existe backend próprio obrigatório.
- sTv e sFy são add-ons separados e não importam código de produção um do outro.
- Cada add-on possui banco SQLite próprio.
- GitHub Pages publica apenas arquivos estáticos já gerados.
- `.env` nunca entra em ZIP, commit ou Pages.
- GitHub token nunca é usado pelo runtime dos add-ons.
- URLs de stream do yt-dlp são resolvidas no momento da reprodução e não persistidas como permanentes.
- TMDB enriquece metadados; não fornece mídia.
- Sincronização LAN, caso retomada, é manual, opcional e fase posterior; não bloqueia a V1.

## Conteúdo

- 100 skills em `.agents/skills/`.
- Arquitetura traduzida do roadmap.
- Blueprint de monorepo.
- Política de segredos e `.gitignore` blindado.
- ADRs iniciais.
- Templates para RFC, ADR, plano de mudança e release.
- Schemas SQLite de referência.
- Exemplos técnicos de padrões Kodi, SQLite, Xtream e yt-dlp.
- Mapa de referências oficiais.
- Pacote com 38 artes genéricas temporárias para ícones, fanarts e fallbacks.
- Manifesto de artwork com origem e destino exato de cada arquivo.

## Artes genéricas incluídas

O diretório `artwork/generic/` contém assets temporários para os três add-ons. Eles existem para permitir scaffolding, testes visuais e geração dos primeiros ZIPs sem imagens quebradas.

```text
artwork/generic/
├── repository.srepo/
│   ├── icon.png
│   └── fanart.jpg
├── plugin.video.stv/
│   ├── icon.png
│   ├── fanart.jpg
│   └── resources/media/
└── plugin.audio.sfy/
    ├── icon.png
    ├── fanart.jpg
    └── resources/media/
```

As artes devem ser copiadas para os caminhos reais indicados em `artwork/artwork-manifest.json`. Elas são deliberadamente identificadas como genéricas e podem ser substituídas depois, mantendo nomes, formatos e proporções compatíveis. Consulte `docs/ui/ARTWORK_CATALOG.md`.
