# Query and Index Policy

Consultas usam parâmetros. Paginação e filtros precisam de ordem determinística. Índices são adicionados após `EXPLAIN QUERY PLAN` e medição com volume representativo. Evitar índice redundante, `SELECT *` em caminhos críticos e transação longa durante rede ou UI.
