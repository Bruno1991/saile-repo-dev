---
name: add-feature-safely
title: "Workflow: Adicionar Funcionalidade com Segurança"
description: "Adiciona recurso preservando arquitetura, dados e rotas existentes."
domain: "workflows"
triggers:
  - "adicionar funcionalidade"
  - "nova tela"
  - "novo provider"
  - "nova rota"
---

# Workflow: Adicionar Funcionalidade com Segurança

## Sequência

1. localizar requisito e contratos afetados;
2. mapear fluxo atual;
3. criar teste ou roteiro de regressão;
4. definir modelo e caso de uso;
5. alterar provider/persistência se necessário;
6. expor por rota/UI;
7. adicionar settings/idioma;
8. validar erros e cancelamento;
9. atualizar documentação;
10. revisar diff e pacote.

## Perguntas de controle

- a UI passou a conhecer detalhes externos?
- uma tabela precisa de migração?
- action nova conflita com favorita antiga?
- a funcionalidade funciona sem cache?
- funciona com cache stale?
- quais dados sensíveis foram adicionados?
- a home ficou mais lenta?

## Saída

Relatório com arquivos, comportamento, testes, versão necessária e rollback.
