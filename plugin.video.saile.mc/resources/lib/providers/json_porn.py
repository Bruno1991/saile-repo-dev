# -*- coding: utf-8 -*-
"""Provider JSON Porn via RapidAPI."""

from __future__ import absolute_import
from providers.rapidapi_base import request_rapidapi

HOST = "json-porn.p.rapidapi.com"

def releases():
    """Retorna lançamentos (latest)."""
    data = request_rapidapi(HOST, "/videos/latest", {"limit": "25"})
    return _parse(data)

def search(query):
    data = request_rapidapi(HOST, "/videos/search", {"q": query, "limit": "25"})
    return _parse(data)

def _parse(data):
    if not isinstance(data, dict):
        return []
    items = data.get("videos") or data.get("items") or []
    out = []
    for m in items:
        out.append({
            "id": str(m.get("id", "") or m.get("url", "")),
            "title": m.get("title", "Video"),
            "type": "video",
            "year": "",
            "plot": m.get("description", ""),
            "artwork": m.get("thumb") or m.get("thumbnail") or m.get("cover") or "",
            "play_url": m.get("video_url") or m.get("embed_url") or m.get("url") or "",
            "tmdb_rating": "",
            "payload": m
        })
    return out

def playback_url(item):
    return item.get("play_url") or ""
