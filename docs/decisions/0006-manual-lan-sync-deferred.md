# ADR-0006 — Sincronização LAN manual e adiada

## Status
Aceito como direção futura

## Decisão
A V1 não depende de sincronização LAN. Se implementada, será iniciada manualmente pelo usuário, por addon, com troca de registros e resolução de conflitos.

## Consequências
Nunca montar/abrir o mesmo SQLite simultaneamente por rede.
