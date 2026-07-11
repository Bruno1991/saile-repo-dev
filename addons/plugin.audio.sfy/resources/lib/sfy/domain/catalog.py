from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from sfy.domain.models import Track

if TYPE_CHECKING:
    from sfy.persistence.repository import MusicRepository


class CatalogOrchestrator:
    def __init__(self, repo: MusicRepository) -> None:
        self.repo = repo

    def search_and_cache(self, ytm_client: 'YtmClient', query: str) -> list[Track]:
        import xbmcgui
        dialog = xbmcgui.DialogProgress()
        dialog.create("sFy", "Buscando no YouTube Music...")
        
        try:
            raw_results = ytm_client.search_songs(query, limit=20)
            
            tracks = []
            for raw in raw_results:
                tracks.append(Track(
                    track_id=raw["track_id"],
                    title=raw["title"],
                    artist=raw["artist"],
                    album=raw["album"],
                    thumbnail=raw["thumbnail"],
                    webpage_url=raw["webpage_url"],
                    duration=raw["duration"]
                ))
                
            # Cache in SQLite
            self.repo.upsert_tracks(tracks)
            return tracks
        finally:
            dialog.close()

    def get_history(self) -> list[Track]:
        return self.repo.get_history()
