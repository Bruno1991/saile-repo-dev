from __future__ import annotations

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class HttpClient:
    def __init__(self, timeout: float = 15.0, user_agent: str = "sTv/0.1") -> None:
        self.timeout = timeout
        self.user_agent = user_agent

    def get_json(self, url: str, headers: dict[str, str] | None = None) -> object:
        request_headers = {"User-Agent": self.user_agent, **(headers or {})}
        request = Request(url, headers=request_headers, method="GET")
        try:
            with urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, ValueError) as exc:
            raise RuntimeError("Falha ao consultar serviço remoto") from exc
