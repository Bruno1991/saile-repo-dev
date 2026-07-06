# ADR-0001 — Separar sRepo, sTv e sFy

## Status
Aceito

## Decisão
O sistema será composto por `repository.srepo`, `plugin.video.stv` e `plugin.audio.sfy`. Os plugins não importam código de produção um do outro.

## Consequências
Atualizações e falhas ficam isoladas. Pode existir pequena duplicação de utilitários, aceita para evitar acoplamento e problemas de empacotamento.
