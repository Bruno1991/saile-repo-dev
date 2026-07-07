# Diagnóstico e manutenção

## Operações futuras

- limpar cache sTv;
- limpar cache sFy;
- reconstruir índice;
- verificar banco;
- exportar/restaurar dados não sensíveis;
- gerar pacote de diagnóstico sanitizado.

## Pacote de diagnóstico

```text
saile-diagnostics.zip
├── system.json
├── addons.json
├── versions.json
├── database-schema.json
└── sanitized.log
```

Nunca incluir credenciais, tokens, cookies, URLs de mídia, `.env` ou conteúdo integral do banco.
