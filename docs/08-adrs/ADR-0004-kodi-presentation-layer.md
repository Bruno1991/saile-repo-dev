# ADR-0004 — Kodi as Presentation Layer

**Status:** Proposed

## Decisão

APIs Kodi ficam na fronteira de apresentação/gateway. Domínio e providers permanecem independentes.

## Consequências

Facilita testes e evolução, mas exige tradução explícita de modelos para `ListItem`, dialogs e player.
