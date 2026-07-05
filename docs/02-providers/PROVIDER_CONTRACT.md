# Provider Contract

## Interface conceitual

```python
class MediaProvider:
    provider_id: str

    def capabilities(self) -> set[str]: ...
    def validate_configuration(self) -> None: ...
    def list_categories(self, media_type: str) -> list[Category]: ...
    def list_items(self, category_id: str, page: int | None = None) -> Page: ...
    def get_details(self, item_id: str) -> MediaItem: ...
    def search(self, query: str, media_type: str | None = None) -> list[MediaItem]: ...
    def resolve_playback(self, item_id: str) -> PlaybackSource: ...
```

## Regras

- IDs são namespaced pelo provider;
- erros externos são convertidos ao modelo comum;
- credenciais ficam na configuração, não nos modelos;
- resultados são normalizados antes da UI;
- capability ausente é declarada, não simulada;
- timeout e cancelamento são respeitados;
- responses remotas são validadas defensivamente;
- provider não importa APIs Kodi de UI.

## Versionamento

Mudança incompatível no contrato exige ADR e adaptação de todos os providers antes do merge.
