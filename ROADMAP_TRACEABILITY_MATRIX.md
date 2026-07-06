# Matriz de rastreabilidade

| Capacidade | Addon | Skills principais | Persistência | Fase |
|---|---|---|---|---|
| Provedor Xtream, login e senha | sTv | xtream-configuration, settings-xml, env-secrets | settings Kodi | V1 |
| TV ao vivo | sTv | live-tv, video-playback, xtream-client | categories, live_streams | V1 |
| VOD | sTv | vod, movie-matching, images-hd | vod_items, metadata_cache, playback_progress | V1 |
| Séries | sTv | series, tv-matching, continue-watching | series, seasons, episodes, playback_progress | V1 |
| Busca/favoritos sTv | sTv | stv-search, stv-favorites, fts-search | favorites, FTS/fallback | V1 |
| Top Brasil/Mundo | sFy | charts, sfy-cache-resilience | charts_cache | V1 |
| Categorias | sFy | categories, spotify-like-navigation | music_categories | V1 |
| Minhas playlists | sFy | playlists, favorites-history | playlists, playlist_items | V1 |
| Busca e reprodução musical | sFy | sfy-search, yt-dlp-embedding, stream-resolution, audio-playback | search_cache, tracks | V1 |
| Capas e metadata | sFy | music-metadata, artwork | tracks/artwork cache | V1 |
| TMDB HD e sinopse | sTv | tmdb-client, movie-matching, tv-matching, images-hd | metadata_cache | V1 |
| Repositório e updates | sRepo | repository-addon, zip-packaging, addons-xml, checksums, github-pages | artefatos estáticos | V1 |
| Sincronização LAN manual | sTv/sFy | local-first-constitution, schema-versioning, security-review | journal de mudanças/export | V2 opcional |
