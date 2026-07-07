# Migrações SQLite

Cada plugin possui versão de schema independente da versão do add-on.

Regras:

1. Migração numerada e idempotência definida.
2. Execução dentro de transação.
3. Backup/rollback quando a operação não for reversível.
4. Preservar favoritos, progresso e playlists.
5. Nunca apagar o banco automaticamente.
6. Testar criação limpa e atualização de pelo menos a versão anterior.
7. Fechar conexões explicitamente, inclusive em testes Windows.
