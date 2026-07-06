---
name: pragmas
title: PRAGMAs seguros
skill_id: 02.06
category: sqlite
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# PRAGMAs seguros

## Missão

Escolher foreign_keys, journal mode, synchronous, busy_timeout e cache de forma compatível.

## Quando ativar

Ative esta skill quando a tarefa envolver **pragmas seguros** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Habilitar fks**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Definir busy_timeout**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Avaliar wal por plataforma**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Não usar synchronous off**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Medir antes de otimizar**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Habilitar fks foi executado e possui evidência verificável.
- [ ] Definir busy_timeout foi executado e possui evidência verificável.
- [ ] Avaliar wal por plataforma foi executado e possui evidência verificável.
- [ ] Não usar synchronous off foi executado e possui evidência verificável.
- [ ] Medir antes de otimizar foi executado e possui evidência verificável.
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
