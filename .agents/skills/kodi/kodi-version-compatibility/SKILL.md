---
name: kodi-version-compatibility
title: "Compatibilidade entre Versões do Kodi"
description: "Gerencia diferenças de API, settings e metadata entre versões."
domain: "kodi"
triggers:
  - "Kodi 19 20 21 22"
  - "compatibilidade de versão"
  - "API depreciada Kodi"
---

# Compatibilidade entre Versões do Kodi

## Não assumir “master” = instalado

A documentação master pode representar uma versão posterior. Descubra a versão mínima e máxima suportada pelo projeto.

## Estratégias

- declarar dependência mínima em `addon.xml`;
- manter uma matriz de APIs usadas;
- encapsular diferenças em `compat.py`;
- detectar recursos por presença quando seguro;
- evitar branches espalhados pelo código;
- remover compatibilidade antiga somente com decisão registrada.

## Áreas sensíveis

- metadata/InfoTags;
- settings tipados e formato XML;
- argumentos de `ListItem`;
- inputstream properties;
- Python embarcado;
- repositório e manifesto.

## Testes

Uma versão mínima declarada deve ser realmente testada. Testar apenas a mais nova não prova compatibilidade retroativa.

## Falha clara

Quando versão não suportada for detectada, falhe com mensagem compreensível, não com `AttributeError` em ação aleatória.

## Dependências

Verifique a disponibilidade de módulos no repositório de cada versão. Não suponha que um add-on de módulo recente existe em versões antigas.
