# Routing and Navigation

## Contrato

Rotas são ações nomeadas com parâmetros codificados por `urllib.parse.urlencode`. Nenhum parâmetro recebe código executável, caminho arbitrário ou URL secreta completa.

## Regras

- validar `handle` e parâmetros;
- converter tipos na fronteira;
- separar itens navegáveis de itens reproduzíveis;
- marcar `IsPlayable` apenas quando a rota resolve playback;
- definir content type consistente;
- sempre finalizar listagem com `endOfDirectory`;
- não usar labels como IDs;
- preservar rotas publicadas ou criar compatibilidade.

## Erros

Rota desconhecida gera log e diretório finalizado, sem stack trace exposto ao usuário. Parâmetros inválidos retornam mensagem compreensível e não acessam banco/rede.
