---
name: kodi-debugging-logs
title: "Logs e Depuração no Kodi"
description: "Cria diagnósticos úteis em dispositivos reais sem vazar dados."
domain: "kodi"
triggers:
  - "kodi.log"
  - "debug Kodi"
  - "traceback addon"
  - "suporte"
---

# Logs e Depuração no Kodi

## Adaptador de log

Centralize prefixo, nível e sanitização:

```python
def log(message: str, level=xbmc.LOGINFO) -> None:
    xbmc.log(f"[plugin.video.exemplo] {message}", level)
```

## O que registrar

- versão do add-on;
- action e IDs não sensíveis;
- início/fim de sync;
- contagens;
- duração;
- status HTTP sem corpo sensível;
- versão de schema;
- traceback inesperado.

## O que não registrar

- senha;
- token;
- cookie;
- URL assinada completa;
- payload pessoal;
- listas enormes.

## Diagnóstico por camada

- router: action e parâmetros validados;
- provider: endpoint lógico e resultado;
- persistence: operação e quantidade;
- presentation: quantidade de itens;
- playback: fase de resolução, não segredo.

## Modo debug

Pode aumentar detalhe, mas continua sanitizado. Nunca condicione segurança ao modo debug.

## Relatório de suporte

Inclua instruções para obter log, versão, plataforma e passos de reprodução. Não peça banco ou credenciais por padrão.
