# ADR-0003 — Um SQLite por plugin

## Status
Aceito

## Decisão
sTv e sFy mantêm bancos independentes em seus perfis. Nenhum arquivo SQLite é compartilhado entre processos/dispositivos.

## Consequências
A sincronização futura troca registros por protocolo/export, não o arquivo do banco.
