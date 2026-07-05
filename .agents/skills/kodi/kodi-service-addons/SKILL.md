---
name: kodi-service-addons
title: "Serviços e Tarefas em Background"
description: "Implementa loops de serviço respeitando encerramento, energia e recursos."
domain: "kodi"
triggers:
  - "service addon"
  - "background Kodi"
  - "xbmc.Monitor"
  - "tarefa periódica"
---

# Serviços e Tarefas em Background

## Quando usar

Serviço é apropriado para tarefa contínua ou periódica realmente necessária. Não use serviço apenas para evitar projetar refresh sob demanda.

## Loop correto

```python
monitor = xbmc.Monitor()
while not monitor.abortRequested():
    run_due_tasks()
    if monitor.waitForAbort(60):
        break
```

`waitForAbort` permite encerramento rápido, ao contrário de `time.sleep` longo.

## Regras

- startup leve;
- nenhuma UI bloqueante;
- conexões e threads fechadas;
- backoff em falhas;
- limites de CPU/rede;
- não repetir sync completo a cada minuto;
- respeitar configuração do usuário.

## Coordenação

Se plugin e serviço usam o mesmo SQLite, mantenha transações curtas e protocolo de migração único. Não migre simultaneamente.

## Logs

Evite poluir log em cada iteração. Registre mudanças de estado, falhas e métricas resumidas.

## Desativação

O serviço deve funcionar com add-on desabilitado/atualizado sem deixar processos externos órfãos.
