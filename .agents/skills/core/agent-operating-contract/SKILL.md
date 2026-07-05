---
name: agent-operating-contract
title: "Contrato Operacional do Agente"
description: "Define como o agente investiga, modifica, valida e relata mudanças de engenharia."
domain: "core"
triggers:
  - "início de qualquer tarefa"
  - "alteração de código"
  - "correção de bug"
  - "implementação de funcionalidade"
---

# Contrato Operacional do Agente

## Objetivo

Impedir mudanças impulsivas e transformar cada tarefa em um ciclo verificável de engenharia.

## Procedimento obrigatório

### 1. Inspecionar

- localizar a raiz real do repositório;
- ler a árvore relevante;
- identificar entry points, arquivos de configuração, testes e scripts de build;
- procurar implementações existentes antes de criar novas;
- registrar restrições explícitas do usuário e do projeto.

### 2. Delimitar

Defina o menor conjunto de arquivos que resolve o problema. Separe:

- causa raiz;
- sintomas;
- dívida técnica relacionada, mas fora do escopo;
- risco de regressão;
- contratos que não podem mudar.

### 3. Implementar

- prefira alterações pequenas e coesas;
- preserve interfaces públicas;
- não duplique lógica já existente;
- escreva código compatível com a versão mínima declarada;
- use nomes do domínio, não nomes genéricos como `data`, `manager2` ou `helper_new`.

### 4. Validar

A validação mínima inclui:

- sintaxe;
- imports;
- testes existentes;
- caso feliz;
- pelo menos um caso de erro;
- revisão de logs e segredos;
- revisão do diff.

### 5. Relatar

O relatório deve listar:

- caminho de cada arquivo criado, modificado ou removido;
- comportamento antes e depois;
- comandos ou testes executados;
- riscos e limitações restantes.

## Proibições

- alegar sucesso sem evidência;
- ocultar falha de teste;
- substituir uma arquitetura inteira para corrigir um defeito local;
- criar código dentro de `.agents`;
- alterar IDs do Kodi, nomes de tabelas ou chaves de settings sem migração.

## Critério de saída

A skill termina somente quando o agente consegue responder: “o que mudou, por que mudou, como foi validado e como reverter?”.
