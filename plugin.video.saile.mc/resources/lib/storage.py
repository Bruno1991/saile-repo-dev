# -*- coding: utf-8 -*-
"""SQLite local do Saile Media Center."""

from __future__ import absolute_import

import json
import os
import sqlite3
import time
from contextlib import contextmanager

from kodi import profile_path

DB_FILE = profile_path("saile_media_center.db")


@contextmanager
def connect():
    """Abre conexão SQLite com row_factory."""
    parent = os.path.dirname(DB_FILE)
    if not os.path.isdir(parent):
        os.makedirs(parent, exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    """Cria schema local idempotente."""
    with connect() as db:
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                kind TEXT NOT NULL CHECK(kind IN ('adult','kids')),
                avatar TEXT,
                created_at INTEGER NOT NULL
            );

            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                profile_id INTEGER NOT NULL,
                provider TEXT NOT NULL,
                media_type TEXT NOT NULL,
                external_id TEXT NOT NULL,
                title TEXT NOT NULL,
                artwork TEXT,
                payload_json TEXT,
                created_at INTEGER NOT NULL,
                UNIQUE(profile_id, provider, media_type, external_id)
            );

            CREATE TABLE IF NOT EXISTS continue_watching (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                profile_id INTEGER NOT NULL,
                provider TEXT NOT NULL,
                media_type TEXT NOT NULL,
                external_id TEXT NOT NULL,
                title TEXT NOT NULL,
                artwork TEXT,
                position_seconds INTEGER DEFAULT 0,
                duration_seconds INTEGER DEFAULT 0,
                payload_json TEXT,
                updated_at INTEGER NOT NULL,
                UNIQUE(profile_id, provider, media_type, external_id)
            );

            CREATE TABLE IF NOT EXISTS cached_items (
                cache_key TEXT PRIMARY KEY,
                provider TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                expires_at INTEGER NOT NULL,
                created_at INTEGER NOT NULL
            );

            CREATE TABLE IF NOT EXISTS indexed_channels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                provider TEXT NOT NULL,
                external_id TEXT NOT NULL,
                category_id TEXT,
                title TEXT NOT NULL,
                artwork TEXT,
                payload_json TEXT,
                updated_at INTEGER NOT NULL,
                UNIQUE(provider, external_id)
            );

            CREATE TABLE IF NOT EXISTS indexed_movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                provider TEXT NOT NULL,
                external_id TEXT NOT NULL,
                category_id TEXT,
                title TEXT NOT NULL,
                artwork TEXT,
                payload_json TEXT,
                updated_at INTEGER NOT NULL,
                UNIQUE(provider, external_id)
            );

            CREATE TABLE IF NOT EXISTS indexed_series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                provider TEXT NOT NULL,
                external_id TEXT NOT NULL,
                category_id TEXT,
                title TEXT NOT NULL,
                artwork TEXT,
                payload_json TEXT,
                updated_at INTEGER NOT NULL,
                UNIQUE(provider, external_id)
            );

            CREATE TABLE IF NOT EXISTS local_playlists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                profile_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                provider TEXT NOT NULL DEFAULT 'youtube',
                created_at INTEGER NOT NULL,
                UNIQUE(profile_id, title, provider)
            );

            CREATE TABLE IF NOT EXISTS local_playlist_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                playlist_id INTEGER NOT NULL,
                provider TEXT NOT NULL,
                media_type TEXT NOT NULL,
                external_id TEXT NOT NULL,
                title TEXT NOT NULL,
                artwork TEXT,
                payload_json TEXT,
                created_at INTEGER NOT NULL,
                UNIQUE(playlist_id, provider, media_type, external_id)
            );

            CREATE INDEX IF NOT EXISTS idx_favorites_profile ON favorites(profile_id, provider, media_type);
            CREATE INDEX IF NOT EXISTS idx_continue_profile ON continue_watching(profile_id, provider, media_type);
            CREATE INDEX IF NOT EXISTS idx_cache_expires ON cached_items(expires_at);
            CREATE INDEX IF NOT EXISTS idx_channels_category ON indexed_channels(category_id);
            CREATE INDEX IF NOT EXISTS idx_movies_category ON indexed_movies(category_id);
            CREATE INDEX IF NOT EXISTS idx_series_category ON indexed_series(category_id);
            """
        )


def ensure_default_profiles():
    """Garante perfis Adulto e Kids."""
    now = int(time.time())
    with connect() as db:
        db.execute(
            "INSERT OR IGNORE INTO profiles(name, kind, avatar, created_at) VALUES(?,?,?,?)",
            ("Adulto", "adult", "art/adult.png", now),
        )
        db.execute(
            "INSERT OR IGNORE INTO profiles(name, kind, avatar, created_at) VALUES(?,?,?,?)",
            ("Kids", "kids", "art/kids.png", now),
        )


def list_profiles():
    """Lista perfis."""
    with connect() as db:
        return [dict(r) for r in db.execute("SELECT * FROM profiles ORDER BY kind, name")]


def get_profile(profile_id):
    """Obtém perfil por id."""
    with connect() as db:
        row = db.execute("SELECT * FROM profiles WHERE id=?", (profile_id,)).fetchone()
        return dict(row) if row else None


def get_profile_by_name(name):
    """Obtém perfil por nome."""
    with connect() as db:
        row = db.execute("SELECT * FROM profiles WHERE name=?", (name,)).fetchone()
        return dict(row) if row else None


def save_profile(name, kind="adult", avatar=""):
    """Cria ou atualiza perfil."""
    now = int(time.time())
    with connect() as db:
        db.execute(
            "INSERT INTO profiles(name, kind, avatar, created_at) VALUES(?,?,?,?) "
            "ON CONFLICT(name) DO UPDATE SET kind=excluded.kind, avatar=excluded.avatar",
            (name, kind, avatar, now),
        )


def delete_profile(profile_id):
    """Remove perfil que não seja padrão."""
    with connect() as db:
        row = db.execute("SELECT name FROM profiles WHERE id=?", (profile_id,)).fetchone()
        if row and row["name"] not in ("Adulto", "Kids"):
            db.execute("DELETE FROM profiles WHERE id=?", (profile_id,))


def cache_get(cache_key):
    """Lê cache válido."""
    now = int(time.time())
    with connect() as db:
        row = db.execute(
            "SELECT payload_json FROM cached_items WHERE cache_key=? AND expires_at>?",
            (cache_key, now),
        ).fetchone()
        if not row:
            return None
        try:
            return json.loads(row["payload_json"])
        except Exception:
            return None


def cache_set(cache_key, provider, payload, ttl_seconds):
    """Grava cache com TTL."""
    now = int(time.time())
    expires = now + int(ttl_seconds)
    with connect() as db:
        db.execute(
            "INSERT INTO cached_items(cache_key, provider, payload_json, expires_at, created_at) VALUES(?,?,?,?,?) "
            "ON CONFLICT(cache_key) DO UPDATE SET payload_json=excluded.payload_json, expires_at=excluded.expires_at, created_at=excluded.created_at",
            (cache_key, provider, json.dumps(payload, ensure_ascii=False), expires, now),
        )


def upsert_favorite(profile_id, provider, media_type, external_id, title, artwork="", payload=None):
    """Cria ou atualiza favorito."""
    now = int(time.time())
    with connect() as db:
        db.execute(
            "INSERT INTO favorites(profile_id, provider, media_type, external_id, title, artwork, payload_json, created_at) "
            "VALUES(?,?,?,?,?,?,?,?) "
            "ON CONFLICT(profile_id, provider, media_type, external_id) DO UPDATE SET title=excluded.title, artwork=excluded.artwork, payload_json=excluded.payload_json",
            (profile_id, provider, media_type, external_id, title, artwork, json.dumps(payload or {}, ensure_ascii=False), now),
        )


def list_favorites(profile_id, provider=None, media_type=None):
    """Lista favoritos do perfil."""
    sql = "SELECT * FROM favorites WHERE profile_id=?"
    params = [profile_id]
    if provider:
        sql += " AND provider=?"
        params.append(provider)
    if media_type:
        sql += " AND media_type=?"
        params.append(media_type)
    sql += " ORDER BY created_at DESC"
    with connect() as db:
        return [dict(r) for r in db.execute(sql, params)]


def upsert_continue(profile_id, provider, media_type, external_id, title, artwork="", position_seconds=0, duration_seconds=0, payload=None):
    """Cria ou atualiza continuar assistindo."""
    now = int(time.time())
    with connect() as db:
        db.execute(
            "INSERT INTO continue_watching(profile_id, provider, media_type, external_id, title, artwork, position_seconds, duration_seconds, payload_json, updated_at) "
            "VALUES(?,?,?,?,?,?,?,?,?,?) "
            "ON CONFLICT(profile_id, provider, media_type, external_id) DO UPDATE SET title=excluded.title, artwork=excluded.artwork, position_seconds=excluded.position_seconds, duration_seconds=excluded.duration_seconds, payload_json=excluded.payload_json, updated_at=excluded.updated_at",
            (profile_id, provider, media_type, external_id, title, artwork, int(position_seconds), int(duration_seconds), json.dumps(payload or {}, ensure_ascii=False), now),
        )


def list_continue(profile_id, provider=None):
    """Lista itens de continuar assistindo."""
    sql = "SELECT * FROM continue_watching WHERE profile_id=?"
    params = [profile_id]
    if provider:
        sql += " AND provider=?"
        params.append(provider)
    sql += " ORDER BY updated_at DESC LIMIT 100"
    with connect() as db:
        return [dict(r) for r in db.execute(sql, params)]


def index_item(table, provider, external_id, category_id, title, artwork="", payload=None):
    """Indexa item em tabela permitida."""
    if table not in ("indexed_channels", "indexed_movies", "indexed_series"):
        raise ValueError("Tabela de índice inválida")
    now = int(time.time())
    with connect() as db:
        db.execute(
            "INSERT INTO " + table + "(provider, external_id, category_id, title, artwork, payload_json, updated_at) "
            "VALUES(?,?,?,?,?,?,?) ON CONFLICT(provider, external_id) DO UPDATE SET category_id=excluded.category_id, title=excluded.title, artwork=excluded.artwork, payload_json=excluded.payload_json, updated_at=excluded.updated_at",
            (provider, str(external_id), str(category_id or ""), title, artwork, json.dumps(payload or {}, ensure_ascii=False), now),
        )
