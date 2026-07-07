# ADR 0011 — Sincronização LAN manual

**Status:** aceito

## Decisão

A sincronização é iniciada somente pelo usuário e troca registros sanitizados. Bancos SQLite, catálogos e credenciais não são compartilhados.

## Consequências

Mais segurança e consistência, com necessidade de protocolo de conflito e confirmação de dispositivos.
