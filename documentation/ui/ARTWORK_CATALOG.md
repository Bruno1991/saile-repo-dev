# Catálogo oficial de artwork

## Princípio

Cada add-on mantém sua identidade na própria raiz:

```text
icon.png
fanart.jpg
```

Todos os demais ícones fixos acordados são instalados por `resource.images.saile`.

## Nove artes compartilhadas

```text
resource.images.saile/resources/media/
├── common/
│   ├── search.png
│   ├── erro.png
│   ├── check.png
│   └── sync.png
├── sfy/
│   └── minhas_playlists.png
└── stv/
    ├── live.png
    ├── vod.png
    ├── series.png
    └── favoritos.png
```

## Uso

| Arquivo | Consumidor | Uso |
|---|---|---|
| `common/search.png` | sTv/sFy | busca |
| `common/erro.png` | sTv/sFy | pop-up de erro |
| `common/check.png` | sTv/sFy | pop-up de sucesso |
| `common/sync.png` | sTv/sFy | sincronização LAN manual |
| `sfy/minhas_playlists.png` | sFy | playlists locais |
| `stv/live.png` | sTv | TV ao vivo |
| `stv/vod.png` | sTv | filmes/VOD |
| `stv/series.png` | sTv | séries |
| `stv/favoritos.png` | sTv | favoritos por seção |

## Não pertence ao recurso

- logos de canais;
- pôsteres de filmes/séries;
- fanarts de conteúdo;
- thumbnails do YouTube;
- capas de álbum/faixa/artista;
- imagens obtidas de Xtream ou TMDB;
- cache gerado em runtime.

Essas imagens são dinâmicas e usam URL/cache do Kodi.

## Convenções

- PNG 1:1, preferencialmente 512×512 para ícones.
- Nomes minúsculos, sem espaço ou acento.
- Substituição futura preserva nome e proporção.
- O manifesto `artwork/artwork-manifest.json` é a fonte de verdade do bootstrap.
