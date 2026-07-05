---
name: kodi-repository-packaging
title: "Empacotamento e Repositório Kodi"
description: "Gera ZIPs, addons.xml, checksum e repositório de forma reproduzível e segura."
domain: "kodi"
triggers:
  - "repositório Kodi"
  - "addons.xml"
  - "zip addon"
  - "GitHub Pages"
  - "publicar addon"
---

# Empacotamento e Repositório Kodi

## Layout de pacote

O ZIP deve conter a pasta raiz do add-on:

```text
plugin.video.exemplo-1.2.3.zip
└── plugin.video.exemplo/
    ├── addon.xml
    └── ...
```

Não compacte apenas o conteúdo interno.

## Repositório

A estrutura publicada normalmente contém diretórios por ID, ZIP versionado, assets e um `addons.xml` agregado, além do arquivo usado para detectar mudanças.

## Regras

- gerar a partir dos `addon.xml` fonte;
- ordenar saída para reprodutibilidade;
- validar XML;
- usar HTTPS;
- preferir hashes fortes quando suportados;
- nunca incluir `.env`, banco, logs ou ferramentas privadas;
- não editar artefatos gerados manualmente.

## Repositório add-on

Use extensão `xbmc.addon.repository` e bloco `<dir>` compatível com versões-alvo. URLs `info`, `checksum` e `datadir` devem apontar para arquivos reais.

## Versionamento

ZIP, `addon.xml`, `addons.xml` e changelog precisam concordar.

## Validação antes de publicar

- listar conteúdo do ZIP;
- extrair em diretório temporário;
- validar `addon.xml` extraído;
- calcular hash;
- instalar ZIP em Kodi limpo;
- atualizar pelo repositório;
- testar rollback ou versão anterior quando aplicável.
