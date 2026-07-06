---
name: change-plan
title: Plano de mudança
skill_id: 00.03
category: governance
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Plano de mudança

## Missão

Produzir um plano executável por arquivo com riscos e critérios de aceitação.

## Quando ativar

Ative esta skill quando a tarefa envolver **plano de mudança** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Inspecionar estado atual**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Listar arquivos a criar/modificar/remover**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Ordenar mudanças**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Definir rollback**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Definir verificações**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- Produção nunca deve ser criada dentro de `.agents`; essa pasta contém somente instruções para o agente.
- Mudanças devem preservar a arquitetura local-first e o escopo de dois plugins administrados por um repositório.
- Antes de alterar código existente, o agente deve registrar impacto, arquivos afetados, riscos e validações.
- Nenhum segredo, token, senha, banco de usuário ou artefato de build entra em commits públicos.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Inspecionar estado atual foi executado e possui evidência verificável.
- [ ] Listar arquivos a criar/modificar/remover foi executado e possui evidência verificável.
- [ ] Ordenar mudanças foi executado e possui evidência verificável.
- [ ] Definir rollback foi executado e possui evidência verificável.
- [ ] Definir verificações foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Codificar sem plano.
- Misturar documentação do agente com produção.
- Renomear ids sem migração.
- Ampliar escopo silenciosamente.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
