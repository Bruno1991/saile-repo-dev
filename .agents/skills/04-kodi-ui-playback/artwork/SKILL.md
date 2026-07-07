---
name: artwork
title: Artwork e fallbacks
skill_id: 04.02
category: kodi-ui
version: 1.1.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Artwork e fallbacks

## Missão

Selecionar thumb, icon, poster, fanart e fallback sem imagens quebradas.

## Quando ativar

Ative esta skill quando a tarefa envolver **artwork e fallbacks** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Priorizar cache local**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Validar url**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Definir fallback do addon**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Não baixar durante cada render**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Limpar cache por ttl**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
6. **Aplicar pacote genérico**: leia `artwork/artwork-manifest.json`, copie assets ausentes para o add-on de destino definido no manifesto e valide dimensões/formato.
7. **Bloquear arte ausente**: trate `icon.png`, `fanart.jpg` e fallbacks declarados como requisito de build.

## Regras específicas do projeto

- A interface deve funcionar no skin Estuary e em skins de terceiros sem depender de propriedades privadas.
- Não usar emojis como ícones; usar PNGs do projeto via `setArt` e fallback seguro.
- O pacote `artwork/generic/` é a fonte oficial de placeholders temporários; o runtime usa os nove assets fixos instalados por `resource.images.saile`; cada add-on mantém apenas seu `icon.png` e `fanart.jpg` próprios.
- Consulte `docs/ui/ARTWORK_CATALOG.md` para nomes, dimensões, destinos e ordem de fallback.
- Operações lentas exibem progresso cancelável; trabalho pesado não roda repetidamente durante renderização de cada item.
- Reprodução usa URL resolvida no último momento e não persiste URLs temporárias como se fossem permanentes.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Priorizar cache local foi executado e possui evidência verificável.
- [ ] Validar url foi executado e possui evidência verificável.
- [ ] Definir fallback do addon foi executado e possui evidência verificável.
- [ ] Não baixar durante cada render foi executado e possui evidência verificável.
- [ ] Limpar cache por ttl foi executado e possui evidência verificável.
- [ ] O manifesto de artwork foi aplicado e todos os assets obrigatórios existem nos destinos do add-on.
- [ ] As imagens foram abertas/validadas e possuem formato e proporção compatíveis.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Emoji como arte.
- Bloquear thread da ui sem progresso.
- Persistir url temporária.
- Assumir um skin específico.
- Apontar o runtime diretamente para `artwork/generic/`.
- Gerar ZIP com `icon.png`, `fanart.jpg` ou fallback obrigatório ausente.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
