---
name: audio-playback
title: Reprodução de áudio
skill_id: 04.07
category: kodi-ui
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Reprodução de áudio

## Missão

Configurar itens sFy como música com duração, artista, álbum e capa.

## Quando ativar

Ative esta skill quando a tarefa envolver **reprodução de áudio** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Definir media=music**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Preencher musicinfotag**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Marcar isplayable**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Resolver formato de áudio**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Não usar extensão falsa**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- A interface deve funcionar no skin Estuary e em skins de terceiros sem depender de propriedades privadas.
- Não usar emojis como ícones; usar PNGs do projeto via `setArt` e fallback seguro.
- Operações lentas exibem progresso cancelável; trabalho pesado não roda repetidamente durante renderização de cada item.
- Reprodução usa URL resolvida no último momento e não persiste URLs temporárias como se fossem permanentes.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Definir media=music foi executado e possui evidência verificável.
- [ ] Preencher musicinfotag foi executado e possui evidência verificável.
- [ ] Marcar isplayable foi executado e possui evidência verificável.
- [ ] Resolver formato de áudio foi executado e possui evidência verificável.
- [ ] Não usar extensão falsa foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Emoji como arte.
- Bloquear thread da ui sem progresso.
- Persistir url temporária.
- Assumir um skin específico.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
