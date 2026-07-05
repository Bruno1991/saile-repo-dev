---
name: fix-kodi-bug
title: "Workflow: Corrigir Bug no Kodi"
description: "Reproduz, localiza e corrige defeitos em roteamento, UI, banco, rede ou playback."
domain: "workflows"
triggers:
  - "corrigir bug Kodi"
  - "traceback Kodi"
  - "menu vazio"
  - "playback falha"
---

# Workflow: Corrigir Bug no Kodi

## Procedimento

1. obter passos exatos e log;
2. identificar versão/plataforma;
3. reproduzir com menor caso;
4. classificar camada da falha;
5. adicionar instrumentação sanitizada;
6. confirmar hipótese;
7. implementar menor correção;
8. adicionar teste de regressão;
9. testar fluxo adjacente;
10. remover logs temporários excessivos.

## Árvores rápidas

### Menu vazio

- action correta?
- provider retornou dados?
- cache filtrou tudo?
- `addDirectoryItems` recebeu itens?
- `endOfDirectory` foi chamado?

### Playback não inicia

- item tem `IsPlayable`?
- rota play foi chamada?
- URL foi resolvida?
- `ListItem(path=...)` correto?
- `setResolvedUrl` sucesso/falha?
- player suporta protocolo/codec?

### DB locked

- transação longa?
- conexão global?
- thread concorrente?
- WAL/permissão?

## Entrega

Causa raiz e evidência são obrigatórias.
