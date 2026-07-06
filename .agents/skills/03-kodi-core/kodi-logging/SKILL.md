---
name: kodi-logging
title: Integração de logs Kodi
skill_id: 03.08
category: kodi-core
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Integração de logs Kodi

## Missão

Encapsular xbmc.log com prefixo, níveis e sanitização.

## Quando ativar

Ative esta skill quando a tarefa envolver **integração de logs kodi** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Criar logger único**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Mapear nível**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Adicionar addon id**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Mascarar**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Evitar spam por item**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- Usar `special://profile` e `xbmcvfs.translatePath` para dados locais e caminhos portáveis.
- Rotas de plugin são puras: interpretar parâmetros, chamar serviço e renderizar; não conter regras de negócio remotas.
- Cada listagem finaliza corretamente com `xbmcplugin.endOfDirectory` e itens reproduzíveis usam `IsPlayable=true`.
- Metadados e artwork são opcionais e nunca podem bloquear a navegação básica.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Criar logger único foi executado e possui evidência verificável.
- [ ] Mapear nível foi executado e possui evidência verificável.
- [ ] Adicionar addon id foi executado e possui evidência verificável.
- [ ] Mascarar foi executado e possui evidência verificável.
- [ ] Evitar spam por item foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Chamar api remota dentro da função que cria cada listitem.
- Usar caminho absoluto do sistema.
- Esquecer endofdirectory.
- Misturar roteador e cliente http.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
