# Matriz de rastreabilidade

| Capacidade | Componente | Persistência | Fase | Evidência mínima |
|---|---|---|---|---|
| Distribuição/updates | `repository.srepo` | artefatos estáticos | V1 | ZIP, addons.xml, checksum |
| Nove artes fixas | `resource.images.saile` | arquivos locais | V1 | manifesto + teste de existência |
| Infra comum | `script.module.saile.core` | nenhuma de domínio | V1 | teste de dependências/import |
| Home sTv | `plugin.video.stv` | nenhuma | V1 | ordem coberta por teste |
| Buscar/Favoritos por seção | `plugin.video.stv` | favorites/FTS | V1 | ordem + filtro por seção |
| Xtream | `plugin.video.stv` | catálogo/cache | V1 | fixtures sanitizadas + Kodi real |
| TMDB | `plugin.video.stv` | metadata cache | V1 | matching e fallback |
| Home sFy | `plugin.audio.sfy` | nenhuma | V1 | ordem coberta por teste |
| Minhas Playlists | `plugin.audio.sfy` | playlists/playlist_tracks | V1 | CRUD e preservação em migração |
| yt-dlp | sFy, inicialmente interno | tracks/cache | prova técnica | reprodução em Windows/Linux/Android/Fire TV |
| `script.module.saile.ytdlp` | módulo futuro | nenhuma | condicionado | ADR após prova técnica |
| Sincronização LAN manual | sTv/sFy | journal/export | V2 | ação explícita + conflito testado |
| Diagnóstico seguro | core/plugins | pacote sanitizado | V2 | teste de redaction |
| Serviço de monitoramento | futuro | a definir | futuro | necessidade comprovada |
| PVR avançado | futuro | M3U/XMLTV local | futuro | ADR e teste multiplataforma |
