---
name: kodi-xbmcvfs-special-paths
title: "xbmcvfs e special://"
description: "Manipula arquivos, diretórios e paths virtuais de maneira portátil."
domain: "kodi"
triggers:
  - "xbmcvfs"
  - "special://profile"
  - "filesystem Kodi"
  - "path Android"
---

# xbmcvfs e special://

## Paths importantes

- `special://home`: instalação/ambiente Kodi;
- `special://profile`: perfil do usuário;
- profile do add-on via `getAddonInfo("profile")`;
- path do add-on via `getAddonInfo("path")`.

## Tradução

Use `xbmcvfs.translatePath` quando biblioteca nativa como `sqlite3` precisa de caminho local.

## VFS

Para `smb://`, `nfs://`, `zip://` e outras fontes, prefira funções de `xbmcvfs`. `open()` não é universal.

## Criação de diretório

```python
profile = xbmcvfs.translatePath(addon.getAddonInfo("profile"))
if not xbmcvfs.exists(profile):
    xbmcvfs.mkdirs(profile)
```

## Dados imutáveis versus mutáveis

- assets e código: pasta do add-on;
- banco, cache e estado: profile;
- temporários: diretório apropriado e limpeza controlada.

## Atualização

Nunca escreva sobre arquivos da instalação para “salvar configuração”; atualizações podem substituir ou negar escrita.

## Compatibilidade

Teste separadores, Unicode e permissões em Windows e Android. Não concatene paths com `/` manualmente para paths locais.
