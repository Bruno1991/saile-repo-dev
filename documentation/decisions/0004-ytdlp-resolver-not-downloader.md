# ADR-0004 — yt-dlp como resolvedor de streaming

## Status
Aceito

## Decisão
O caminho principal do sFy usa a API Python do yt-dlp para descobrir formatos e resolver URL temporária de áudio. Download persistente não é comportamento padrão.

## Consequências
URLs precisam ser resolvidas perto da reprodução e não podem ser tratadas como permanentes.
