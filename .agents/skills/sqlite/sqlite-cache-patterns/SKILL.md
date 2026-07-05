---
name: sqlite-cache-patterns
title: "Padrões de Cache com SQLite"
description: "Implementa TTL, invalidação e identidade de cache sem mascarar erros."
domain: "sqlite"
triggers:
  - "cache SQLite"
  - "TTL"
  - "offline"
  - "sincronização de catálogo"
---

# Padrões de Cache com SQLite

## Modelo

Um cache útil registra:

- chave estável;
- payload normalizado ou colunas consultáveis;
- instante de atualização;
- validade/TTL;
- identidade do provider/usuário;
- versão do formato.

## Fresh, stale, missing

Diferencie três estados:

- **fresh**: pode servir diretamente;
- **stale**: pode servir como fallback com aviso e tentar atualizar;
- **missing**: precisa buscar ou informar indisponibilidade.

## Não cachear como sucesso

Erro de rede, 401 ou JSON inválido não deve substituir cache válido por lista vazia.

## Invalidação

Eventos comuns:

- mudança de credenciais;
- mudança de servidor/provider;
- nova versão de schema;
- ação manual de atualizar;
- expiração por categoria de dado.

## Escrita

Baixe e transforme fora da transação. Grave em lote curto. Para snapshot completo, considere tabela temporária ou versão de geração para evitar estado parcialmente atualizado.

## Limpeza

Remova entradas antigas por política limitada. Não faça `VACUUM` frequente durante uso normal.
