from __future__ import annotations

from urllib.parse import urlencode, urlsplit, urlunsplit

from stv.infrastructure.http import HttpClient


class XtreamClient:
    def __init__(self, host: str, username: str, password: str, http: HttpClient | None = None) -> None:
        self.host = self._normalize_host(host)
        self.username = username.strip()
        self.password = password
        self.http = http or HttpClient()

    @staticmethod
    def _normalize_host(host: str) -> str:
        value = host.strip().rstrip("/")
        if not value:
            raise ValueError("Servidor Xtream não configurado")
        if not value.startswith(("http://", "https://")):
            value = "http://" + value
        parts = urlsplit(value)
        return urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip("/"), "", ""))

    def request(self, action: str, **params: object) -> object:
        query = {
            "username": self.username,
            "password": self.password,
            "action": action,
            **{key: value for key, value in params.items() if value is not None},
        }
        return self.http.get_json(f"{self.host}/player_api.php?{urlencode(query)}")

    def get_live_categories(self) -> list[dict[str, object]]:
        res = self.request("get_live_categories")
        return res if isinstance(res, list) else []

    def get_live_streams(self) -> list[dict[str, object]]:
        res = self.request("get_live_streams")
        return res if isinstance(res, list) else []

    def get_vod_categories(self) -> list[dict[str, object]]:
        res = self.request("get_vod_categories")
        return res if isinstance(res, list) else []

    def get_vod_streams(self) -> list[dict[str, object]]:
        res = self.request("get_vod_streams")
        return res if isinstance(res, list) else []

    def get_series_categories(self) -> list[dict[str, object]]:
        res = self.request("get_series_categories")
        return res if isinstance(res, list) else []

    def get_series(self) -> list[dict[str, object]]:
        res = self.request("get_series")
        return res if isinstance(res, list) else []

    def stream_url(self, media_type: str, stream_id: str, extension: str = "") -> str:
        roots = {"live": "live", "vod": "movie", "series": "series"}
        root = roots.get(media_type, "live")
        ext = extension.lstrip(".") or ("ts" if media_type == "live" else "mp4")
        return f"{self.host}/{root}/{self.username}/{self.password}/{stream_id}.{ext}"
