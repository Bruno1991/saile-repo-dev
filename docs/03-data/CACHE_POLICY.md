# Cache Policy

## Classes

- categorias: TTL moderado e refresh manual;
- catálogo: TTL curto/moderado por provider;
- detalhes: TTL maior quando estáveis;
- playback source: não persistir além da expiração;
- imagens: delegar ao Kodi quando possível;
- erro: negative cache curto apenas quando seguro.

## Regras

Cache possui namespace, chave, criação, expiração e versão de schema. Dados stale podem sustentar navegação quando o provider falha e a UI informa a condição. Alteração de credencial/provider invalida somente namespaces afetados.

Limpeza é incremental, não bloqueia a UI e preserva favoritos/progresso.
