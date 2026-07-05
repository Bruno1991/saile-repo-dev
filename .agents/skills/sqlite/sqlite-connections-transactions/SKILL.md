---
name: sqlite-connections-transactions
title: "Conexões e Transações SQLite"
description: "Controla ciclo de vida, atomicidade, locks e fechamento de conexões."
domain: "sqlite"
triggers:
  - "sqlite3.connect"
  - "transação"
  - "commit"
  - "rollback"
  - "database is locked"
---

# Conexões e Transações SQLite

## Ciclo de vida

Abra conexões por operação ou unidade de trabalho curta. Não mantenha conexão global atravessando UI, rede ou longos períodos de inatividade.

## Configuração inicial

Após conectar, configure de forma explícita conforme a política do projeto:

```python
conn.execute("PRAGMA foreign_keys = ON")
conn.execute("PRAGMA busy_timeout = 5000")
```

Confirme o efeito de cada PRAGMA na versão embarcada.

## Transações

Agrupe múltiplas escritas relacionadas:

```python
with sqlite3.connect(path) as conn:
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executemany(SQL, rows)
```

O contexto confirma em sucesso e reverte em exceção, respeitando o comportamento do módulo e a configuração de autocommit da versão de Python utilizada.

## Regras

- não fazer HTTP dentro de transação;
- não abrir diálogo enquanto mantém lock;
- usar `executemany` para lotes;
- evitar commit por linha;
- sempre fechar cursores/conexões;
- não compartilhar a mesma conexão entre threads por conveniência.

## Locking

Ao receber `database is locked`, investigue:

- transação longa;
- conexão esquecida;
- escrita concorrente;
- arquivo em storage inadequado;
- WAL/SHM sem permissão;
- antivírus ou sync externo interferindo.

Não resolva apenas aumentando timeout indefinidamente.
