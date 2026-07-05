---
name: sqlite-schema-design
title: "Modelagem de Schema SQLite"
description: "Cria esquemas pequenos, coerentes, versionáveis e adequados ao domínio local."
domain: "sqlite"
triggers:
  - "criar banco"
  - "nova tabela"
  - "modelagem SQLite"
  - "schema"
---

# Modelagem de Schema SQLite

## Comece pelas consultas

Modele tabelas a partir de entidades e consultas reais. Liste:

- chaves de identidade;
- unicidade;
- relações;
- estados válidos;
- ordenações e filtros frequentes;
- dados descartáveis versus permanentes.

## Tipos e restrições

SQLite usa tipagem dinâmica, portanto restrições importam:

- `PRIMARY KEY` para identidade;
- `NOT NULL` quando ausência não faz sentido;
- `UNIQUE` para deduplicação verdadeira;
- `CHECK` para estados e faixas;
- `FOREIGN KEY` para relações reais;
- `STRICT` somente após confirmar compatibilidade da versão SQLite embarcada.

## Exemplo

```sql
CREATE TABLE media_item (
    provider_id TEXT NOT NULL,
    media_id TEXT NOT NULL,
    title TEXT NOT NULL,
    media_type TEXT NOT NULL CHECK (media_type IN ('movie','episode','channel')),
    updated_at INTEGER NOT NULL,
    PRIMARY KEY (provider_id, media_id)
);
```

## Chaves

Prefira IDs do domínio estáveis. Autoincremento não substitui unicidade externa. Use chave composta quando a identidade depende de provider + ID remoto.

## Datas

Escolha uma convenção única:

- epoch UTC em inteiro; ou
- ISO 8601 UTC em texto.

Não misture formatos na mesma coluna.

## Cache versus biblioteca

Cache pode ser reconstruído e ter TTL. Favoritos, perfis, progresso e preferências exigem mais cuidado, backup e migração.

## Revisão

Pergunte se cada coluna é necessária, se pode ficar nula e qual consulta justifica cada índice.
