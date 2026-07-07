# Prova técnica obrigatória do yt-dlp

Antes de criar `script.module.saile.ytdlp` ou concluir a UI do sFy, validar o fluxo mínimo:

```text
Buscar → selecionar resultado → resolver áudio → entregar URL ao Kodi → reproduzir → cancelar/encerrar limpo
```

## Plataformas

- Windows + Kodi
- Linux + Kodi
- Android TV + Kodi
- Fire TV/Firestick + Kodi

## Critérios

- nenhuma mídia baixada permanentemente por padrão;
- URL resolvida no momento da reprodução e não persistida;
- headers necessários entregues ao player;
- timeout e cancelamento funcionais;
- nenhum cookie/token em log;
- ausência de processo/thread órfão;
- mensagem clara quando a capacidade não estiver disponível.

Somente após aprovação da matriz, registrar ADR para extrair o módulo independente.
