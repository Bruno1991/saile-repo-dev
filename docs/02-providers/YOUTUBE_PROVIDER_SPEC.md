# YouTube Provider Specification

## Princípio

Usar apenas APIs e métodos autorizados, respeitando termos, quotas e limitações. O provider não deve simular uma API privada nem contornar restrições de reprodução.

## Capacidades

Busca, metadados e resolução conforme métodos oficialmente permitidos no ambiente. A ausência de uma capacidade deve ser comunicada.

## Dados

Persistir apenas metadados necessários e permitidos. Chaves de API são settings locais e nunca entram no Git, log ou diagnóstico exportado.

## Quota

Operações devem informar rate limit, evitar repetição desnecessária e usar cache de metadados de acordo com regras aplicáveis.
