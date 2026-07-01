# Implementação do roadmap do Saile Media Center

Este documento transforma o roadmap visual fornecido em uma especificação executável para o addon Kodi `Saile Media Center`.

Imagem base do roadmap: `docs/assets/roadmap-saile-media-center.png`.

## 1. Produto

O Saile Media Center é um addon Kodi com três apps internos. O Kodi é a camada de apresentação. O addon executa toda a lógica localmente com Python e SQLite. O GitHub Pages serve apenas os arquivos estáticos de instalação e atualização do addon: `index.html`, `addons.xml`, checksums e `.zip`.

O addon não depende de servidor próprio. As chamadas externas existem somente para provedores configurados pelo usuário:

- Xtream Codes API para SaileTV.
- YouTube Data API para SaileFy.
- API JSON configurável para sTorrent.

## 2. Apps internos do roadmap

### 2.1 SaileTV

Cor do roadmap: rosa.

Responsabilidades:

- TV ao vivo.
- VOD.
- Séries.
- Busca.
- Favoritos.
- Conteúdo infantil filtrável para o perfil Kids.
- Indexação local em SQLite de canais, filmes e séries retornados pela API Xtream.

Fluxo do roadmap:

```text
Home -> SaileTV -> TV ao Vivo -> Categorias -> Canais -> Player
Home -> SaileTV -> VOD -> Categorias -> Filmes -> Player
Home -> SaileTV -> Séries -> Categorias -> Séries -> Temporadas -> Episódios -> Player
Home -> SaileTV -> Busca -> Resultado -> Player
Home -> SaileTV -> Favoritos -> Item -> Player
```

### 2.2 SaileFy

Cor do roadmap: verde.

Responsabilidades:

- Música via YouTube Data API.
- Busca.
- Favoritos.
- Top Brasil.
- Top mundo.
- Categorias.
- Minhas playlists locais.
- Capas, álbuns, singles e metadados quando retornados pela API.
- UI inspirada em navegação de música, sem copiar identidade visual proprietária.

Fluxo do roadmap:

```text
Home -> SaileFy -> Busca -> Resultados -> Reproduzir via YouTube plugin/URL resolvível
Home -> SaileFy -> Top Brasil -> Resultados
Home -> SaileFy -> Top Mundo -> Resultados
Home -> SaileFy -> Categorias -> Busca temática
Home -> SaileFy -> Minhas playlists -> Itens salvos localmente
Home -> SaileFy -> Favoritos -> Itens salvos localmente
```

### 2.3 sTorrent

Cor do roadmap: azul.

Responsabilidades:

- Índice genérico de filmes, séries, animes, doramas e outros conteúdos conforme a API legal/autorizada configurada pelo usuário.
- Lançamentos.
- Favoritos.
- Continuar assistindo.
- Categorias.
- Ranking TMDB quando a API escolhida retornar dados ou quando uma integração futura autorizada for configurada.
- Capas, sinopse, pontuação e metadados quando fornecidos pela API.

Regra obrigatória:

O addon não deve embutir endpoint pirata, scraper de sites de pirataria, bypass anti-bloqueio ou fonte de conteúdo adulto/pornográfico. O sTorrent é um adaptador JSON genérico. O usuário configura uma API própria, legal ou autorizada.

Fluxo do roadmap:

```text
Home -> sTorrent -> Lançamentos -> Item -> Player se houver stream_url resolvível
Home -> sTorrent -> Categorias -> Categoria -> Itens
Home -> sTorrent -> Ranking TMDB -> Itens
Home -> sTorrent -> Busca -> Resultados
Home -> sTorrent -> Favoritos -> Item
Home -> sTorrent -> Continuar assistindo -> Item
```

## 3. Perfis, PIN e controle dos pais

O roadmap define três entradas principais:

- Adulto.
- Kids.
- Configurações.

Regras:

- O perfil Adulto acessa SaileTV, SaileFy e sTorrent.
- O perfil Kids acessa somente conteúdo vindo do SaileTV.
- O perfil Kids não acessa SaileFy nem sTorrent.
- O PIN tem 4 a 6 dígitos numéricos.
- Configurações e perfil Adulto podem exigir PIN se o PIN estiver configurado.
- Gerenciamento de perfil permite criar, editar e deletar perfil.

## 4. SQLite

O roadmap pede SQLite como centro local de dados.

Tabelas mínimas implementadas:

- `profiles`.
- `favorites`.
- `continue_watching`.
- `cached_items`.
- `indexed_channels`.
- `indexed_movies`.
- `indexed_series`.
- `local_playlists`.
- `local_playlist_items`.

## 5. Indexação

O roadmap mostra:

- Canais indexados.
- Canais favoritos.
- Filmes indexados.
- Filmes favoritos.
- Séries indexadas.
- Séries favoritas.
- Top Brasil.
- Top mundo.
- Categorias.
- Minhas playlists.
- Capas, álbuns, singles, YouTube metadados.

No MVP pronto para teste:

- Xtream indexa categorias, canais, VOD e séries em SQLite.
- Favoritos são armazenados por provider e tipo.
- Continuar assistindo é armazenado por provider e tipo.
- SaileFy salva favoritos e playlists localmente.
- sTorrent salva favoritos e continuar assistindo localmente.

## 6. Regras que o Antigravity deve obedecer

1. Não colocar lógica de API dentro da UI.
2. Não criar servidor externo obrigatório.
3. Não salvar token, `.env`, login ou senha no Git.
4. Não quebrar o fluxo de perfis e PIN.
5. Não habilitar Kids para SaileFy ou sTorrent.
6. Não implementar endpoint pirata hardcoded.
7. Não remover SQLite.
8. Não trocar Python por outra stack no runtime do addon.
9. Não depender de HTML para lógica do addon; HTML é somente índice do GitHub Pages.
10. Não publicar bancos, logs, dumps ou zips temporários.
