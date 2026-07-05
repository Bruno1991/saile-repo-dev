---
name: kodi-cache-database
title: "Cache e Banco Local no Kodi"
description: "Combina SQLite, TTL e sincronização sem travar a interface."
domain: "kodi"
triggers:
  - "cache Kodi"
  - "sincronizar conteúdo"
  - "SQLite addon"
  - "offline Kodi"
---

# Cache e Banco Local no Kodi

## Política por dado

- categorias: TTL médio;
- detalhes/metadata: TTL longo;
- URL de playback assinada: TTL curto ou sem persistência;
- favoritos/progresso: permanente e migrável;
- credenciais: settings, não cache.

## Fluxo de listagem

1. consultar cache;
2. se fresh, retornar;
3. se stale, poder mostrar e atualizar;
4. se ausente, buscar com progresso;
5. transformar fora da transação;
6. gravar lote curto;
7. retornar modelos.

## Atualização manual

A ação “Atualizar conteúdo” deve ser explícita, cancelável e não apagar dados válidos antes de obter novo snapshot.

## Evitar

- sync completo na home;
- download dentro de transação;
- apagar banco por qualquer exceção;
- cache compartilhado entre credenciais diferentes sem namespace;
- usar timestamp local ambíguo.

## Recuperação

Cache pode ser reconstruído após corrupção; dados de usuário não. Separe tabelas ou bancos se isso simplificar política de recuperação.
