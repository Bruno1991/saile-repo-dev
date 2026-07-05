# Error Model

## Categorias

- `ConfigurationError` — dados ausentes ou inválidos;
- `AuthenticationError` — credencial rejeitada;
- `ProviderUnavailable` — indisponibilidade temporária;
- `RateLimitError` — limite remoto;
- `NotFoundError` — entidade inexistente;
- `PlaybackResolutionError` — fonte não resolvida;
- `DatabaseError` — operação ou integridade;
- `MigrationError` — atualização de schema;
- `CompatibilityError` — recurso ausente no runtime;
- `UnexpectedError` — defeito não classificado.

## Política

Erros possuem mensagem técnica sanitizada e mensagem de usuário localizável. Não converter todo erro em lista vazia. Causa original pode ser encadeada, mas nunca exibida com segredo.
