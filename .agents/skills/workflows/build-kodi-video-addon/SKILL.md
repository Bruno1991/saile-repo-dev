---
name: build-kodi-video-addon
title: "Workflow: Construir Plugin de Vídeo Kodi"
description: "Orquestra a construção completa de um plugin de vídeo desde requisitos até ZIP instalável."
domain: "workflows"
triggers:
  - "construir addon completo"
  - "novo plugin de vídeo"
  - "MVP Kodi"
---

# Workflow: Construir Plugin de Vídeo Kodi

## Entrada necessária

- nome e ID desejados;
- fonte de conteúdo autorizada;
- versões Kodi alvo;
- plataformas alvo;
- autenticação e settings;
- funcionalidades mínimas.

## Etapas

### 1. Descoberta

Documente domínio, rotas, modelos, provider, cache e playback. Confirme restrições legais e técnicas.

### 2. Esqueleto

Crie manifesto, entry point, estrutura modular, idioma, settings, licença e README.

### 3. Vertical slice

Implemente `Home -> Categoria -> Lista -> Play` com dados reais autorizados ou fixture apenas para teste claramente identificada.

### 4. Persistência

Crie schema versionado, repository, TTL e migração inicial.

### 5. Resiliência

Adicione timeout, mensagens, logs, cancelamento, paginação e fallback.

### 6. Testes

Execute testes Python, validação XML, compilação sintática, teste de ZIP e roteiro manual no Kodi.

### 7. Publicação

Gere ZIP, `addons.xml`, checksum/hash, repository add-on e página HTTP/HTTPS conforme arquitetura escolhida.

## Gate

Não avançar para publicação enquanto o fluxo vertical não funcionar em Kodi limpo e não houver evidência de que o ZIP possui a pasta raiz correta.
