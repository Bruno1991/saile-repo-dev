---
name: kodi-directory-listings
title: "Diretórios e Listagens Kodi"
description: "Monta listagens corretas com addDirectoryItems, content type, ordenação e finalização."
domain: "kodi"
triggers:
  - "addDirectoryItem"
  - "endOfDirectory"
  - "lista Kodi"
  - "menu Kodi"
---

# Diretórios e Listagens Kodi

## Sequência correta

1. definir categoria e content type;
2. construir itens;
3. adicionar em lote quando possível;
4. configurar ordenação;
5. finalizar diretório.

```python
xbmcplugin.setPluginCategory(handle, "Filmes")
xbmcplugin.setContent(handle, "movies")
xbmcplugin.addDirectoryItems(handle, items, totalItems=len(items))
xbmcplugin.endOfDirectory(handle, succeeded=True)
```

## `isFolder`

- `True`: navegar para outra rota/listagem;
- `False`: item final, ação ou mídia reproduzível.

Não confunda `ListItem.setIsFolder` com o argumento de `addDirectoryItem`; mantenha ambos coerentes quando usados.

## Content type

Use o tipo mais específico: `movies`, `tvshows`, `episodes`, `songs`, `videos`. Isso influencia skins e exibição.

## Falhas

Se a listagem falha antes de concluir, chame `endOfDirectory(..., succeeded=False)` quando apropriado e informe o usuário sem esconder o erro.

## Listas grandes

- prefira `addDirectoryItems`;
- informe `totalItems`;
- pagine;
- evite centenas de chamadas de rede por tela;
- não faça download de imagens manualmente apenas para listar.

## Cache da listagem

Controle `cacheToDisc` conforme volatilidade. Não desative sem motivo e não dependa dele como cache de domínio.
