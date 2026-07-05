from __future__ import annotations

import time
from typing import Callable, Dict
from urllib.parse import parse_qs, urlencode

import xbmcgui
import xbmcplugin

from .config import load_config
from .database import record_playback
from .logging_adapter import error, info
from .models import VideoItem
from .ui import resolve_failure, resolve_playback, show_home


def build_url(base_url: str, action: str, **params: str) -> str:
    query = {"action": action}
    query.update(params)
    return f"{base_url}?{urlencode(query)}"


def parse_params(raw_query: str) -> Dict[str, str]:
    parsed = parse_qs(raw_query.lstrip("?"), keep_blank_values=True)
    return {key: values[-1] for key, values in parsed.items()}


def _home(handle: int, base_url: str, params: Dict[str, str]) -> None:
    config = load_config()
    items = []
    if config.demo_url:
        items.append(
            VideoItem(
                item_id="configured-demo",
                title="Vídeo configurado pelo usuário",
                plot="A URL de mídia foi definida nas configurações do add-on.",
                stream_url=config.demo_url,
            )
        )
    else:
        xbmcgui.Dialog().notification(
            "SAILE Reference",
            "Configure uma URL MP4 autorizada nas configurações.",
            xbmcgui.NOTIFICATION_INFO,
            5000,
        )
    show_home(handle, base_url, build_url, items)


def _play(handle: int, base_url: str, params: Dict[str, str]) -> None:
    item_id = params.get("item_id", "")
    config = load_config()
    if item_id != "configured-demo" or not config.demo_url:
        resolve_failure(handle, "Fonte de reprodução indisponível.")
        return

    record_playback(item_id, "Vídeo configurado pelo usuário", int(time.time()))
    resolve_playback(handle, config.demo_url)


Route = Callable[[int, str, Dict[str, str]], None]
ROUTES: Dict[str, Route] = {
    "home": _home,
    "play": _play,
}


def dispatch(argv: list[str]) -> None:
    if len(argv) < 2:
        raise RuntimeError("O plugin precisa ser executado pelo Kodi.")

    base_url = argv[0]
    handle = int(argv[1])
    raw_query = argv[2] if len(argv) > 2 else ""
    params = parse_params(raw_query)
    action = params.get("action") or "home"
    route = ROUTES.get(action)

    if route is None:
        error(f"Action desconhecida: {action!r}")
        xbmcplugin.endOfDirectory(handle, succeeded=False)
        return

    info(f"Executando action={action}")
    try:
        route(handle, base_url, params)
    except Exception as exc:
        error(f"Falha inesperada em action={action}: {exc}")
        if action == "play":
            resolve_failure(handle, "Não foi possível iniciar a reprodução.")
        else:
            xbmcgui.Dialog().notification(
                "SAILE Reference",
                "Não foi possível carregar o conteúdo.",
                xbmcgui.NOTIFICATION_ERROR,
                5000,
            )
            xbmcplugin.endOfDirectory(handle, succeeded=False)
        raise
