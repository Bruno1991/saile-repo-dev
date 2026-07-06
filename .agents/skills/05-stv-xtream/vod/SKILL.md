---
name: vod
title: Filmes VOD
skill_id: 05.05
category: stv
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Filmes VOD

## Missão

Listar filmes, enriquecer metadados e reproduzir extensão informada pelo provider.

## Quando ativar

Ative esta skill quando a tarefa envolver **filmes vod** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Normalizar filme**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Preservar stream_id**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Usar container_extension**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Enriquecer tmdb**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Registrar progresso**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Normalizar filme foi executado e possui evidência verificável.
- [ ] Preservar stream_id foi executado e possui evidência verificável.
- [ ] Usar container_extension foi executado e possui evidência verificável.
- [ ] Enriquecer tmdb foi executado e possui evidência verificável.
- [ ] Registrar progresso foi executado e possui evidência verificável.
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
