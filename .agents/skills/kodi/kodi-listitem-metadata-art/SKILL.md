---
name: kodi-listitem-metadata-art
title: "ListItem, Metadata e Arte"
description: "Preenche itens com metadados e imagens compatíveis com skins e versões Kodi."
domain: "kodi"
triggers:
  - "ListItem"
  - "setArt"
  - "metadata Kodi"
  - "InfoTagVideo"
  - "poster fanart"
---

# ListItem, Metadata e Arte

## Construção

```python
item = xbmcgui.ListItem(label=video.title, offscreen=True)
item.setArt({
    "thumb": video.thumb,
    "poster": video.poster,
    "fanart": video.fanart,
})
```

Confirme `offscreen` na versão-alvo.

## Metadata

APIs de metadata evoluem entre versões. Prefira a API recomendada na documentação da versão-alvo, como `getVideoInfoTag()`/`InfoTagVideo` quando disponível, em vez de depender indefinidamente de métodos depreciados.

## Campos úteis

- título e título original;
- plot;
- ano;
- duração em segundos;
- gênero;
- temporada e episódio;
- rating e votos;
- IDs externos;
- data de estreia;
- playcount/progresso quando aplicável.

## Arte

Use caminhos/URLs válidos e chaves conhecidas: `icon`, `thumb`, `poster`, `fanart`, `banner`, `landscape`, `clearlogo`.

## IsPlayable

Para itens reproduzíveis:

```python
item.setProperty("IsPlayable", "true")
```

A URL do item pode apontar para a rota `play`, não necessariamente para mídia direta.

## Segurança

Não inclua credenciais em labels, propriedades ou URLs visíveis. Normalize metadata externa e limite tamanhos excessivos.
