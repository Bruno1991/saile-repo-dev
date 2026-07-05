---
name: python-http-clients
title: "Clientes HTTP Robustos"
description: "Padroniza rede com timeout, codificação, retries limitados e validação de resposta."
domain: "python"
triggers:
  - "API HTTP"
  - "provider remoto"
  - "download JSON"
  - "requisição de rede"
---

# Clientes HTTP Robustos

## Requisitos obrigatórios

- timeout finito;
- User-Agent identificável sem dados pessoais;
- validação de status;
- limite de tamanho quando aplicável;
- decodificação explícita;
- erro de transporte separado de erro de conteúdo;
- cancelamento quando integrado a progresso Kodi.

## Fronteira do cliente

O cliente retorna dados do provider ou modelos intermediários. Ele não cria `ListItem`, não escreve no banco e não abre diálogo.

## URL e parâmetros

Use `urllib.parse.urlencode` ou biblioteca disponível no repositório. Nunca concatene entrada bruta.

## Retries

Repita apenas falhas transitórias e operações idempotentes. Use poucas tentativas e backoff. Não repita automaticamente:

- autenticação inválida;
- resposta 4xx permanente;
- payload inválido consistente;
- operações com efeito colateral não idempotente.

## TLS

Não desabilite verificação de certificado para “resolver” erro. Documente certificados privados ou forneça configuração explícita, com alerta de risco.

## Paginação

Modele paginação, limites e continuidade. Não baixe catálogos gigantes na abertura da tela inicial.

## Observabilidade

Registre host sanitizado, endpoint lógico, status, duração e quantidade de itens. Não registre corpo completo por padrão.
