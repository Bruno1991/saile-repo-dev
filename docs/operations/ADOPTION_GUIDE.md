# Guia de adoção

## Para adicionar ao projeto

1. Copie `.agents/`, `AGENTS.md`, `PROJECT_CONSTITUTION.md` e os documentos desejados para a raiz do monorepo.
2. Não copie `docs/roadmap/ROADMAP_ORIGINAL.png` para os ZIPs dos addons.
3. Renomeie apenas URLs/base owner do GitHub, sem alterar os IDs canônicos definidos.
4. Crie o código em `addons/`, nunca dentro de `.agents/`.
5. Use `.gitignore.template` como base e execute `git status --ignored` antes do primeiro commit.

## Prompt inicial sugerido para o agente

> Leia AGENTS.md, PROJECT_CONSTITUTION.md, ROADMAP_ARCHITECTURE.md, REPOSITORY_BLUEPRINT.md e SKILLS_INDEX.md. Inspecione o repositório real. Não implemente nada ainda. Entregue somente: diagnóstico do estado atual, divergências em relação ao blueprint, árvore alvo mínima, plano por fases e skills que serão ativadas. Não crie código dentro de .agents.

## Primeira fase recomendada

1. `repository.srepo` mínimo instalável.
2. `plugin.video.stv` com configuração, autenticação, sincronização e live.
3. VOD, séries, favoritos, busca e progresso.
4. TMDB com cache e matching seguro.
5. `plugin.audio.sfy` com home, busca e reprodução por yt-dlp.
6. Tops, categorias, playlists e favoritos sFy.
7. Pipeline de build, validação e Pages.
8. Sincronização LAN somente depois da V1 estável e mediante RFC/ADR.
