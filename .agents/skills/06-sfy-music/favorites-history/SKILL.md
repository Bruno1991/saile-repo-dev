---
name: favorites-history
title: Playlists e histórico sFy
skill_id: 06.07
category: sfy
version: 2.0.0
applies_to:
  - plugin.audio.sfy
---

# Playlists e histórico sFy

## Missão

Persistir músicas em **Minhas Playlists** e registrar reproduções recentes com limites de retenção. O sFy não possui atalho ou domínio fixo de Favoritos.

## Procedimento obrigatório

1. Identificar faixas por origem e ID estáveis.
2. Criar playlists locais com nome, ordem e timestamps.
3. Evitar duplicação acidental dentro da mesma playlist.
4. Registrar histórico sem armazenar URL temporária.
5. Limitar retenção do histórico sem remover playlists.
6. Sincronizar playlists apenas por ação manual do usuário.

## Critérios de aceitação

- [ ] Nenhum item fixo chamado Favoritos foi adicionado ao sFy.
- [ ] A home continua Buscar, Minhas Playlists e Sincronizar Dados.
- [ ] URLs temporárias não são persistidas.
- [ ] Migrações preservam playlists existentes.
