# ADR 0007 — Recurso de artwork compartilhado

**Status:** aceito

## Decisão

Criar `resource.images.saile` para nove ícones fixos usados por sTv e sFy. Cada plugin mantém apenas sua identidade própria e imagens dinâmicas de conteúdo.

## Consequências

Menos duplicação, atualização visual independente e dependência explícita. Falta de asset passa a ser erro de build.
