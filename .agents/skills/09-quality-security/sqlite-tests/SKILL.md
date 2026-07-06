---
name: sqlite-tests
title: Testes SQLite
skill_id: 09.05
category: quality
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Testes SQLite

## Missão

Verificar migrações, constraints, índices, UPSERT e preservação de favoritos.

## Quando ativar

Ative esta skill quando a tarefa envolver **testes sqlite** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Usar banco temporário**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Aplicar todas migrações**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Testar upgrade**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Rodar quick_check**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Verificar rollback**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Usar banco temporário foi executado e possui evidência verificável.
- [ ] Aplicar todas migrações foi executado e possui evidência verificável.
- [ ] Testar upgrade foi executado e possui evidência verificável.
- [ ] Rodar quick_check foi executado e possui evidência verificável.
- [ ] Verificar rollback foi executado e possui evidência verificável.
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
