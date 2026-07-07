# Matriz de compatibilidade

## Alvos

| Plataforma | Prioridade | Validação necessária |
|---|---:|---|
| Windows + Kodi estável | alta | instalação, menus, SQLite e reprodução |
| Linux + Kodi estável | alta | instalação, permissões e reprodução |
| Android TV + Kodi estável | alta | memória, controle remoto e reprodução |
| Fire TV/Firestick + Kodi estável | alta | desempenho e capacidade do yt-dlp |
| Versão futura do Kodi | preventiva | testes sem promessa de suporte antes da estabilidade |

## Requisitos comuns

- Python fornecido pelo Kodi.
- `resource.images.saile` e `script.module.saile.core` instalados como dependências.
- Dados escritos somente em `special://profile/addon_data/`.
- Nenhum executável externo obrigatório na V1.

## yt-dlp

O sFy só é considerado suportado em uma plataforma após a prova técnica resolver e reproduzir áudio, cancelar corretamente e não deixar threads/processos presos. A extração para módulo independente depende dessa evidência.
