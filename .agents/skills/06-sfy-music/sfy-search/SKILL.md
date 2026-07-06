---
name: sfy-search
title: Busca musical
skill_id: 06.03
category: sfy
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Busca musical

## Missão

Pesquisar faixas, artistas, álbuns e playlists com resultados normalizados.

## Quando ativar

Ative esta skill quando a tarefa envolver **busca musical** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Normalizar consulta**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Limitar resultados**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Deduplicar**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Separar tipo**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Renderizar estado vazio**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Normalizar consulta foi executado e possui evidência verificável.
- [ ] Limitar resultados foi executado e possui evidência verificável.
- [ ] Deduplicar foi executado e possui evidência verificável.
- [ ] Separar tipo foi executado e possui evidência verificável.
- [ ] Renderizar estado vazio foi executado e possui evidência verificável.
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
