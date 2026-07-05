---
name: python-concurrency-cancellation
title: "Concorrência, Threads e Cancelamento"
description: "Evita bloqueios, corridas e operações que ignoram cancelamento do usuário."
domain: "python"
triggers:
  - "thread"
  - "concorrência"
  - "background"
  - "progresso"
  - "cancelamento"
---

# Concorrência, Threads e Cancelamento

## Princípio

Concorrência só deve ser adicionada quando existe benefício mensurável e contrato de cancelamento.

## Kodi

- não manipule GUI arbitrariamente de threads secundárias;
- use `xbmc.Monitor().abortRequested()` em serviços e loops;
- em diálogos de progresso, cheque cancelamento entre lotes;
- não deixe threads não-daemon impedirem encerramento;
- não compartilhe conexão SQLite entre threads sem desenho explícito.

## Estratégias

- I/O independente: pool pequeno de workers;
- escrita SQLite: fila ou serialização curta;
- atualização de UI: thread principal/adaptador apropriado;
- tarefas longas: lotes e checkpoints.

## Erros

Colete exceções dos workers. Uma thread que falha silenciosamente produz estado parcial difícil de diagnosticar.

## Cancelamento cooperativo

```python
def sync_items(items, monitor):
    for batch in batched(items, 100):
        if monitor.abortRequested():
            raise OperationCancelled()
        process_batch(batch)
```

## Evitar

- thread por item;
- sleeps longos sem checar monitor;
- lock mantido durante rede;
- transação SQLite cobrindo download inteiro;
- executor global criado em import.
