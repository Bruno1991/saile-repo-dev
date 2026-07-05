---
name: sqlite-kodi-integration
title: "Integração SQLite em Add-ons Kodi"
description: "Aplica SQLite de forma segura dentro do ciclo de vida e filesystem do Kodi."
domain: "sqlite"
triggers:
  - "SQLite no Kodi"
  - "profile database"
  - "cache do addon"
  - "xbmcvfs database"
---

# Integração SQLite em Add-ons Kodi

## Local do banco

Armazene no profile do add-on:

```python
addon = xbmcaddon.Addon()
profile = xbmcvfs.translatePath(addon.getAddonInfo("profile"))
```

Crie o diretório com API adequada antes de conectar.

## Não usar banco interno do Kodi

O add-on deve manter seu próprio banco. Alterar diretamente `MyVideos`, `Textures` ou outros bancos internos cria dependência de versão e risco de corrupção.

## Inicialização

- criar diretório;
- abrir conexão;
- aplicar PRAGMAs;
- executar migrações rápidas;
- fechar.

Migrações pesadas devem apresentar progresso e suportar falha segura.

## Threads

Cada thread deve possuir sua conexão ou utilizar uma camada de escrita serializada. Não contorne `check_same_thread` sem entender sincronização.

## Desinstalação/atualização

O profile pode sobreviver à atualização. Portanto, nunca dependa apenas da versão do código para inferir schema; leia versão do banco.

## Logs e suporte

Registre versão de schema, path lógico mascarado, duração e erros. Não envie banco do usuário para suporte sem consentimento.
