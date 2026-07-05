---
name: repository-context
title: "Leitura e Contexto do Repositório"
description: "Ensina o agente a compreender um projeto existente antes de editar."
domain: "core"
triggers:
  - "primeiro contato com repositório"
  - "dump de projeto"
  - "árvore de arquivos"
  - "continuação de implementação"
---

# Leitura e Contexto do Repositório

## Inventário inicial

O agente deve encontrar e ler, quando existirem:

- `README`, `AGENTS`, `CONTRIBUTING`, ADRs e documentação de arquitetura;
- `addon.xml`, `settings.xml`, arquivos de idioma e entry point;
- módulos de domínio, persistência, rede, UI e playback;
- scripts de build, empacotamento e publicação;
- testes e fixtures;
- `.gitignore`, arquivos de ambiente e configuração de CI.

## Mapa de execução

Produza mentalmente ou em documentação um mapa com:

```text
entrada -> roteador -> caso de uso -> provider -> persistência -> apresentação/playback
```

Para Kodi, identifique especificamente:

```text
plugin:// invocado
  -> sys.argv
  -> parsing de query string
  -> dispatch da ação
  -> criação de ListItem
  -> addDirectoryItem/addDirectoryItems
  -> endOfDirectory ou setResolvedUrl
```

## Perguntas que devem ser respondidas antes da edição

1. Qual arquivo realmente inicia a aplicação?
2. Onde ficam os contratos públicos?
3. Qual camada acessa rede?
4. Qual camada acessa SQLite?
5. Onde erros são convertidos em mensagens de UI?
6. Há cache? Qual TTL e política de invalidação?
7. Como a versão é incrementada e publicada?
8. Quais plataformas são suportadas?

## Sinais de arquitetura frágil

- UI executando SQL ou HTTP diretamente;
- credenciais trafegando em URLs exibidas ou logs;
- um único arquivo concentrando roteamento, rede, banco e UI;
- tabelas criadas durante qualquer consulta sem controle de versão;
- exceções amplas e silenciosas;
- uso de caminhos absolutos;
- dependência de ordem implícita de imports.

## Saída esperada

Antes de codificar, o agente deve saber quais arquivos são fonte da verdade e quais são artefatos gerados. Nunca edite manualmente `addons.xml`, ZIPs ou checksums se o projeto possui gerador oficial para eles.
