# -*- coding: utf-8 -*-
"""Provider ThePirateBay via RapidAPI."""

from __future__ import absolute_import
from providers.rapidapi_base import request_rapidapi

HOST = "thepiratebay.p.rapidapi.com"

def releases():
    """Retorna recentes (Top 100 Video)."""
    # 200 = Video
    data = request_rapidapi(HOST, "/top/200", {})
    return _parse(data)

def search(query):
    data = request_rapidapi(HOST, "/search/" + query + "/1/99/0", {})
    return _parse(data)

def _parse(data):
    if not isinstance(data, list):
        if isinstance(data, dict):
            data = data.get("results") or data.get("items") or []
        else:
            return []
            
    out = []
    for m in data:
        out.append({
            "id": str(m.get("id") or m.get("info_hash", "")),
            "title": m.get("name") or m.get("title") or "Torrent",
            "type": "video",
            "year": "",
            "plot": "Seeders: %s / Leechers: %s" % (m.get("seeders", 0), m.get("leechers", 0)),
            "artwork": "",
            "play_url": m.get("magnet") or m.get("magnet_uri") or "",
            "tmdb_rating": "",
            "payload": m
        })
    return out

def playback_url(item):
    return item.get("play_url") or ""
