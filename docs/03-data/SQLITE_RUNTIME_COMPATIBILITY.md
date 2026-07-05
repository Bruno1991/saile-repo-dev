# SQLite Runtime Compatibility

## Verificações obrigatórias por plataforma

Registrar, por ambiente testado:

- versão retornada por `sqlite3.sqlite_version`;
- `PRAGMA compile_options` quando permitido;
- suporte a foreign keys, JSON e FTS usados pelo projeto;
- comportamento de `journal_mode`;
- `busy_timeout` efetivo;
- funcionamento da API de backup;
- resultado de `quick_check`;
- filesystem e caminho do perfil Kodi.

## Política de WAL

WAL não é default universal. Só deve ser ativado após teste no filesystem e dispositivo-alvo, considerando arquivos auxiliares, desligamento abrupto e concorrência real. Fallback para journal compatível deve ser documentado.
