# Módulos do ecossistema SAILE

## Ativos

### `repository.srepo`

Somente descoberta, instalação e atualização. Não executa regras de mídia.

### `resource.images.saile`

Pacote local de nove artes fixas. Atualiza o visual dos dois plugins sem duplicar arquivos. Não armazena pôsteres, capas ou thumbnails dinâmicos.

### `script.module.saile.core`

Infraestrutura pequena, versionada e compartilhada. Inclui artwork, notificações, caminhos, erros e capacidades. Não conhece Xtream, TMDB, yt-dlp ou modelos de mídia.

### `plugin.video.stv`

Domínio completo de IPTV: configuração Xtream, catálogo, busca, favoritos, reprodução, TMDB e SQLite próprio.

### `plugin.audio.sfy`

Domínio musical: busca, playlists locais, resolução e reprodução, com SQLite próprio.

## Condicionais

### `script.module.saile.ytdlp`

Só deve ser extraído quando o protótipo do sFy estiver funcional em Windows, Linux, Android TV e Fire TV. A atualização independente é desejável, mas não justifica criar um módulo não validado.

### `service.saile.monitor`

Adiado. Um serviço contínuo aumenta consumo em dispositivos modestos. Só será criado para uma função que não possa ser implementada com ações do plugin ou eventos pontuais.

### `repository.srepo.beta`

Adiado até existir pipeline estável, matriz de testes e política de promoção/rollback.
