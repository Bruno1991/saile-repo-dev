# Contrato oficial de navegação

## sFy

A home sempre inicia nesta ordem:

```text
1. Buscar                 common/search.png
2. Minhas Playlists       sfy/minhas_playlists.png
3. Sincronizar Dados      common/sync.png
4. Conteúdo dinâmico
```

O sFy não possui atalho fixo de Favoritos. A organização persistente do usuário é feita por **Minhas Playlists**.

## sTv

A home sempre inicia nesta ordem:

```text
1. TV ao Vivo             stv/live.png
2. VOD                     stv/vod.png
3. Séries                  stv/series.png
4. Sincronizar Dados       common/sync.png
```

Dentro de cada seção `TV ao Vivo`, `VOD` e `Séries`:

```text
1. Buscar                  common/search.png
2. Favoritos               stv/favoritos.png
3. Categorias e itens dinâmicos da seção
```

Favoritos e busca são filtrados pela seção atual. O item `Sincronizar Dados` aparece somente na home do sTv.

## Regras

- Não ordenar os atalhos fixos alfabeticamente.
- Não misturar favoritos de live, VOD e séries.
- Não esconder atalhos porque o catálogo ainda não foi sincronizado.
- Não adicionar conteúdo remoto antes dos atalhos fixos.
- Não usar emojis.
- Toda alteração de ordem exige ADR e atualização do teste `test_navigation_contract.py`.
