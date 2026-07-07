-- Schema de referência do plugin.audio.sfy
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS schema_migrations (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tracks (
    source TEXT NOT NULL,
    source_track_id TEXT NOT NULL,
    title TEXT NOT NULL,
    artist TEXT,
    album TEXT,
    duration_seconds INTEGER,
    thumbnail_url TEXT,
    webpage_url TEXT NOT NULL,
    metadata_json TEXT,
    updated_at TEXT NOT NULL,
    PRIMARY KEY (source, source_track_id)
);

CREATE TABLE IF NOT EXISTS playlists (
    playlist_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    artwork_url TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS playlist_items (
    playlist_id TEXT NOT NULL REFERENCES playlists(playlist_id) ON DELETE CASCADE,
    position INTEGER NOT NULL,
    source TEXT NOT NULL,
    source_track_id TEXT NOT NULL,
    added_at TEXT NOT NULL,
    PRIMARY KEY (playlist_id, position),
    UNIQUE (playlist_id, source, source_track_id)
);

CREATE TABLE IF NOT EXISTS play_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    source_track_id TEXT NOT NULL,
    played_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_sfy_history_played_at
ON play_history(played_at DESC);

CREATE TABLE IF NOT EXISTS discovery_cache (
    cache_key TEXT PRIMARY KEY,
    payload_json TEXT NOT NULL,
    fetched_at TEXT NOT NULL,
    expires_at TEXT NOT NULL
);

-- O sFy usa Minhas Playlists em vez de um recurso fixo de Favoritos.
-- Não armazenar URLs de formato assinadas/temporárias resolvidas pelo yt-dlp.
