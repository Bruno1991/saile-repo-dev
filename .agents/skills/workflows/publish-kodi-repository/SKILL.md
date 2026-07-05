---
name: publish-kodi-repository
title: "Workflow: Publicar Repositório Kodi"
description: "Empacota e publica add-ons por processo repetível, validado e seguro."
domain: "workflows"
triggers:
  - "publicar Kodi repo"
  - "GitHub Pages Kodi"
  - "gerar addons.xml"
  - "release addon"
---

# Workflow: Publicar Repositório Kodi

## Preparação

- working tree revisada;
- segredos ausentes;
- versões incrementadas;
- changelog atualizado;
- testes passando.

## Build

1. descobrir add-ons por `addon.xml`;
2. validar XML e IDs;
3. copiar somente arquivos permitidos;
4. criar ZIP com pasta raiz;
5. extrair e revalidar;
6. agregar manifests em `addons.xml`;
7. gerar detector de mudança/checksum;
8. copiar assets;
9. gerar índice web opcional.

## Segurança

- HTTPS;
- hash forte quando suportado;
- token de publicação nunca no repositório;
- publicação somente após autorização explícita;
- evitar force push automático.

## Teste de consumo

Instale repository add-on em Kodi limpo, force refresh, instale plugin, atualize para nova versão e confirme integridade.

## Rollback

Preserve artefatos anteriores e documente como restaurar `addons.xml` e ZIP anterior.
