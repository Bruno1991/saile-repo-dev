---
name: favorites-progress
title: Favoritos e progresso
skill_id: 02.09
category: sqlite
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Favoritos e progresso

## Missão

Persistir ações do usuário separadas do catálogo atualizável.

## Quando ativar

Ative esta skill quando a tarefa envolver **favoritos e progresso** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Usar tabela por domínio**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Chave externa estável**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Upsert idempotente**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Registrar posição e duração**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Não apagar em sync**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Usar tabela por domínio foi executado e possui evidência verificável.
- [ ] Chave externa estável foi executado e possui evidência verificável.
- [ ] Upsert idempotente foi executado e possui evidência verificável.
- [ ] Registrar posição e duração foi executado e possui evidência verificável.
- [ ] Não apagar em sync foi executado e possui evidência verificável.
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
