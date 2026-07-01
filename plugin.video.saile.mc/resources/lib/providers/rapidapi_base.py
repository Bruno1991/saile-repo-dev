# -*- coding: utf-8 -*-
"""Base client para RapidAPI."""

from __future__ import absolute_import

from providers.http_client import get_json
from settings import rapidapi_config

def request_rapidapi(host, endpoint, params=None):
    cfg = rapidapi_config()
    if not cfg or not cfg.get("key"):
        return None
        
    headers = {
        "x-rapidapi-key": cfg["key"],
        "x-rapidapi-host": host
    }
    url = "https://" + host + endpoint
    return get_json(url, params=params or {}, headers=headers, timeout=25)
