---
name: resolved-playback
title: Reprodução resolvida
skill_id: 04.06
category: kodi-ui
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Reprodução resolvida

## Missão

Entregar ao Kodi uma URL reproduzível com ListItem e MIME apropriados.

## Quando ativar

Ative esta skill quando a tarefa envolver **reprodução resolvida** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Resolver no último momento**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Validar url**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Definir path**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Setmimetype**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Setresolvedurl**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Resolver no último momento foi executado e possui evidência verificável.
- [ ] Validar url foi executado e possui evidência verificável.
- [ ] Definir path foi executado e possui evidência verificável.
- [ ] Setmimetype foi executado e possui evidência verificável.
- [ ] Setresolvedurl foi executado e possui evidência verificável.
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
