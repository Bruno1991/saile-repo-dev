---
name: sqlite-parameterization
title: "SQL Parametrizado e Consultas Seguras"
description: "Impede injeção e erros de escaping em todas as consultas."
domain: "sqlite"
triggers:
  - "SQL injection"
  - "query dinâmica"
  - "parâmetros SQL"
  - "filtro SQLite"
---

# SQL Parametrizado e Consultas Seguras

## Regra absoluta

Valores entram por placeholders, nunca por concatenação ou f-string.

```python
row = conn.execute(
    "SELECT * FROM media_item WHERE provider_id = ? AND media_id = ?",
    (provider_id, media_id),
).fetchone()
```

## IN dinâmico

Gere apenas placeholders, não valores:

```python
marks = ",".join("?" for _ in ids)
sql = f"SELECT * FROM media_item WHERE media_id IN ({marks})"
rows = conn.execute(sql, ids).fetchall()
```

Lista vazia deve ser tratada antes.

## Identificadores

Placeholders não representam nomes de tabela ou coluna. Identificadores dinâmicos devem vir de allowlist fixa:

```python
ORDER_COLUMNS = {"title": "title", "updated": "updated_at"}
column = ORDER_COLUMNS[user_choice]
```

## LIKE

Defina se `%` e `_` devem atuar como curingas. Quando a busca é literal, escape-os e declare `ESCAPE`.

## Logs

Não registre SQL com valores sensíveis interpolados. Registre nome lógico da consulta, duração e contagem.
