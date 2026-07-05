# ADR-0001 — Local-First Runtime

**Status:** Proposed

## Contexto

O SAILE deve rodar no dispositivo do usuário sem backend próprio obrigatório.

## Decisão

Estado e execução principais são locais. Serviços remotos são providers substituíveis configurados pelo usuário.

## Consequências

Melhora privacidade e independência, mas exige cuidado com recursos limitados, migrações locais, compatibilidade e recuperação.
