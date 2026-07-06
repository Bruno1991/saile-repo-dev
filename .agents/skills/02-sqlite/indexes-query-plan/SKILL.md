---
name: indexes-query-plan
title: Índices e query plan
skill_id: 02.07
category: sqlite
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Índices e query plan

## Missão

Criar índices baseados em consultas reais e verificar seu uso.

## Quando ativar

Ative esta skill quando a tarefa envolver **índices e query plan** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Listar queries críticas**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Criar índice composto**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Evitar redundância**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Usar explain query plan**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Medir tamanho e latência**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- sTv e sFy possuem bancos próprios; compartilhamento direto de um mesmo arquivo SQLite entre addons é proibido.
- Toda conexão habilita `PRAGMA foreign_keys=ON`, usa timeout e encerra cursores/conexões de forma determinística.
- Mudanças de esquema passam por migrações versionadas e transacionais; nunca apagar banco do usuário como estratégia de upgrade.
- Consultas recebem parâmetros por placeholders; concatenação de entrada do usuário em SQL é proibida.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Listar queries críticas foi executado e possui evidência verificável.
- [ ] Criar índice composto foi executado e possui evidência verificável.
- [ ] Evitar redundância foi executado e possui evidência verificável.
- [ ] Usar explain query plan foi executado e possui evidência verificável.
- [ ] Medir tamanho e latência foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- `select *` em caminho crítico.
- Migração destrutiva sem backup.
- Uma conexão global eterna.
- Sql montado por concatenação.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
