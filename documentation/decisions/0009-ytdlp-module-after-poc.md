# ADR 0009 — Extração do yt-dlp condicionada

**Status:** aceito

## Decisão

Manter a integração inicialmente dentro do sFy. `script.module.saile.ytdlp` só será criado após prova técnica multiplataforma.

## Consequências

Evita modularização prematura e permite validar requisitos reais de runtime.
