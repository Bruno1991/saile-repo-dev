# -*- coding: utf-8 -*-
"""Provider Torrent Search via RapidAPI."""

from __future__ import absolute_import
from providers.rapidapi_base import request_rapidapi

HOST = "torrent-search.p.rapidapi.com"

def releases():
    """Retorna lançamentos/populares."""
    data = request_rapidapi(HOST, "/popular", {})
    return _parse(data)

def search(query):
    data = request_rapidapi(HOST, "/search", {"query": query})
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
            "id": str(m.get("info_hash") or m.get("id") or m.get("link", "")),
            "title": m.get("title") or m.get("name") or "Torrent",
            "type": "video",
            "year": "",
            "plot": m.get("category", ""),
            "artwork": "",
            "play_url": m.get("magnet") or m.get("download_url") or "",
            "tmdb_rating": "",
            "payload": m
        })
    return out

def playback_url(item):
    return item.get("play_url") or ""
