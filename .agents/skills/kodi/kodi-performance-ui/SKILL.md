---
name: kodi-performance-ui
title: "Desempenho de UI e Navegação Kodi"
description: "Mantém menus responsivos e reduz trabalho por tela."
domain: "kodi"
triggers:
  - "menu lento"
  - "UI Kodi"
  - "listagem grande"
  - "otimizar navegação"
---

# Desempenho de UI e Navegação Kodi

## Orçamento por tela

A abertura deve fazer o mínimo necessário para mostrar conteúdo. Separe:

- dados essenciais;
- metadata secundária;
- arte remota;
- refresh em background/sob demanda.

## Técnicas

- cache de categorias;
- paginação de itens;
- batch `addDirectoryItems`;
- `offscreen=True` quando suportado;
- uma chamada agregada ao provider em vez de N+1;
- índices SQLite;
- evitar diálogos em fluxo normal;
- não reconstruir schema a cada rota.

## N+1

Se uma tela lista 100 filmes e faz uma chamada por filme para detalhes, redesenhe provider/cache. Pré-busque em lote ou carregue detalhes apenas ao abrir item.

## Arte

Forneça URLs ao Kodi em vez de baixar e converter na abertura, salvo necessidade comprovada.

## Percepção

Progresso é melhor que congelamento, mas não substitui otimização. Mostre dados stale válidos quando a política permitir.

## Medição

Registre duração por camada e quantidade de itens. Compare cache frio/quente e dispositivo modesto.
