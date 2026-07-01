# -*- coding: utf-8 -*-
"""HTTP simples com biblioteca padrão."""

from __future__ import absolute_import

import json
import urllib.parse
import urllib.request

from kodi import warning

USER_AGENT = "SaileMediaCenter/0.1.0 Kodi"


def get_json(url, params=None, headers=None, timeout=20):
    """Faz GET JSON com timeout e tratamento de erro."""
    if params:
        sep = "&" if "?" in url else "?"
        url = url + sep + urllib.parse.urlencode(params)
    req_headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode("utf-8", "replace")
        return json.loads(data)
    except Exception as exc:
        warning("Falha HTTP JSON: %s" % exc)
        return None
