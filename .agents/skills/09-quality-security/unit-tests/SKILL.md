---
name: unit-tests
title: Testes unitários
skill_id: 09.03
category: quality
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Testes unitários

## Missão

Testar normalizadores, roteamento, matching, SQL e seleção de formatos sem Kodi real.

## Quando ativar

Ative esta skill quando a tarefa envolver **testes unitários** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Isolar função**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Usar fixtures**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Cobrir bordas**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Não acessar rede**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Reportar regressão**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- Toda entrega inclui testes relevantes, validação de XML, inspeção do ZIP e checklist manual no Kodi.
- Logs removem credenciais, query strings sensíveis, tokens e URLs assinadas.
- Erros recuperáveis degradam recursos opcionais; corrupção, schema incompatível e segredo exposto falham de forma explícita.
- O agente não declara sucesso sem evidência: comando, teste, log, checksum ou inspeção de artefato.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Isolar função foi executado e possui evidência verificável.
- [ ] Usar fixtures foi executado e possui evidência verificável.
- [ ] Cobrir bordas foi executado e possui evidência verificável.
- [ ] Não acessar rede foi executado e possui evidência verificável.
- [ ] Reportar regressão foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Teste que depende de serviço real sem controle.
- Log com senha.
- Marcar tarefa concluída sem executar validação.
- Corrigir sintoma apagando dados.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
