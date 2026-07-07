# ADR-0005 — GitHub Pages como hospedagem estática

## Status
Aceito

## Decisão
O build gera ZIPs, `addons.xml`, checksum, hashes e índice HTML. GitHub Pages somente publica esses arquivos estáticos.

## Consequências
Nenhum código Python roda no Pages. Build e validação ocorrem localmente ou em Actions.
