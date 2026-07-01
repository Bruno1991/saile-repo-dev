# -*- coding: utf-8 -*-
"""Provider Xtream Codes API para SaileTV."""

from __future__ import absolute_import

import urllib.parse

from providers.http_client import get_json
from settings import require_xtream, xtream_config
import storage

PROVIDER = "xtream"


def _normalize_host(host):
    if not host:
        return ""
    if not host.startswith(("http://", "https://")):
        host = "http://" + host
    return host.rstrip("/")


def _api(action=None, extra=None):
    cfg = require_xtream()
    if not cfg:
        return None
    params = {
        "username": cfg["username"],
        "password": cfg["password"],
    }
    if action:
        params["action"] = action
    if extra:
        params.update(extra)
    url = _normalize_host(cfg["host"]) + "/player_api.php"
    return get_json(url, params=params, timeout=25)


def categories(kind):
    """Lista categorias live, vod ou series."""
    action = {
        "live": "get_live_categories",
        "vod": "get_vod_categories",
        "series": "get_series_categories",
    }.get(kind)
    if not action:
        return []
    data = _api(action)
    return data if isinstance(data, list) else []


def items(kind, category_id=""):
    """Lista itens do Xtream por tipo."""
    action = {
        "live": "get_live_streams",
        "vod": "get_vod_streams",
        "series": "get_series",
    }.get(kind)
    if not action:
        return []
    extra = {}
    if category_id:
        extra["category_id"] = category_id
    data = _api(action, extra)
    return data if isinstance(data, list) else []


def series_info(series_id):
    """Obtém detalhes da série, temporadas e episódios."""
    data = _api("get_series_info", {"series_id": series_id})
    return data if isinstance(data, dict) else {}


def search(kind, query):
    """Busca local simples a partir dos itens retornados por categoria geral."""
    query_norm = (query or "").lower().strip()
    if not query_norm:
        return []
    results = []
    for item in items(kind):
        name = (item.get("name") or item.get("title") or "").lower()
        if query_norm in name:
            results.append(item)
    return results[:200]


def playback_url(kind, item):
    """Monta URL de reprodução Xtream."""
    cfg = xtream_config()
    host = _normalize_host(cfg["host"])
    user = urllib.parse.quote(cfg["username"])
    password = urllib.parse.quote(cfg["password"])
    if kind == "live":
        stream_id = item.get("stream_id") or item.get("id")
        return "%s/live/%s/%s/%s.ts" % (host, user, password, stream_id)
    if kind == "vod":
        stream_id = item.get("stream_id") or item.get("id")
        ext = item.get("container_extension") or "mp4"
        return "%s/movie/%s/%s/%s.%s" % (host, user, password, stream_id, ext)
    if kind == "episode":
        stream_id = item.get("id") or item.get("stream_id")
        ext = item.get("container_extension") or item.get("ext") or "mp4"
        return "%s/series/%s/%s/%s.%s" % (host, user, password, stream_id, ext)
    return ""


def index_all():
    """Indexa conteúdo principal do Xtream no SQLite local."""
    count = 0
    for item in items("live"):
        external_id = item.get("stream_id") or item.get("id")
        if external_id:
            storage.index_item("indexed_channels", PROVIDER, external_id, item.get("category_id"), item.get("name") or "Canal", item.get("stream_icon") or "", item)
            count += 1
    for item in items("vod"):
        external_id = item.get("stream_id") or item.get("id")
        if external_id:
            storage.index_item("indexed_movies", PROVIDER, external_id, item.get("category_id"), item.get("name") or "Filme", item.get("stream_icon") or item.get("cover") or "", item)
            count += 1
    for item in items("series"):
        external_id = item.get("series_id") or item.get("id")
        if external_id:
            storage.index_item("indexed_series", PROVIDER, external_id, item.get("category_id"), item.get("name") or "Série", item.get("cover") or "", item)
            count += 1
    return count
