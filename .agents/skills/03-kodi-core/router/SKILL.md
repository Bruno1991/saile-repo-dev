---
name: router
title: Roteamento de plugin
skill_id: 03.04
category: kodi-core
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Roteamento de plugin

## Missão

Interpretar ações e parâmetros com whitelist e fallback para home.

## Quando ativar

Ative esta skill quando a tarefa envolver **roteamento de plugin** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Parsear sys.argv**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Validar action**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Coagir ids**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Despachar handler**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Tratar rota desconhecida**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Parsear sys.argv foi executado e possui evidência verificável.
- [ ] Validar action foi executado e possui evidência verificável.
- [ ] Coagir ids foi executado e possui evidência verificável.
- [ ] Despachar handler foi executado e possui evidência verificável.
- [ ] Tratar rota desconhecida foi executado e possui evidência verificável.
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
