# -*- coding: utf-8 -*-
"""Integração com TMDB API para metadados em alta definição."""

from __future__ import absolute_import
import re
from concurrent.futures import ThreadPoolExecutor
from providers.http_client import get_json
from settings import rapidapi_config
from kodi import xbmc

def get_metadata(title, year=""):
    cfg = rapidapi_config()
    key = cfg.get("tmdb_key")
    if not key:
        return {}
        
    params = {"api_key": key, "query": title, "language": "pt-BR"}
    if year:
        # Tenta usar o ano para melhorar a precisão
        params["primary_release_year"] = year
        
    url = "https://api.themoviedb.org/3/search/multi"
    data = get_json(url, params=params, timeout=5)
    
    if data and data.get("results"):
        # Pega o primeiro resultado (maior relevância)
        res = data["results"][0]
        poster = res.get("poster_path")
        plot = res.get("overview") or ""
        artwork = "https://image.tmdb.org/t/p/w500" + poster if poster else ""
        return {"artwork": artwork, "plot": plot}
    return {}

def _clean_title(title):
    """Limpa o título de torrent para melhorar a busca no TMDB."""
    # Remove textos entre parênteses ou colchetes
    t = re.sub(r'[\(\[].*?[\)\]]', '', title)
    # Corta a string antes de resoluções ou fontes
    t = re.split(r'(1080p|720p|2160p|4k|BluRay|WEB-DL|HDR|HD)', t, flags=re.IGNORECASE)[0]
    # Substitui pontos por espaço
    t = t.replace(".", " ").replace("-", " ").strip()
    return t

def _enrich_single(item):
    if item.get("title"):
        clean_title = _clean_title(item["title"])
        if clean_title:
            try:
                meta = get_metadata(clean_title, item.get("year", ""))
                if meta.get("artwork"):
                    item["artwork"] = meta["artwork"]
                if meta.get("plot"):
                    item["plot"] = meta["plot"]
            except Exception as e:
                xbmc.log("[Saile] Erro no TMDB para %s: %s" % (clean_title, e), xbmc.LOGWARNING)
    return item

def enrich_items(items):
    """Enriquece uma lista de itens com capas e sinopses do TMDB em paralelo."""
    if not items:
        return items
        
    # Executa as chamadas ao TMDB em até 10 threads simultâneas
    with ThreadPoolExecutor(max_workers=10) as executor:
        enriched = list(executor.map(_enrich_single, items))
        
    return enriched
