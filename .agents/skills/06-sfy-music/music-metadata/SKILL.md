---
name: music-metadata
title: Metadados musicais
skill_id: 06.08
category: sfy
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Metadados musicais

## Missão

Preencher título, artista, álbum, duração, thumb e origem sem inventar dados.

## Quando ativar

Ative esta skill quando a tarefa envolver **metadados musicais** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Usar payload da fonte**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Normalizar artista**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Selecionar thumbnail**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Validar duração**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Preservar source_url**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Usar payload da fonte foi executado e possui evidência verificável.
- [ ] Normalizar artista foi executado e possui evidência verificável.
- [ ] Selecionar thumbnail foi executado e possui evidência verificável.
- [ ] Validar duração foi executado e possui evidência verificável.
- [ ] Preservar source_url foi executado e possui evidência verificável.
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
