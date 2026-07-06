---
name: continue-watching
title: Continuar assistindo
skill_id: 04.09
category: kodi-ui
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Continuar assistindo

## Missão

Capturar e restaurar progresso sem sobrescrever estado concluído incorretamente.

## Quando ativar

Ative esta skill quando a tarefa envolver **continuar assistindo** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Ouvir estado do player**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Persistir posição**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Aplicar resume**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Definir limiar de concluído**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Limpar entradas antigas**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Ouvir estado do player foi executado e possui evidência verificável.
- [ ] Persistir posição foi executado e possui evidência verificável.
- [ ] Aplicar resume foi executado e possui evidência verificável.
- [ ] Definir limiar de concluído foi executado e possui evidência verificável.
- [ ] Limpar entradas antigas foi executado e possui evidência verificável.
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
