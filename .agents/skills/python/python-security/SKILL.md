---
name: python-security
title: "Segurança Aplicada a Python"
description: "Previne injeção, SSRF, traversal, vazamento de segredos e execução insegura."
domain: "python"
triggers:
  - "segurança Python"
  - "entrada não confiável"
  - "URL externa"
  - "arquivo baixado"
  - "injeção"
---

# Segurança Aplicada a Python

## Superfícies

- parâmetros de rota `plugin://`;
- respostas de APIs;
- settings do usuário;
- nomes de arquivos;
- playlists e manifests;
- URLs de mídia;
- dados SQLite antigos ou manipulados.

## Regras

- nunca usar `eval`/`exec` em dados;
- nunca usar `pickle` para cache não confiável;
- parametrizar SQL;
- validar esquema/host de URLs;
- limitar redirecionamentos e tamanho de download;
- impedir path traversal;
- não executar binário baixado;
- não descompactar ZIP sem validar destinos;
- evitar `shell=True`;
- usar comparação e armazenamento apropriados para credenciais quando aplicável.

## SSRF

Quando o usuário fornece URL de provider, considere bloqueio opcional de esquemas perigosos e validação de host. Não permita `file://` ou protocolos inesperados em clientes HTTP.

## ZIP Slip

Antes de extrair, confirme que cada destino permanece dentro do diretório permitido.

## Dados sensíveis

Classifique credenciais, histórico de consumo, perfis e identificadores. Colete e persista somente o necessário.

## Resposta a incidente

Se um token apareceu em commit ou conversa operacional, trate como comprometido e recomende rotação; mascarar posteriormente não desfaz exposição.
