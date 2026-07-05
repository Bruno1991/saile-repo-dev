---
name: root-cause-debugging
title: "Depuração por Causa Raiz"
description: "Orienta diagnóstico reproduzível sem aplicar correções aleatórias."
domain: "core"
triggers:
  - "erro"
  - "falha"
  - "traceback"
  - "comportamento intermitente"
  - "Kodi fecha ou trava"
---

# Depuração por Causa Raiz

## Regra central

Não corrija o primeiro sintoma observado. Reconstrua a cadeia causal.

## Método

### Reproduzir

Registre:

- ação exata do usuário;
- versão do Kodi e plataforma;
- versão do add-on;
- dados mínimos necessários;
- resultado esperado e observado;
- trecho relevante do log.

### Localizar fronteira da falha

Teste separadamente:

- parsing da rota;
- consulta ao banco;
- chamada do provider;
- transformação de dados;
- montagem de `ListItem`;
- resolução de URL;
- player.

### Formular hipótese

Uma hipótese útil é falsificável, por exemplo:

> A lista fica vazia porque `category_id` chega como string vazia e a consulta exige inteiro.

Uma hipótese ruim é “o Kodi está bugado”.

### Instrumentar

Adicione logs temporários estruturados, sem segredos. Registre IDs, contagens, duração e estado, não payloads sensíveis completos.

### Confirmar

A correção precisa eliminar a causa e manter os demais fluxos.

## Erros comuns em add-ons Kodi

- `sys.argv[1]` indisponível fora do contexto de plugin;
- URL mal codificada;
- ausência de `endOfDirectory`;
- uso incorreto de `isFolder`;
- `setResolvedUrl` chamado com item sem path;
- exceção de rede engolida e convertida em lista vazia;
- DB bloqueado por transação longa;
- path nativo incompatível com Android;
- arte ou metadata em formato não aceito pela versão-alvo.

## Entrega

Inclua causa raiz, evidência e teste de regressão. Não entregue apenas “adicionei try/except”.
