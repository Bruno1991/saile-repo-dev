---
name: kodi-providers-networking
title: "Providers e Integrações de Rede"
description: "Cria adapters de fontes externas sem acoplar API, UI e cache."
domain: "kodi"
triggers:
  - "provider Kodi"
  - "API externa"
  - "Xtream"
  - "YouTube API"
  - "catálogo remoto"
---

# Providers e Integrações de Rede

## Contrato de provider

Um provider deve expor operações do domínio, por exemplo:

```text
list_categories()
list_items(category_id, page)
get_details(item_id)
resolve_playback(item_id)
search(query, page)
```

## Normalização

Cada provider converte seu payload em modelos internos. A UI não conhece nomes de campos externos.

## Autenticação

Credenciais vêm da configuração e são aplicadas dentro do cliente. Não trafegam em rotas internas nem são persistidas em cache sem necessidade.

## Resiliência

- timeout;
- paginação;
- retries limitados;
- tratamento de rate limit;
- validação de JSON;
- fallback para cache stale;
- cancelamento.

## Registry

Use registry quando existem múltiplos providers. Ele resolve implementação por ID estável e evita condicionais espalhadas.

## Legalidade

Integre apenas serviços e conteúdos cujo acesso, reprodução e distribuição sejam autorizados. Respeite termos de serviço, autenticação e limites da API.

## Testes

Use fixtures mínimas e testes de contrato para garantir que providers diferentes retornam modelos equivalentes.
