# ADR-0002 — Local-first sem backend obrigatório

## Status
Aceito

## Decisão
Toda lógica, cache e estado do usuário rodam no dispositivo Kodi. APIs externas são chamadas diretamente pelos addons conforme configuração.

## Consequências
Não é possível manter segredos de aplicação verdadeiramente secretos no cliente distribuído. O projeto aceita modo degradado e credenciais dedicadas.
