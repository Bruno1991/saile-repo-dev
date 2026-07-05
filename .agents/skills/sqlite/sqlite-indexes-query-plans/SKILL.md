---
name: sqlite-indexes-query-plans
title: "Índices e Planos de Consulta"
description: "Otimiza com base em consultas reais e EXPLAIN QUERY PLAN."
domain: "sqlite"
triggers:
  - "índice SQLite"
  - "consulta lenta"
  - "EXPLAIN QUERY PLAN"
  - "performance SQL"
---

# Índices e Planos de Consulta

## Princípio

Índice não é decoração. Cada índice aumenta armazenamento e custo de escrita.

## Processo

1. capture consulta e parâmetros típicos;
2. meça duração e cardinalidade;
3. use `EXPLAIN QUERY PLAN`;
4. crie índice alinhado a filtros, joins e ordenação;
5. meça novamente;
6. remova índices redundantes.

## Ordem das colunas

Em índice composto, considere igualdade primeiro, depois faixa/ordenação, conforme consultas reais.

```sql
CREATE INDEX idx_streams_category_name
ON streams(category_id, name COLLATE NOCASE);
```

## Índice cobridor

Pode evitar leitura da tabela, mas só use quando o ganho justifica tamanho e manutenção.

## Prefixos redundantes

Se existe `(provider_id, category_id, name)`, um índice separado apenas em `provider_id` pode ser redundante, dependendo das consultas.

## Estatísticas

`ANALYZE` pode ajudar o planner. Não execute indiscriminadamente em toda abertura.

## Sinais de problema

- `SCAN` em tabela grande para consulta frequente;
- ordenação temporária repetida;
- função aplicada à coluna indexada;
- `LIKE '%termo%'` esperando usar índice B-tree;
- conversão de tipo impedindo busca eficiente.
