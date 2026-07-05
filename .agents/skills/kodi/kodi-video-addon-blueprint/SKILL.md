---
name: kodi-video-addon-blueprint
title: "Blueprint de Plugin de Vídeo"
description: "Fornece um plano completo para construir plugin de vídeo desde zero."
domain: "kodi"
triggers:
  - "construir plugin de vídeo"
  - "novo plugin Kodi"
  - "blueprint Kodi"
---

# Blueprint de Plugin de Vídeo

## Fase 1 — Contratos

Defina:

- ID e nome;
- versões Kodi alvo;
- fontes autorizadas;
- modelos `Category`, `VideoItem`, `PlaybackSource`;
- rotas públicas;
- política de cache;
- settings;
- critérios de playback.

## Fase 2 — Esqueleto

Crie:

- `addon.xml`;
- `main.py` fino;
- router;
- adaptador de listagem;
- provider interface;
- provider concreto;
- repositório SQLite;
- settings e idioma;
- logging.

## Fase 3 — Vertical slice

Implemente um fluxo completo pequeno:

```text
Home -> Categoria -> Lista -> Play
```

Não implemente dezenas de telas antes de provar playback.

## Fase 4 — Resiliência

- timeouts;
- erro de autenticação;
- cache stale;
- cancelamento;
- paginação;
- logs sanitizados.

## Fase 5 — Qualidade

- testes puros;
- migração;
- compatibilidade de dispositivo;
- empacotamento;
- instalação limpa;
- update via repositório.

## Entrega

Inclua documentação, licença, changelog, suporte e limitações conhecidas. O exemplo desta biblioteca é referência estrutural, não produto pronto para conteúdo real.
