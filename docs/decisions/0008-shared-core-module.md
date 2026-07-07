# ADR 0008 — Módulo Python compartilhado

**Status:** aceito

## Decisão

Criar `script.module.saile.core` para infraestrutura estável. Regras de Xtream, TMDB, sFy e navegação permanecem nos plugins.

## Consequências

Reduz duplicação sem acoplar domínios. Mudanças no core exigem compatibilidade semântica.
