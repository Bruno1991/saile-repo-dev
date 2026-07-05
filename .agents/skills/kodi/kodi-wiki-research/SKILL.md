---
name: kodi-wiki-research
title: "Pesquisa na Wiki e API Oficial do Kodi"
description: "Ensina o agente a verificar APIs e evitar exemplos obsoletos."
domain: "kodi"
triggers:
  - "consultar Kodi Wiki"
  - "API Kodi desconhecida"
  - "verificar método Kodi"
  - "documentação Kodi"
---

# Pesquisa na Wiki e API Oficial do Kodi

## Fontes prioritárias

1. documentação Python API da versão-alvo;
2. Kodi Wiki oficial;
3. código-fonte oficial do Kodi;
4. add-ons oficiais recentes;
5. fórum apenas como evidência complementar.

## Processo

1. identificar versão Kodi alvo;
2. localizar módulo e método exato;
3. verificar assinatura, parâmetros, retorno e versão de introdução/depreciação;
4. conferir exemplo oficial;
5. registrar link e data;
6. testar no ambiente alvo.

## Cuidados

- páginas antigas podem usar APIs removidas;
- `setInfo`, settings e metadata evoluíram;
- snippets de fóruns podem ser específicos de uma versão;
- nomes XBMC antigos podem persistir em documentação;
- documentação “master” pode descrever versão futura em relação ao usuário.

## Regra de implementação

Se a API não foi confirmada, o agente deve marcar a incerteza e não inventar assinatura. Para compatibilidade multi-versão, encapsule diferenças em um adaptador pequeno.

## Registro

Toda decisão dependente de versão deve aparecer em comentário técnico, ADR ou matriz de compatibilidade, não ficar apenas na memória do agente.
