---
name: kodi-testing-release
title: "Testes e Release Kodi"
description: "Define matriz de testes e gate de publicação."
domain: "kodi"
triggers:
  - "testar addon Kodi"
  - "release Kodi"
  - "QA addon"
  - "antes de publicar"
---

# Testes e Release Kodi

## Testes automatizados

- router e URL builder;
- parsers de provider;
- cache/TTL;
- schema/migrações;
- sanitização;
- modelos de domínio;
- build e validação XML/ZIP.

## Testes manuais

### Instalação

- ZIP em perfil limpo;
- dependências resolvidas;
- settings abrem;
- ícone/fanart aparecem.

### Navegação

- home;
- pastas vazias;
- paginação;
- back navigation;
- erro de rede;
- credencial inválida.

### Playback

- mídia direta;
- URL expirada;
- cancelamento;
- retorno após player;
- headers/manifest quando usados.

### Persistência

- primeira execução;
- upgrade de versão anterior;
- cache expirado;
- banco bloqueado/corrompido simulado;
- preservação de favoritos/progresso.

## Matriz

Teste pelo menos desktop + dispositivo alvo principal, com cache frio/quente e rede lenta/interrompida.

## Gate

Não publicar com traceback conhecido no fluxo principal, segredo em artefato, versão divergente ou ZIP não instalável.
