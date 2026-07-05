---
name: sqlite-wal-concurrency
title: "WAL e Concorrência SQLite"
description: "Decide quando usar Write-Ahead Logging e como evitar problemas de arquivo."
domain: "sqlite"
triggers:
  - "WAL"
  - "journal_mode"
  - "concorrência SQLite"
  - "db-wal"
  - "db-shm"
---

# WAL e Concorrência SQLite

## Quando considerar WAL

WAL pode melhorar convivência entre leitores e um escritor, mas não elimina o modelo de escritor único. É útil quando existem leituras frequentes e escritas curtas.

## Habilitação

```sql
PRAGMA journal_mode = WAL;
```

O retorno deve ser verificado. Nem todo filesystem ou ambiente é adequado.

## Riscos

- arquivos `-wal` e `-shm` precisam de permissão;
- storage de rede pode ser inadequado;
- encerramento abrupto pode deixar WAL para recuperação;
- cópia do `.db` sem arquivos auxiliares durante atividade pode ser inconsistente;
- checkpoints podem causar picos.

## Regras Kodi

- banco no profile local do add-on;
- transações curtas;
- uma estratégia clara de escrita;
- não usar WAL como desculpa para concorrência descontrolada;
- fechar conexões no encerramento de serviço.

## Busy timeout

Use valor finito e trate falha. Timeout não corrige deadlock lógico nem transação esquecida.

## Checkpoint

Só implemente controle manual se houver necessidade medida. Caso contrário, deixe comportamento padrão e monitore tamanho.
