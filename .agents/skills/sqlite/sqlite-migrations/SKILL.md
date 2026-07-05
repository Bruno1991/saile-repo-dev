---
name: sqlite-migrations
title: "Migrações de Schema SQLite"
description: "Evolui o banco sem perder dados nem depender de recriação silenciosa."
domain: "sqlite"
triggers:
  - "migração"
  - "schema version"
  - "ALTER TABLE"
  - "atualizar banco"
---

# Migrações de Schema SQLite

## Fonte da versão

Use `PRAGMA user_version` ou tabela de migrações, mas não ambos sem necessidade. Cada migração deve ter número, objetivo e operação idempotente controlada.

## Fluxo

1. abrir conexão exclusiva para migração;
2. ler versão atual;
3. validar versão suportada;
4. executar migrações em ordem;
5. atualizar versão somente após sucesso;
6. revalidar schema;
7. registrar resultado sanitizado.

## Exemplo

```python
def migrate(conn):
    version = conn.execute("PRAGMA user_version").fetchone()[0]
    if version < 1:
        conn.executescript(SCHEMA_V1)
        conn.execute("PRAGMA user_version = 1")
    if version < 2:
        conn.execute("ALTER TABLE media_item ADD COLUMN plot TEXT")
        conn.execute("PRAGMA user_version = 2")
```

A implementação real deve executar dentro de transação apropriada e lidar com DDL compatível.

## Migração destrutiva

Para alterar coluna ou constraint:

1. criar nova tabela;
2. copiar dados com transformação explícita;
3. validar contagens;
4. remover tabela antiga;
5. renomear nova;
6. recriar índices e triggers.

## Cache descartável

Se o banco contém somente cache, pode haver estratégia de reconstrução. Isso deve ser explícito e jamais aplicado a favoritos ou progresso.

## Testes

Teste banco vazio, cada versão anterior suportada, interrupção e dados inválidos.
