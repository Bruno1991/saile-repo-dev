---
name: python-refactoring
title: "Refatoração Controlada"
description: "Melhora estrutura sem misturar mudança comportamental e reescrita ampla."
domain: "python"
triggers:
  - "refatorar"
  - "dividir arquivo"
  - "melhorar arquitetura"
  - "reduzir complexidade"
---

# Refatoração Controlada

## Sequência segura

1. caracterizar comportamento existente;
2. adicionar teste de proteção;
3. mover código sem alterar lógica;
4. validar;
5. só depois melhorar algoritmo ou contrato.

## Técnicas

- extrair parser puro;
- introduzir modelo interno;
- mover HTTP para provider;
- mover SQL para repositório;
- criar caso de uso entre UI e infraestrutura;
- substituir globals por dependências explícitas;
- quebrar função por responsabilidade.

## Preservar

- parâmetros e actions de rota;
- IDs usados em favoritos;
- formato de configuração;
- esquema persistido;
- mensagens e fluxos públicos, salvo escopo.

## Sinais de excesso

- dezenas de arquivos com uma função trivial;
- abstração sem segunda implementação ou benefício de teste;
- interfaces espelhando classe concreta integralmente;
- mudança de nomes sem ganho semântico;
- novo framework dentro de add-on pequeno.

## Saída

O agente deve explicar quais dependências foram invertidas, quais ciclos foram removidos e por que a nova estrutura reduz risco real.
