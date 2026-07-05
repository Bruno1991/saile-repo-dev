---
name: code-review
title: "Revisão de Código Orientada a Risco"
description: "Fornece uma rotina de revisão para Python, SQLite e Kodi."
domain: "core"
triggers:
  - "revisar código"
  - "auditoria"
  - "pull request"
  - "antes de publicar"
---

# Revisão de Código Orientada a Risco

## Ordem da revisão

1. Correção funcional.
2. Segurança e privacidade.
3. Integridade de dados.
4. Compatibilidade Kodi/plataformas.
5. Desempenho.
6. Manutenibilidade.
7. Estilo.

## Checklist Python

- exceções específicas;
- timeouts de rede;
- fechamento de recursos;
- tipos coerentes;
- ausência de estado global mutável desnecessário;
- funções com uma responsabilidade;
- imports compatíveis com o runtime do Kodi.

## Checklist SQLite

- placeholders em parâmetros;
- transações explícitas para múltiplas escritas;
- foreign keys habilitadas quando usadas;
- índices justificáveis por consultas reais;
- migração idempotente;
- tratamento de corrupção ou banco incompatível;
- nenhuma conexão mantida aberta durante rede/UI.

## Checklist Kodi

- `addon.xml` consistente;
- content type correto;
- `ListItem` com art e metadata adequados;
- diretórios finalizados;
- playback resolvido corretamente;
- uso de `xbmcvfs`/`special://`;
- settings localizados;
- logs via `xbmc.log`;
- ausência de operações longas no thread da UI sem feedback.

## Severidade

- **bloqueador**: perda de dados, segredo exposto, add-on não inicia;
- **alta**: fluxo principal quebrado, incompatibilidade ampla;
- **média**: regressão localizada, tratamento insuficiente;
- **baixa**: clareza, estilo, otimização não crítica.

## Formato do parecer

Cada achado deve indicar arquivo, trecho, impacto e correção recomendada. Evite comentários vagos como “melhorar arquitetura”.
