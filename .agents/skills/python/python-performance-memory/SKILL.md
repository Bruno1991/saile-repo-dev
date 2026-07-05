---
name: python-performance-memory
title: "Desempenho e Memória em Dispositivos Limitados"
description: "Orienta otimização para Android TV, Fire TV e hardware modesto."
domain: "python"
triggers:
  - "desempenho"
  - "Firestick"
  - "memória"
  - "lista grande"
  - "lentidão"
---

# Desempenho e Memória em Dispositivos Limitados

## Medir primeiro

Colete duração por etapa:

- rede;
- parsing;
- consulta SQL;
- construção de itens;
- entrega ao Kodi;
- resolução de playback.

## Otimizações de alto impacto

- paginação;
- cache com TTL;
- `addDirectoryItems` para listas grandes;
- `ListItem(..., offscreen=True)` quando adequado à versão-alvo;
- consultas com índices;
- imagens dimensionadas e cacheadas pelo Kodi;
- evitar carregar catálogos completos na memória;
- processar em geradores/lotes.

## Memória

Não mantenha simultaneamente payload bruto, payload transformado e lista final quando um pipeline incremental resolve. Remova campos externos desnecessários cedo.

## Startup

Importações do entry point devem ser leves. Não faça:

- sync de banco;
- chamada HTTP;
- migração pesada;
- varredura de disco;
- import de bibliotecas enormes sem necessidade.

## Cache

Cacheie dados caros e relativamente estáveis. Não cacheie erro de autenticação como lista vazia. Inclua versão de schema e identidade do provider na chave.

## Critério

Otimização deve vir com métrica antes/depois ou justificativa clara de complexidade evitada.
