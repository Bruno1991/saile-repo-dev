---
name: audit-existing-addon
title: "Workflow: Auditar Add-on Existente"
description: "Executa auditoria técnica completa antes de continuar desenvolvimento."
domain: "workflows"
triggers:
  - "auditar addon"
  - "analisar dump"
  - "avaliar projeto Kodi"
  - "o que falta"
---

# Workflow: Auditar Add-on Existente

## Escopo da auditoria

### Estrutura

- manifesto, entry point, módulos, assets, settings, idioma;
- arquivos gerados versus fonte;
- duplicações e legados.

### Arquitetura

- separação UI/provider/DB;
- roteamento;
- tratamento de erro;
- dependências e globals.

### SQLite

- schema, migração, índices, locks, cache;
- dados descartáveis versus permanentes.

### Kodi

- APIs usadas;
- finalização de diretórios;
- metadata;
- playback;
- paths;
- compatibilidade.

### Segurança

- segredos;
- URLs autenticadas;
- TLS;
- logs;
- conteúdo autorizado;
- dependências.

### Build

- ZIP;
- versões;
- repositório;
- hashes;
- `.gitignore`.

## Resultado

Produza achados por severidade, evidência por arquivo, ordem recomendada de correção e uma rota para MVP testável. Não reescreva o projeto durante a auditoria.
