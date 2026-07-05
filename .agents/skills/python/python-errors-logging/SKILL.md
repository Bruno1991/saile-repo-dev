---
name: python-errors-logging
title: "Erros, Exceções e Logging"
description: "Cria uma taxonomia de erros e logs úteis sem expor dados sensíveis."
domain: "python"
triggers:
  - "tratamento de erro"
  - "logging"
  - "traceback"
  - "mensagens ao usuário"
---

# Erros, Exceções e Logging

## Taxonomia recomendada

```python
class SaileError(Exception):
    """Base para falhas esperadas do domínio."""

class ConfigurationError(SaileError):
    pass

class ProviderError(SaileError):
    pass

class PersistenceError(SaileError):
    pass

class PlaybackError(SaileError):
    pass
```

## Onde capturar

- capture perto da fronteira capaz de tomar uma decisão;
- preserve causa com `raise ... from exc`;
- no entry point, converta erro conhecido em mensagem amigável;
- erro inesperado deve gerar traceback no log e mensagem genérica ao usuário.

## Evitar

```python
try:
    ...
except Exception:
    return []
```

Isso transforma falha de autenticação, JSON inválido e bug de código em “lista vazia”.

## Logging Kodi

Centralize um adaptador que use `xbmc.log`. Níveis:

- DEBUG: IDs, contagens e duração;
- INFO: início/fim de operação relevante;
- WARNING: fallback ou dado incompleto;
- ERROR: operação falhou;
- FATAL: inicialização impossível.

## Sanitização

Antes de registrar URLs, remova senha, token, cookies e query strings sensíveis.

## Mensagens de UI

A mensagem deve orientar ação: “Configure servidor, usuário e senha” é melhor que “Erro 401”. O detalhe técnico permanece no log.
