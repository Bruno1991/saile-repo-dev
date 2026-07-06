# Contrato futuro de sincronização LAN manual

## Não fazer

- Não colocar o `.db` em pasta SMB compartilhada.
- Não abrir o mesmo SQLite por dois dispositivos.
- Não sincronizar automaticamente sem ação do usuário.
- Não transmitir credenciais, cookies, URLs Xtream ou tokens.

## Envelope sugerido

```json
{
  "protocol_version": 1,
  "addon_id": "plugin.video.stv",
  "device_id": "uuid-local",
  "exported_at": "ISO-8601",
  "records": [
    {
      "entity": "favorite",
      "key": ["vod", "123"],
      "updated_at": "ISO-8601",
      "deleted": false,
      "payload": {}
    }
  ]
}
```

## Política inicial

- Favoritos: last-write-wins por `updated_at`, com tombstone para remoção.
- Progresso: maior `updated_at`; em empate, maior posição não concluída ou estado concluído.
- Playlists: operações por item com IDs estáveis; não substituir lista inteira sem confirmação.
- Catálogos e caches: não sincronizar; cada dispositivo refaz o próprio cache.
