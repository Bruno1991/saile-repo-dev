---
name: agent-output-contract
title: Contrato de saída do agente
skill_id: 00.09
category: governance
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Contrato de saída do agente

## Missão

Padronizar respostas do agente com caminhos, arquivos completos e validações.

## Quando ativar

Ative esta skill quando a tarefa envolver **contrato de saída do agente** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Informar diretório de trabalho**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Entregar conteúdo completo**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Explicar remoções**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Listar comandos**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Reportar resultado real**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Informar diretório de trabalho foi executado e possui evidência verificável.
- [ ] Entregar conteúdo completo foi executado e possui evidência verificável.
- [ ] Explicar remoções foi executado e possui evidência verificável.
- [ ] Listar comandos foi executado e possui evidência verificável.
- [ ] Reportar resultado real foi executado e possui evidência verificável.
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
