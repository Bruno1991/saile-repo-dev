---
name: scope-guard
title: Proteção de escopo
skill_id: 00.01
category: governance
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Proteção de escopo

## Missão

Definir o que pertence ao sRepo, sTv e sFy antes de qualquer alteração.

## Quando ativar

Ative esta skill quando a tarefa envolver **proteção de escopo** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Classificar pedido por produto**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Registrar dentro/fora do escopo**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Detectar impacto cruzado**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Bloquear expansão silenciosa**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Gerar decisão objetiva**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Classificar pedido por produto foi executado e possui evidência verificável.
- [ ] Registrar dentro/fora do escopo foi executado e possui evidência verificável.
- [ ] Detectar impacto cruzado foi executado e possui evidência verificável.
- [ ] Bloquear expansão silenciosa foi executado e possui evidência verificável.
- [ ] Gerar decisão objetiva foi executado e possui evidência verificável.
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
