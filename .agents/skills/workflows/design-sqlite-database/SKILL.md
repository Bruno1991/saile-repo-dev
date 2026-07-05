---
name: design-sqlite-database
title: "Workflow: Projetar Banco SQLite"
description: "Vai de requisitos e consultas a schema, migração, índices e testes."
domain: "workflows"
triggers:
  - "projetar SQLite"
  - "novo banco"
  - "novo schema"
  - "persistência local"
---

# Workflow: Projetar Banco SQLite

## Etapas

1. classificar dados em cache, permanentes e sensíveis;
2. listar entidades e identidades;
3. listar consultas e ordenações;
4. desenhar tabelas e constraints;
5. escolher formato de tempo;
6. definir versionamento;
7. criar migração inicial;
8. criar repositories parametrizados;
9. analisar índices;
10. testar criação, upgrade, rollback e corrupção.

## Artefatos

- diagrama textual;
- DDL;
- mapa de queries;
- política de transação;
- política de backup;
- plano de migração;
- testes.

## Gate

Nenhuma tabela entra sem identidade e política de atualização. Nenhum índice entra sem consulta que o justifique.
