from __future__ import annotations

import json
import urllib.parse
import urllib.request
from typing import Any


class TmdbClient:
    def __init__(self, bearer_token: str, language: str = "pt-BR"):
        self.bearer_token = bearer_token
        self.language = language
        self.base_url = "https://api.themoviedb.org/3"

    def _request(self, endpoint: str, params: dict[str, str] | None = None) -> dict[str, Any]:
        if not self.bearer_token:
            return {}
            
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        query_params = {"language": self.language}
        if params:
            query_params.update(params)
            
        query_string = urllib.parse.urlencode(query_params)
        full_url = f"{url}?{query_string}"
        
        req = urllib.request.Request(full_url)
        req.add_header("Authorization", f"Bearer {self.bearer_token}")
        req.add_header("accept", "application/json")
        
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception:
            return {}

    def search_movie(self, title: str, year: str = "") -> dict[str, Any] | None:
        params = {"query": title}
        if year:
            params["primary_release_year"] = year
        data = self._request("search/movie", params)
        results = data.get("results", [])
        if results:
            return results[0]
        return None

    def search_tv(self, title: str, year: str = "") -> dict[str, Any] | None:
        params = {"query": title}
        if year:
            params["first_air_date_year"] = year
        data = self._request("search/tv", params)
        results = data.get("results", [])
        if results:
            return results[0]
        return None
