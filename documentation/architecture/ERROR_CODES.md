# Contrato de erros

Códigos públicos permitem diagnóstico sem expor credenciais.

| Código | Significado |
|---|---|
| `SAILE-NET-001` | falha de conexão |
| `SAILE-NET-002` | timeout |
| `SAILE-XTREAM-001` | autenticação recusada |
| `SAILE-XTREAM-002` | resposta inválida |
| `SAILE-TMDB-001` | metadados não encontrados |
| `SAILE-YTDLP-001` | áudio não resolvido |
| `SAILE-DB-001` | falha de banco |
| `SAILE-ART-001` | artwork ausente |
| `SAILE-PLAY-001` | reprodução não iniciada |
| `SAILE-SYNC-001` | sincronização incompatível ou recusada |

A UI mostra mensagem legível e o código. O log registra detalhes sanitizados, nunca URL com senha/token.
