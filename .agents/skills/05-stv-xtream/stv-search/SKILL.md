---
name: stv-search
title: Busca sTv
skill_id: 05.07
category: stv
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Busca sTv

## Missão

Pesquisar canais, filmes e séries localmente com filtros por domínio.

## Quando ativar

Ative esta skill quando a tarefa envolver **busca stv** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Escolher domínio**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Usar fts/fallback**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Limitar resultados**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Mostrar origem**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Preservar navegação**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- sTv é `plugin.video.stv`, cliente pessoal de um único provedor Xtream por perfil do addon.
- Host, usuário e senha vêm das configurações do Kodi; nunca do `.env` distribuído.
- API Xtream é encapsulada por cliente e adaptadores; a UI não monta endpoints diretamente.
- Live, VOD e séries compartilham modelos normalizados, mas mantêm regras de reprodução específicas.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Escolher domínio foi executado e possui evidência verificável.
- [ ] Usar fts/fallback foi executado e possui evidência verificável.
- [ ] Limitar resultados foi executado e possui evidência verificável.
- [ ] Mostrar origem foi executado e possui evidência verificável.
- [ ] Preservar navegação foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Credenciais no código.
- Urls xtream espalhadas.
- Usar nome como chave primária.
- Repetir download de catálogo a cada abertura.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
