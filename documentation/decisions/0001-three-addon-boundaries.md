# ADR 0001 — Separar repositório e plugins

## Status

Superado em parte pelos ADRs 0007 e 0008.

## Decisão original

Separar `repository.srepo`, `plugin.video.stv` e `plugin.audio.sfy`, impedindo importação direta entre os plugins.

## Evolução

A separação permanece, mas o ecossistema agora inclui `resource.images.saile` e `script.module.saile.core` como dependências compartilhadas explícitas e versionadas.
