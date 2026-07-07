# ADR 0006 — Sincronização LAN manual e adiada

## Status

Aceito; item de navegação presente, implementação funcional na V2.

## Decisão

sTv e sFy exibem `Sincronizar Dados`, mas nenhuma sincronização ocorre sem ação do usuário. A futura implementação troca registros e nunca compartilha o arquivo SQLite.
