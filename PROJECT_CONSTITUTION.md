# Constituição de engenharia

## Artigo 1 — Local-first

sTv e sFy executam integralmente dentro do ambiente Kodi do usuário. Serviços externos são apenas provedores de dados ou mídia configurados pelo usuário. O sistema não depende de servidor próprio, banco remoto, fila remota ou autenticação central.

## Artigo 2 — Três add-ons, três responsabilidades

- `repository.srepo`: descoberta, instalação e atualização.
- `plugin.video.stv`: domínio IPTV/Xtream e vídeo.
- `plugin.audio.sfy`: domínio música/yt-dlp e áudio.

Nenhum plugin importa módulos internos do outro. Código realmente reutilizável deve ser pequeno, versionado e empacotado como dependência Kodi própria somente após ADR; copiar um utilitário simples é preferível a criar acoplamento prematuro.

## Artigo 3 — Persistência

Cada plugin usa seu próprio SQLite no perfil do addon. Catálogo atualizável, estado do usuário e cache são tabelas separadas. Migrações são versionadas, transacionais e testadas. Sincronização LAN é opcional, manual e não faz parte do caminho crítico da V1.

## Artigo 4 — Segurança

`.env` é ferramenta de desenvolvimento. GitHub PAT é exclusivamente de build/administração e nunca entra no runtime. Credenciais Xtream vêm das configurações do Kodi. Um token TMDB usado por cliente local público deve ser dedicado e tratável como recuperável, pois não pode ser mantido secretamente em software distribuído ao usuário.

## Artigo 5 — Experiência Kodi

A UI usa componentes públicos do Kodi, assets PNG, metadados e navegação por controle remoto. O comportamento precisa funcionar no skin padrão e degradar corretamente quando metadata, imagem ou serviço externo falhar.

## Artigo 6 — Evidência

Nenhuma tarefa é concluída apenas por plausibilidade. A conclusão exige evidência proporcional: testes, parse de XML, `PRAGMA quick_check`, inspeção de ZIP, checksum, instalação limpa ou reprodução validada.
