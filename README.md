# Saile Media Center

Saile Media Center é um addon Kodi local-first com três apps internos:

1. SaileTV: IPTV via Xtream Codes API, com canais ao vivo, VOD, séries, busca, favoritos e cache SQLite.
2. SaileFy: música via YouTube Data API, com busca, favoritos, top Brasil, top mundo, categorias e playlists locais.
3. sTorrent: índice genérico JSON configurável para filmes, séries, animes e doramas, com lançamentos, categorias, favoritos, continuar assistindo e metadados quando a API escolhida fornecer esses campos.

Este pacote segue o roadmap visual fornecido e foi organizado para rodar 100% no dispositivo do usuário dentro do Kodi. Não há servidor próprio obrigatório. As únicas chamadas externas são para APIs configuradas pelo usuário.

## O que está pronto para teste

- Addon Kodi `plugin.video.saile.mc` com menus reais, rotas, perfis, PIN, favoritos, continuar assistindo e SQLite local.
- Provider Xtream funcional para categorias, canais ao vivo, VOD e séries quando o usuário configurar host, login e senha.
- Provider YouTube Data API funcional para busca/listagem quando o usuário configurar uma API key. A reprodução usa URL compatível com o addon oficial do YouTube no Kodi quando instalado.
- Provider sTorrent genérico por API JSON configurável. O addon não embute fonte pirata nem endpoint ilegal; ele consome apenas a API que o usuário configurar e só reproduz `stream_url` direto ou magnet/URL resolvível pelo ambiente Kodi do usuário.
- Repositório Kodi `repository.saile` pronto para empacotar e publicar via GitHub Pages.
- `index.html`, `addons.xml`, `addons.xml.md5` e zips gerados em `zips/`.
- Documentação para Antigravity, biblioteca de skills, guia de regras, master spec e gitignore blindado.

## Estrutura principal

```text
plugin.video.saile.mc/       Addon principal do Kodi
repository.saile/            Addon de repositório para instalação/atualização
tools/build_repo.py          Gera zips, addons.xml, addons.xml.md5 e index.html
tools/preflight_no_secrets.py Verifica vazamento de segredos antes do commit
docs/                        Documentação de engenharia para Antigravity
zips/                        Pacotes finais para GitHub Pages
```

## Teste local no Kodi

1. Copie a pasta `plugin.video.saile.mc` para a pasta de addons do Kodi, ou instale o zip gerado em `zips/plugin.video.saile.mc/`.
2. Abra o Kodi e vá em Add-ons.
3. Abra Saile Media Center.
4. Entre em Configurações e informe os dados do Xtream, YouTube e/ou API JSON que deseja testar.
5. Use o perfil Adulto para todos os apps. Use Kids para bloquear SaileFy e sTorrent.

## Build do repositório GitHub Pages

Na raiz deste projeto:

```bash
python tools/preflight_no_secrets.py
python tools/build_repo.py --repo-url https://bruno1991.github.io/saile-repo-dev/
```

Depois envie para o repositório `https://github.com/Bruno1991/saile-repo-dev` e habilite GitHub Pages no branch principal apontando para a raiz do repositório.

Nunca suba `.env`, tokens, bancos `.db`, logs, dumps ou arquivos de mídia.
