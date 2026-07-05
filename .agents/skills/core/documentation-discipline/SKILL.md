---
name: documentation-discipline
title: "Disciplina de Documentação"
description: "Mantém arquitetura, decisões e estado do projeto sincronizados com o código."
domain: "core"
triggers:
  - "documentação"
  - "ADR"
  - "mudança arquitetural"
  - "handoff para outro agente"
---

# Disciplina de Documentação

## Documentos mínimos

- visão e escopo;
- arquitetura e limites de camadas;
- decisões registradas em ADR;
- esquema e política de migrações;
- guia de build e teste;
- publicação e rollback;
- troubleshooting;
- changelog.

## Regra de proximidade

Documente o mais perto possível da fonte:

- contrato de função no próprio módulo;
- decisão ampla em ADR;
- operação repetível em runbook;
- status temporário em documento de progresso;
- interface pública no README do componente.

## O que atualizar após mudanças

- nova rota: catálogo de rotas;
- nova tabela: diagrama/esquema e migração;
- novo provider: contrato e limitações;
- nova configuração: settings e strings;
- nova dependência: manifesto e instruções de build;
- mudança incompatível: ADR e changelog.

## Proibições

- documentação prometendo função inexistente;
- exemplos com segredos reais;
- diagramas divergentes do código;
- instruções que dependem de arquivo removido;
- changelog genérico como “melhorias”.

## Critério de qualidade

Outro agente deve conseguir continuar o trabalho sem redescobrir decisões essenciais por tentativa e erro.
