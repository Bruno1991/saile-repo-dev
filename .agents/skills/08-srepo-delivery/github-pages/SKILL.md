---
name: github-pages
title: Publicação GitHub Pages
skill_id: 08.07
category: srepo
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Publicação GitHub Pages

## Missão

Publicar site estático do repositório sem executar Python no servidor.

## Quando ativar

Ative esta skill quando a tarefa envolver **publicação github pages** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Gerar site antes**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Incluir .nojekyll**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Configurar source/action**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Validar urls**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Testar instalação**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- sRepo é `repository.srepo` e publica `plugin.video.stv`, `plugin.audio.sfy` e o próprio repositório.
- ZIP deve conter a pasta raiz com o mesmo ID do addon e excluir `.env`, bancos, caches, testes temporários e ferramentas locais.
- `addons.xml`, checksum e diretórios versionados são gerados de forma determinística.
- GitHub Pages serve apenas arquivos estáticos; build e validação rodam localmente ou no GitHub Actions.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Gerar site antes foi executado e possui evidência verificável.
- [ ] Incluir .nojekyll foi executado e possui evidência verificável.
- [ ] Configurar source/action foi executado e possui evidência verificável.
- [ ] Validar urls foi executado e possui evidência verificável.
- [ ] Testar instalação foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Editar addons.xml manualmente.
- Publicar .env.
- Zip com estrutura errada.
- Versão divergente entre addon.xml e nome do zip.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
