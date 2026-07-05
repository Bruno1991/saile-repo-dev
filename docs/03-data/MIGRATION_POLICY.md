# Migration Policy

## Regras

- migrações são incrementais, ordenadas e imutáveis após release;
- aplicar dentro de transação quando o SQLite permitir;
- criar backup antes de migração de risco;
- verificar versão inicial e final;
- nunca apagar banco automaticamente por falha de migração;
- migração deve ser idempotente quanto à detecção de versão;
- checksum detecta arquivo alterado após aplicação.

## Processo

1. copiar fixture de versão anterior;
2. aplicar migração;
3. validar `foreign_key_check` e `quick_check`;
4. verificar dados essenciais;
5. testar reabertura;
6. testar falha simulada e rollback;
7. registrar evidência.

Downgrade não é presumido. Quando impossível, rollback usa backup compatível.
