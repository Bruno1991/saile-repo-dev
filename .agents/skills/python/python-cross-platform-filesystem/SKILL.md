---
name: python-cross-platform-filesystem
title: "Filesystem Multiplataforma"
description: "Garante paths seguros em Windows, Linux, Android e VFS do Kodi."
domain: "python"
triggers:
  - "path"
  - "arquivo"
  - "Android"
  - "Windows"
  - "xbmcvfs"
  - "special://"
---

# Filesystem Multiplataforma

## Regra

Dentro do Kodi, diferencie:

- caminho do sistema operacional;
- URI `special://`;
- caminho VFS como `smb://`, `nfs://` ou `zip://`.

Nem todo path VFS funciona com `open()` ou `pathlib`.

## Uso recomendado

- `xbmcvfs.translatePath` quando uma API nativa precisa de path local;
- `xbmcvfs.File`, `exists`, `mkdirs`, `copy`, `delete` para VFS;
- `os.path`/`pathlib` somente para paths locais traduzidos e testados.

## Dados do usuário

Use o profile do add-on, não a pasta de instalação, para:

- SQLite;
- cache próprio;
- configurações auxiliares;
- downloads temporários.

A pasta do add-on pode ser somente leitura.

## Escrita atômica

Para arquivos críticos:

1. escrever em temporário no mesmo volume;
2. flush/fechar;
3. substituir destino;
4. preservar backup quando necessário.

## Segurança

Normalize nomes, rejeite `..`, separadores inesperados e paths absolutos quando a entrada representa apenas um nome.

## Testes

Teste nomes Unicode, espaços, paths longos e ausência de permissão.
