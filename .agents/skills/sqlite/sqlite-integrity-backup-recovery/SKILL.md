---
name: sqlite-integrity-backup-recovery
title: "Integridade, Backup e Recuperação"
description: "Protege dados locais e define resposta a corrupção ou falha de migração."
domain: "sqlite"
triggers:
  - "backup SQLite"
  - "corrupção"
  - "integrity_check"
  - "recuperar banco"
---

# Integridade, Backup e Recuperação

## Classificação de dados

- **reconstruível**: cache, índice remoto;
- **importante**: favoritos, histórico, progresso;
- **sensível**: perfis, tokens, preferências pessoais.

A política depende da classe.

## Verificações

- `PRAGMA quick_check` para diagnóstico rápido;
- `PRAGMA integrity_check` para investigação completa;
- validação de schema e versão;
- contagens e constraints após migração.

Não execute verificações pesadas em toda navegação.

## Backup

Prefira a backup API do SQLite por meio de `Connection.backup()` quando disponível, em vez de copiar arquivo ativo de forma cega.

## Recuperação

Fluxo sugerido:

1. interromper escritas;
2. preservar arquivo original com timestamp;
3. tentar backup/leitura segura;
4. reconstruir somente dados descartáveis;
5. importar dados recuperáveis;
6. informar ao usuário sem expor path sensível desnecessário.

## Falha de migração

Não continue usando schema parcialmente migrado. Reverta a transação ou restaure backup.

## Exclusão

Nunca apague automaticamente banco de dados importante apenas porque uma consulta falhou.
