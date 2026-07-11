from __future__ import annotations

from typing import TYPE_CHECKING

from sfy.domain.models import Track

if TYPE_CHECKING:
    from sfy.persistence.database import Database


class MusicRepository:
    def __init__(self, db: Database) -> None:
        self.db = db

    def upsert_tracks(self, tracks: list[Track]) -> None:
        with self.db.connect() as conn:
            for track in tracks:
                conn.execute(
                    """INSERT INTO tracks (track_id, title, artist, album, thumbnail, webpage_url, duration, updated_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                       ON CONFLICT(track_id) DO UPDATE SET
                       title=excluded.title,
                       artist=excluded.artist,
                       album=excluded.album,
                       thumbnail=excluded.thumbnail,
                       webpage_url=excluded.webpage_url,
                       duration=excluded.duration,
                       updated_at=CURRENT_TIMESTAMP
                    """,
                    (track.track_id, track.title, track.artist, track.album, track.thumbnail, track.webpage_url, track.duration)
                )

    def get_track(self, track_id: str) -> Track | None:
        with self.db.connect() as conn:
            row = conn.execute("SELECT * FROM tracks WHERE track_id = ?", (track_id,)).fetchone()
            if row:
                return Track(
                    track_id=row["track_id"],
                    title=row["title"],
                    artist=row["artist"],
                    album=row["album"],
                    thumbnail=row["thumbnail"],
                    webpage_url=row["webpage_url"],
                    duration=row["duration"]
                )
        return None

    def log_playback(self, track_id: str) -> None:
        with self.db.connect() as conn:
            conn.execute("INSERT INTO playback_history (track_id) VALUES (?)", (track_id,))

    def get_history(self, limit: int = 50) -> list[Track]:
        with self.db.connect() as conn:
            rows = conn.execute(
                """SELECT t.* FROM tracks t
                   JOIN playback_history p ON t.track_id = p.track_id
                   ORDER BY p.played_at DESC LIMIT ?
                """,
                (limit,)
            ).fetchall()
            
            tracks = []
            for row in rows:
                tracks.append(Track(
                    track_id=row["track_id"],
                    title=row["title"],
                    artist=row["artist"],
                    album=row["album"],
                    thumbnail=row["thumbnail"],
                    webpage_url=row["webpage_url"],
                    duration=row["duration"]
                ))
            return tracks

    def get_playlists(self) -> list[dict]:
        with self.db.connect() as conn:
            rows = conn.execute("SELECT * FROM playlists ORDER BY name").fetchall()
            return [{"playlist_id": r["playlist_id"], "name": r["name"]} for r in rows]

    def create_playlist(self, name: str) -> None:
        with self.db.connect() as conn:
            conn.execute("INSERT OR IGNORE INTO playlists (name) VALUES (?)", (name,))

    def add_track_to_playlist(self, playlist_id: int, track_id: str) -> None:
        with self.db.connect() as conn:
            pos_row = conn.execute("SELECT MAX(position) as m FROM playlist_tracks WHERE playlist_id = ?", (playlist_id,)).fetchone()
            next_pos = (pos_row["m"] or 0) + 1
            conn.execute("INSERT OR IGNORE INTO playlist_tracks (playlist_id, track_id, position) VALUES (?, ?, ?)", (playlist_id, track_id, next_pos))

    def get_playlist_tracks(self, playlist_id: int) -> list[Track]:
        with self.db.connect() as conn:
            rows = conn.execute(
                """SELECT t.* FROM tracks t
                   JOIN playlist_tracks pt ON t.track_id = pt.track_id
                   WHERE pt.playlist_id = ?
                   ORDER BY pt.position
                """,
                (playlist_id,)
            ).fetchall()
            tracks = []
            for row in rows:
                tracks.append(Track(
                    track_id=row["track_id"],
                    title=row["title"],
                    artist=row["artist"],
                    album=row["album"],
                    thumbnail=row["thumbnail"],
                    webpage_url=row["webpage_url"],
                    duration=row["duration"]
                ))
            return tracks
