# -*- coding: utf-8 -*-
"""Provider YTS.am via RapidAPI."""

from __future__ import absolute_import
from providers.rapidapi_base import request_rapidapi

HOST = "yts-am-torrent.p.rapidapi.com"

def releases():
    """Retorna lançamentos."""
    data = request_rapidapi(HOST, "/list_movies.json", {"limit": "25", "sort_by": "date_added"})
    return _parse(data)

def search(query):
    data = request_rapidapi(HOST, "/list_movies.json", {"query_term": query, "limit": "25"})
    return _parse(data)

def _parse(data):
    if not isinstance(data, dict):
        return []
    movies = data.get("data", {}).get("movies", [])
    out = []
    for m in movies:
        # Pega o primeiro torrent magnet ou constrói
        torrents = m.get("torrents", [])
        magnet = ""
        if torrents:
            magnet = "magnet:?xt=urn:btih:" + torrents[0].get("hash", "")
            
        out.append({
            "id": str(m.get("id", "")),
            "title": m.get("title", "Filme"),
            "type": "movie",
            "year": str(m.get("year", "")),
            "plot": m.get("summary", ""),
            "artwork": m.get("medium_cover_image", ""),
            "play_url": magnet,
            "tmdb_rating": str(m.get("rating", "")),
            "payload": m
        })
    return out

def playback_url(item):
    return item.get("play_url") or ""
