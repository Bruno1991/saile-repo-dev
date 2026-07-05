# Domain Model

## Entidades principais

### ProviderIdentity

`provider_id`, `display_name`, `capabilities`, `configuration_state`.

### Category

`id`, `provider_id`, `media_type`, `name`, `parent_id`, `art`.

### MediaItem

`id`, `provider_id`, `media_type`, `title`, `plot`, `year`, `art`, `duration`, `content_rating`, `metadata`.

### Series and Episode

Série contém identidade e metadados; temporada e episódio usam IDs estáveis do provider e não dependem do texto exibido.

### PlaybackSource

`url`, `mime_type`, `is_live`, `headers`, `inputstream_properties`, `expires_at`, `resume_supported`.

### Profile

Perfil local, nome, avatar e políticas. Credenciais de provider não são duplicadas por perfil sem requisito explícito.

### Progress

Chave composta por perfil, provider e mídia; posição, duração, atualização e estado concluído.

## Regras

IDs externos são strings. Modelos não carregam senha. Campos desconhecidos de provider não atravessam o domínio sem normalização.
