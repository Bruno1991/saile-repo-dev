---
name: stv-navigation-contract
title: Contrato de navegação sTv
skill_id: 05.11
category: stv
version: 2.0.0
applies_to:
  - repository.srepo
  - resource.images.saile
  - script.module.saile.core
  - plugin.video.stv
  - plugin.audio.sfy
---

# Contrato de navegação sTv

## Missão

Preservar a home e a ordem fixa Buscar/Favoritos em cada seção do sTv.

## Procedimento obrigatório

1. Ler `PROJECT_CONSTITUTION.md`, `docs/architecture/ECOSYSTEM_MODULES.md` e os ADRs relacionados.
2. Inspecionar o código real antes de alterar a estrutura.
3. Preservar IDs canônicos, ordem de navegação e fronteiras de responsabilidade.
4. Tratar sincronização LAN como fluxo manual e opcional.
5. Atualizar testes e documentação na mesma alteração.
6. Executar `python tools/validate_addons.py` e os testes unitários.

## Critérios de aceitação

- [ ] Nenhuma regra de negócio foi movida para o core compartilhado.
- [ ] As artes fixas são resolvidas por `resource.images.saile`.
- [ ] A ordem de navegação canônica permanece coberta por teste.
- [ ] Nenhum arquivo SQLite é compartilhado diretamente pela rede.
- [ ] Nenhum segredo entrou em ZIP, log ou documentação de exemplo.

## Anti-padrões

- Duplicar ícones fixos dentro de sTv e sFy.
- Reordenar menus por ordem alfabética.
- Sincronizar automaticamente ao abrir o add-on.
- Criar dependência circular entre plugins e módulos.
- Colocar Xtream, TMDB ou yt-dlp como regra de negócio no core.
