# Catálogo de artwork genérico

## Objetivo

Garantir que a primeira versão instalável dos add-ons nunca apresente imagem quebrada, campo vazio ou dependência de arte externa. As imagens deste pacote são genéricas e temporárias: o agente deve utilizá-las como fallback até que as artes finais sejam fornecidas.

## Dimensões de referência

| Tipo | Formato do pacote | Proporção | Uso |
|---|---:|---:|---|
| Ícone do add-on | 512 × 512 PNG | 1:1 | `addon.xml`, lista de add-ons e home |
| Fanart do add-on | 1920 × 1080 JPG | 16:9 | fundo do add-on |
| Ícone de menu | 512 × 512 PNG | 1:1 | `ListItem.setArt` |
| Pôster fallback sTv | 600 × 900 PNG | 2:3 | filme, série ou episódio sem pôster |
| Capa fallback sFy | 512 × 512 PNG | 1:1 | álbum, single ou artista sem imagem |

## Regras obrigatórias

- O scaffolding inicial copia as artes genéricas para os caminhos reais em `addons/`.
- `icon.png` e `fanart.jpg` são obrigatórios para os três add-ons.
- Itens sTv usam TMDB/Xtream quando disponível e recorrem a `placeholder_poster.png` e `placeholder_fanart.jpg` quando não há imagem válida.
- Itens sFy usam metadata da origem quando disponível e recorrem a `placeholder_album.png`, `placeholder_artist.png` e `placeholder_fanart.jpg`.
- Nenhum emoji, caractere Unicode decorativo ou caminho absoluto pode substituir um asset.
- A renderização não baixa a mesma imagem a cada item; URLs remotas devem passar por cache e validação.
- A substituição das artes finais deve manter os nomes ou atualizar `addon.xml`, constantes de mídia, testes e documentação.

## Mapeamento de cópia

| Add-on | Papel | Origem no pacote | Destino no monorepo |
|---|---|---|---|
| `repository.srepo` | `addon_icon` | `artwork/generic/repository.srepo/icon.png` | `addons/repository.srepo/icon.png` |
| `repository.srepo` | `addon_fanart` | `artwork/generic/repository.srepo/fanart.jpg` | `addons/repository.srepo/fanart.jpg` |
| `plugin.video.stv` | `addon_icon` | `artwork/generic/plugin.video.stv/icon.png` | `addons/plugin.video.stv/icon.png` |
| `plugin.video.stv` | `addon_fanart` | `artwork/generic/plugin.video.stv/fanart.jpg` | `addons/plugin.video.stv/fanart.jpg` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/live_tv.png` | `addons/plugin.video.stv/resources/media/live_tv.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/vod.png` | `addons/plugin.video.stv/resources/media/vod.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/series.png` | `addons/plugin.video.stv/resources/media/series.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/search.png` | `addons/plugin.video.stv/resources/media/search.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/favorites.png` | `addons/plugin.video.stv/resources/media/favorites.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/continue_watching.png` | `addons/plugin.video.stv/resources/media/continue_watching.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/indexed_channels.png` | `addons/plugin.video.stv/resources/media/indexed_channels.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/indexed_movies.png` | `addons/plugin.video.stv/resources/media/indexed_movies.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/indexed_series.png` | `addons/plugin.video.stv/resources/media/indexed_series.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/provider.png` | `addons/plugin.video.stv/resources/media/provider.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/sync.png` | `addons/plugin.video.stv/resources/media/sync.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/settings.png` | `addons/plugin.video.stv/resources/media/settings.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/refresh.png` | `addons/plugin.video.stv/resources/media/refresh.png` |
| `plugin.video.stv` | `menu_icon` | `artwork/generic/plugin.video.stv/resources/media/error.png` | `addons/plugin.video.stv/resources/media/error.png` |
| `plugin.video.stv` | `fallback_poster` | `artwork/generic/plugin.video.stv/resources/media/placeholder_poster.png` | `addons/plugin.video.stv/resources/media/placeholder_poster.png` |
| `plugin.video.stv` | `fallback_fanart` | `artwork/generic/plugin.video.stv/resources/media/placeholder_fanart.jpg` | `addons/plugin.video.stv/resources/media/placeholder_fanart.jpg` |
| `plugin.audio.sfy` | `addon_icon` | `artwork/generic/plugin.audio.sfy/icon.png` | `addons/plugin.audio.sfy/icon.png` |
| `plugin.audio.sfy` | `addon_fanart` | `artwork/generic/plugin.audio.sfy/fanart.jpg` | `addons/plugin.audio.sfy/fanart.jpg` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/top_brazil.png` | `addons/plugin.audio.sfy/resources/media/top_brazil.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/top_world.png` | `addons/plugin.audio.sfy/resources/media/top_world.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/categories.png` | `addons/plugin.audio.sfy/resources/media/categories.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/playlists.png` | `addons/plugin.audio.sfy/resources/media/playlists.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/albums.png` | `addons/plugin.audio.sfy/resources/media/albums.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/singles.png` | `addons/plugin.audio.sfy/resources/media/singles.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/artists.png` | `addons/plugin.audio.sfy/resources/media/artists.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/search.png` | `addons/plugin.audio.sfy/resources/media/search.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/favorites.png` | `addons/plugin.audio.sfy/resources/media/favorites.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/history.png` | `addons/plugin.audio.sfy/resources/media/history.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/settings.png` | `addons/plugin.audio.sfy/resources/media/settings.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/refresh.png` | `addons/plugin.audio.sfy/resources/media/refresh.png` |
| `plugin.audio.sfy` | `menu_icon` | `artwork/generic/plugin.audio.sfy/resources/media/error.png` | `addons/plugin.audio.sfy/resources/media/error.png` |
| `plugin.audio.sfy` | `fallback_album` | `artwork/generic/plugin.audio.sfy/resources/media/placeholder_album.png` | `addons/plugin.audio.sfy/resources/media/placeholder_album.png` |
| `plugin.audio.sfy` | `fallback_artist` | `artwork/generic/plugin.audio.sfy/resources/media/placeholder_artist.png` | `addons/plugin.audio.sfy/resources/media/placeholder_artist.png` |
| `plugin.audio.sfy` | `fallback_fanart` | `artwork/generic/plugin.audio.sfy/resources/media/placeholder_fanart.jpg` | `addons/plugin.audio.sfy/resources/media/placeholder_fanart.jpg` |

## Critério de pronto

Antes de gerar ZIPs, a validação deve confirmar que todos os destinos obrigatórios existem, abrem corretamente e não possuem tamanho zero. A ausência de arte é erro de build, não aviso.
