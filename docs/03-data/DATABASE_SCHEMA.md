# Database Schema

## Princípios

- `PRAGMA user_version` controla a versão;
- foreign keys habilitadas quando suportadas;
- IDs externos armazenados como TEXT;
- timestamps em UTC ISO-8601 ou epoch consistentemente definido;
- índices baseados em consultas reais;
- dados de cache separados de estado do usuário;
- senha e token não são armazenados no banco de catálogo.

## Tabelas canônicas recomendadas

### schema_migrations

`version INTEGER PRIMARY KEY`, `applied_at TEXT NOT NULL`, `checksum TEXT NOT NULL`.

### providers

`provider_id TEXT PRIMARY KEY`, `display_name TEXT NOT NULL`, `enabled INTEGER NOT NULL`, `updated_at TEXT NOT NULL`.

### categories

Chave primária composta por `provider_id`, `media_type`, `external_id`. Nome, parent, art e timestamps.

### media_items

Chave composta provider/tipo/id, category reference, title, plot, year, duration, art, payload normalizado opcional e validade de cache.

### profiles

ID local, nome, avatar, flags e timestamps.

### favorites

Chave composta profile/provider/media_type/media_id, criada em UTC.

### playback_progress

Mesma identidade de mídia, position, duration, completed e update timestamp.

### cache_entries

Namespace, key, payload, created_at, expires_at e etag quando aplicável.

O schema real do repositório deve ser importado para este documento antes de qualquer migração.
