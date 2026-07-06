---
name: stream-resolution
title: Resolução de stream musical
skill_id: 06.02
category: sfy
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Resolução de stream musical

## Missão

Selecionar URL temporária de áudio adequada para o player Kodi.

## Quando ativar

Ative esta skill quando a tarefa envolver **resolução de stream musical** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Buscar item**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Extrair formatos**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Filtrar audio-only**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Escolher codec/bitrate compatível**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Resolver imediatamente**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- sFy é `plugin.audio.sfy` e usa yt-dlp como resolvedor de fontes, não como camada de UI.
- O padrão é streaming por URL temporária; download persistente de mídia fica fora do escopo principal.
- A experiência visual pode ser inspirada no Spotify, mas usa identidade, nomes e assets próprios.
- Falhas de extração, formatos indisponíveis, idade, região e autenticação são tratadas sem travar o Kodi.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Buscar item foi executado e possui evidência verificável.
- [ ] Extrair formatos foi executado e possui evidência verificável.
- [ ] Filtrar audio-only foi executado e possui evidência verificável.
- [ ] Escolher codec/bitrate compatível foi executado e possui evidência verificável.
- [ ] Resolver imediatamente foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Invocar binário por shell quando api python resolve.
- Baixar mídia por padrão.
- Armazenar cookies no repositório.
- Confundir resultado de busca com item reproduzível.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
