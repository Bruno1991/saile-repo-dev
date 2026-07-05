---
name: sqlite-fts-json
title: "FTS5 e JSON no SQLite"
description: "Usa recursos avançados somente com detecção e fallback."
domain: "sqlite"
triggers:
  - "FTS5"
  - "JSON1"
  - "busca textual"
  - "JSON SQLite"
---

# FTS5 e JSON no SQLite

## Detecção

A versão e as opções compiladas do SQLite variam por plataforma. Antes de depender de FTS5 ou funções JSON, execute teste de capacidade e forneça fallback.

## FTS5

Adequado para busca textual por título, elenco, descrição ou termos normalizados. Planeje:

- tabela virtual;
- sincronização com tabela principal;
- tokenizer e acentos;
- rebuild após migração;
- fallback com LIKE para bases pequenas.

## JSON

JSON em coluna é útil para campos raros ou payload preservado, mas não substitui modelagem de dados usados em filtros e joins.

## Regra

Campos consultados frequentemente devem ser colunas normais com tipos e índices claros.

## Compatibilidade

Não assuma que extensão carregável está habilitada. Em ambientes Kodi, carregar extensões nativas pode ser impossível ou inseguro.

## Testes

Teste ausência do recurso, dados malformados e migração de formato.
