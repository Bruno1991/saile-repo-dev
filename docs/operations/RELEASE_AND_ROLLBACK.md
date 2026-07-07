# Release e rollback

Cada add-on possui versão independente. O pipeline bloqueia publicação quando:

- dependência mínima não existe;
- XML/entrypoint inválido;
- arte declarada ausente;
- versão diminuiu;
- ZIP contém segredo, banco, log ou cache Python;
- checksum diverge;
- navegação contratual falha em teste.

Fluxo: branch → testes → build candidato → Kodi real → tag → Pages. Rollback republica uma versão conhecida e registra a causa.
