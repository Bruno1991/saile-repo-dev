from __future__ import annotations

from urllib.parse import urlencode

from stv.infrastructure.http import HttpClient


class TmdbClient:
    API_BASE = "https://api.themoviedb.org/3"
    IMAGE_BASE = "https://image.tmdb.org/t/p/original"

    def __init__(self, bearer_token: str, language: str = "pt-BR", http: HttpClient | None = None) -> None:
        self.token = bearer_token.strip()
        self.language = language
        self.http = http or HttpClient(user_agent="sTv-TMDB/0.1")

    def search(self, media_type: str, query: str, year: int | None = None) -> object:
        if media_type not in {"movie", "tv"}:
            raise ValueError("Tipo TMDB inválido")
        params = {"query": query, "language": self.language, "include_adult": "false"}
        if year:
            params["year" if media_type == "movie" else "first_air_date_year"] = str(year)
        headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}
        return self.http.get_json(f"{self.API_BASE}/search/{media_type}?{urlencode(params)}", headers)

    @classmethod
    def image_url(cls, path: str) -> str:
        return f"{cls.IMAGE_BASE}{path}" if path else ""
