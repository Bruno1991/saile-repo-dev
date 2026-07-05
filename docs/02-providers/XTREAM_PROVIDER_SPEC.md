# Xtream Provider Specification

## Capacidades

Autenticação/configuração, categorias live/VOD/séries, itens, detalhes quando disponíveis e resolução de playback.

## Configuração

Host normalizado, usuário e senha fornecidos pelo usuário. Não embutir credenciais. URL exibida em logs deve remover user, password e tokens.

## Resiliência

- timeouts de conexão e leitura;
- validação de JSON e tipos;
- lotes controlados;
- cache por tipo de entidade;
- fallback stale somente para navegação, não para fonte expirada;
- erros de autenticação não entram em retry infinito.

## Normalização

IDs permanecem strings. Extensões e URLs são tratadas como dados não confiáveis. Art e metadata podem estar ausentes. Categorias duplicadas devem ser resolvidas por chave composta provider/tipo/id.

## Testes

Fixtures sanitizadas para resposta normal, vazia, parcial, inválida, autenticação falha, timeout e alteração de schema remoto.
