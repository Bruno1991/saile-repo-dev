# ADR-0003 — SQLite Storage

**Status:** Proposed

## Decisão

SQLite é o banco local de estado e cache indexado. O projeto usa repositórios, migrações e transações explícitas.

## Consequências

Baixa dependência e boa portabilidade; exige verificar recursos no runtime e proteger contra corrupção/desligamento.
