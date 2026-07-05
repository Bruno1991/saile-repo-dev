# Performance Budgets

Os budgets iniciais devem ser medidos e ajustados com dados reais:

- abrir menu principal sem rede;
- primeira listagem com feedback imediato;
- transações de banco curtas;
- nenhum payload completo mantido em memória sem necessidade;
- paginação/lotes para catálogos grandes;
- ZIP sem dependência ou asset redundante;
- limpeza de cache incremental;
- operações longas canceláveis.

## Registro

Cada medição informa dispositivo, Kodi, commit, tamanho de dados, tempo, pico de memória quando disponível e método. Regressões relevantes bloqueiam release.
