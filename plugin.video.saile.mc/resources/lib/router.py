# -*- coding: utf-8 -*-
"""Router principal do Saile Media Center."""

from __future__ import absolute_import

import json
import sys
import urllib.parse

from kodi import xbmcgui, xbmcplugin, notify, error
import profiles
import settings
import storage
import ui
from providers import xtream, youtube, yts_am, json_porn, torrent_search, the_pirate_bay


def _parse(argv):
    base_url = argv[0] if argv else "plugin://plugin.video.saile.mc"
    handle = int(argv[1]) if len(argv) > 1 else 1
    query = argv[2][1:] if len(argv) > 2 and argv[2].startswith("?") else ""
    params = dict((k, v[0]) for k, v in urllib.parse.parse_qs(query).items())
    return base_url, handle, params


def run(argv=None):
    """Executa action do addon."""
    argv = argv or sys.argv
    base_url, handle, params = _parse(argv)
    profiles.bootstrap()
    action = params.get("action", "profiles")
    try:
        dispatch(base_url, handle, action, params)
    except Exception as exc:
        error("Erro na rota %s: %s" % (action, exc))
        notify("Erro ao abrir rota. Voltando ao início.", "error")
        show_profiles(base_url, handle)


def dispatch(base_url, handle, action, params):
    routes = {
        "profiles": show_profiles,
        "select_profile": select_profile,
        "settings_menu": show_settings,
        "sync_menu": sync_menu,
        "set_pin": set_pin,
        "set_xtream": set_xtream,
        "manage_profiles": manage_profiles,
        "create_profile": create_profile,
        "home": show_home,
        "favorites": show_favorites,
        "continue": show_continue,
        "sailetv": show_sailetv,
        "sailetv_categories": show_sailetv_categories,
        "sailetv_items": show_sailetv_items,
        "sailetv_series_info": show_sailetv_series_info,
        "sailetv_search": sailetv_search,
        "sailetv_index": sailetv_index,
        "sailefy": show_sailefy,
        "sailefy_search": sailefy_search,
        "sailefy_top_br": sailefy_top_br,
        "sailefy_top_world": sailefy_top_world,
        "sailefy_category": sailefy_category,
        "sailefy_playlists": sailefy_playlists,
        "add_to_playlist": add_to_playlist,
        "create_playlist": create_playlist_route,
        "show_playlist_items": show_playlist_items,
        "storrent": show_storrent,
        "storrent_provider_menu": storrent_provider_menu,
        "storrent_releases": storrent_releases,
        "storrent_search": storrent_search,
        "play": play,
        "save_favorite": save_favorite,
    }
    
    if action == "sync_server":
        from lib import sync_network
        sync_network.server_sync()
        return

    func = routes.get(action, show_profiles)
    return func(base_url, handle, params) if func not in (show_profiles, manage_profiles, show_settings) else func(base_url, handle)


def _profile(params):
    return profiles.get(params.get("profile_id", ""))


def _require_profile(params):
    p = _profile(params)
    if not p:
        notify("Selecione um perfil.", "warning")
    return p


def show_profiles(base_url, handle):
    """Tela principal Adulto/Kids/Configurações."""
    for p in profiles.list_all():
        icon = "adult.png" if p["kind"] == "adult" else "kids.png"
        ui.add_directory(handle, base_url, p["name"], "select_profile", icon, {"profile_id": p["id"]})
    ui.add_directory(handle, base_url, "Configurações", "settings_menu", "settings.png")
    ui.end(handle)


def show_settings(base_url, handle, params=None):
    """Submenu de configurações gerais."""
    ui.add_directory(handle, base_url, "Sync (Rede Local)", "sync_menu", "settings.png")
    ui.add_directory(handle, base_url, "Controle dos Pais (PIN)", "set_pin", "settings.png")
    ui.add_directory(handle, base_url, "Dados Xtream", "set_xtream", "settings.png")
    ui.add_directory(handle, base_url, "Gerenciar Perfis", "manage_profiles", "profiles.png")
    ui.end(handle)


def set_pin(base_url, handle, params=None):
    if not profiles.verify_pin_if_needed():
        show_settings(base_url, handle)
        return
    import xbmcgui, xbmcaddon
    pin = xbmcgui.Dialog().numeric(0, "Novo PIN (4-6 dígitos)", "")
    if pin and len(pin) >= 4 and len(pin) <= 6:
        xbmcaddon.Addon().setSetting("parent_pin", pin)
        notify("PIN atualizado.")
    elif pin:
        notify("PIN inválido. Deve ter 4-6 dígitos.", "error")
    show_settings(base_url, handle)


def set_xtream(base_url, handle, params=None):
    if not profiles.verify_pin_if_needed():
        show_settings(base_url, handle)
        return
    import xbmcgui, xbmcaddon
    addon = xbmcaddon.Addon()
    host = xbmcgui.Dialog().input("Host URL (Ex: http://ip:porta)", addon.getSetting("xtream_host"))
    if host:
        user = xbmcgui.Dialog().input("Usuário", addon.getSetting("xtream_username"))
        pwd = xbmcgui.Dialog().input("Senha", addon.getSetting("xtream_password"))
        addon.setSetting("xtream_host", host)
        addon.setSetting("xtream_username", user)
        addon.setSetting("xtream_password", pwd)
        notify("Dados Xtream salvos.")
    show_settings(base_url, handle)


def sync_menu(base_url, handle, params=None):
    if not profiles.verify_pin_if_needed():
        show_settings(base_url, handle)
        return
    import xbmcgui
    idx = xbmcgui.Dialog().select("Sincronizar", ["Enviar dados (Servidor)", "Receber dados (Cliente)"])
    if idx == 0:
        import xbmc
        xbmc.executebuiltin('RunScript(plugin.video.saile.mc, ?action=sync_server)')
    elif idx == 1:
        from lib import sync_network
        sync_network.client_sync(None)
    show_settings(base_url, handle)


def select_profile(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        show_profiles(base_url, handle)
        return
    if p.get("kind") == "adult" and not profiles.verify_pin_if_needed():
        show_profiles(base_url, handle)
        return
    show_home(base_url, handle, {"profile_id": p["id"]})


def manage_profiles(base_url, handle, params=None):
    """Menu de gerenciamento de perfis."""
    if not profiles.verify_pin_if_needed():
        show_settings(base_url, handle)
        return
    ui.add_directory(handle, base_url, "Criar perfil", "create_profile", "profiles.png")
    for p in profiles.list_all():
        ui.add_directory(handle, base_url, "Perfil: " + p["name"], "select_profile", "profiles.png", {"profile_id": p["id"]})
    ui.end(handle)


def create_profile(base_url, handle, params):
    if not profiles.verify_pin_if_needed():
        show_settings(base_url, handle)
        return
    import xbmcgui
    name = xbmcgui.Dialog().input("Nome do perfil")
    if name:
        storage.save_profile(name.strip(), "adult", "art/adult.png")
        notify("Perfil criado.")
    manage_profiles(base_url, handle)


def show_home(base_url, handle, params):
    """Home do perfil."""
    p = _require_profile(params)
    if not p:
        show_profiles(base_url, handle)
        return
    ui.add_directory(handle, base_url, "SaileTV (xTream)", "sailetv", "app_sailetv.png", {"profile_id": p["id"]})
    if profiles.profile_allows(p, "storrent"):
        ui.add_directory(handle, base_url, "sTorrent (Torrents e APIs)", "storrent", "app_storrent.png", {"profile_id": p["id"]})
    if profiles.profile_allows(p, "sailefy"):
        ui.add_directory(handle, base_url, "SaileFy (stream de músicas)", "sailefy", "app_sailefy.png", {"profile_id": p["id"]})
    ui.end(handle)


def show_favorites(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        return show_profiles(base_url, handle)
    for fav in storage.list_favorites(p["id"]):
        payload = _payload(fav.get("payload_json"))
        play_url = payload.get("play_url") or payload.get("url") or ""
        if play_url:
            ui.add_playable(handle, base_url, fav["title"], "play", play_url, fav.get("artwork") or "favorites.png", {"profile_id": p["id"]}, {"title": fav["title"]})
        else:
            ui.add_directory(handle, base_url, fav["title"], "favorites", "favorites.png", {"profile_id": p["id"]})
    ui.end(handle)


def show_continue(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        return show_profiles(base_url, handle)
    for item in storage.list_continue(p["id"]):
        payload = _payload(item.get("payload_json"))
        play_url = payload.get("play_url") or payload.get("url") or ""
        if play_url:
            ui.add_playable(handle, base_url, item["title"], "play", play_url, item.get("artwork") or "continue.png", {"profile_id": p["id"]}, {"title": item["title"]})
    ui.end(handle)


def show_sailetv(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        return show_profiles(base_url, handle)
    ui.add_directory(handle, base_url, "TV ao vivo", "sailetv_categories", "live.png", {"profile_id": p["id"], "kind": "live"})
    ui.add_directory(handle, base_url, "VOD", "sailetv_categories", "vod.png", {"profile_id": p["id"], "kind": "vod"})
    ui.add_directory(handle, base_url, "Séries", "sailetv_categories", "series.png", {"profile_id": p["id"], "kind": "series"})
    ui.end(handle)


def show_sailetv_categories(base_url, handle, params):
    p = _require_profile(params)
    kind = params.get("kind", "live")
    if not p:
        return show_profiles(base_url, handle)
    ui.add_directory(handle, base_url, "Busca", "sailetv_search", "search.png", {"profile_id": p["id"], "kind": kind})
    ui.add_directory(handle, base_url, "Favoritos", "favorites", "favorites.png", {"profile_id": p["id"], "provider": "xtream", "media_type": kind})
    
    cats = xtream.categories(kind)
    keywords = [x.strip().lower() for x in settings.get_setting("kids_category_keywords", "kids,infantil").split(",")]
    for cat in cats:
        name = cat.get("category_name") or cat.get("name") or "Categoria"
        if p.get("kind") == "kids" and kind in ("live", "vod", "series"):
            if not any(k and k in name.lower() for k in keywords):
                continue
        cid = cat.get("category_id") or cat.get("id") or ""
        ui.add_directory(handle, base_url, name, "sailetv_items", "categories.png", {"profile_id": p["id"], "kind": kind, "category_id": cid})
    ui.end(handle)


def show_sailetv_items(base_url, handle, params):
    p = _require_profile(params)
    kind = params.get("kind", "live")
    category_id = params.get("category_id", "")
    if not p:
        return show_profiles(base_url, handle)
    for item in xtream.items(kind, category_id):
        title = item.get("name") or item.get("title") or "Item"
        artwork = item.get("stream_icon") or item.get("cover") or ("live.png" if kind == "live" else "vod.png")
        if kind == "series":
            sid = item.get("series_id") or item.get("id") or ""
            ui.add_directory(handle, base_url, title, "sailetv_series_info", artwork if artwork.startswith("http") else "series.png", {"profile_id": p["id"], "series_id": sid})
        else:
            play_url = xtream.playback_url(kind, item)
            ui.add_playable(handle, base_url, title, "play", play_url, artwork if artwork else "vod.png", {"profile_id": p["id"], "provider": "xtream", "media_type": kind, "external_id": item.get("stream_id") or item.get("id") or "", "title": title, "artwork": artwork}, {"title": title, "plot": item.get("plot") or ""})
    ui.end(handle)


def show_sailetv_series_info(base_url, handle, params):
    p = _require_profile(params)
    series_id = params.get("series_id", "")
    target_season = params.get("season", "")
    if not p:
        return show_profiles(base_url, handle)
    data = xtream.series_info(series_id)
    episodes = data.get("episodes") or {}
    
    if isinstance(episodes, dict):
        if not target_season:
            # Lista as Temporadas
            for season in sorted(episodes.keys(), key=lambda x: int(x) if str(x).isdigit() else 0):
                ui.add_directory(handle, base_url, "Temporada %s" % season, "sailetv_series_info", "series.png", {"profile_id": p["id"], "series_id": series_id, "season": season})
        else:
            # Lista os Episódios da Temporada
            items = episodes.get(target_season, [])
            for ep in items:
                title = "E%s - %s" % (ep.get("episode_num") or ep.get("id") or "", ep.get("title") or "Episódio")
                play_url = xtream.playback_url("episode", ep)
                ui.add_playable(handle, base_url, title, "play", play_url, "series.png", {"profile_id": p["id"], "provider": "xtream", "media_type": "episode", "external_id": ep.get("id") or "", "title": title, "artwork": "series.png"}, {"title": title, "plot": ep.get("info", {}).get("plot", "") if isinstance(ep.get("info"), dict) else ""})
    ui.end(handle)


def sailetv_search(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        return show_profiles(base_url, handle)
    q = xbmcgui.Dialog().input("Buscar em SaileTV")
    if not q:
        return show_sailetv(base_url, handle, params)
    for kind in ("live", "vod", "series"):
        for item in xtream.search(kind, q):
            title = item.get("name") or "Item"
            if kind == "series":
                sid = item.get("series_id") or item.get("id") or ""
                ui.add_directory(handle, base_url, "Série: " + title, "sailetv_series_info", "series.png", {"profile_id": p["id"], "series_id": sid})
            else:
                play_url = xtream.playback_url(kind, item)
                ui.add_playable(handle, base_url, "%s: %s" % (kind.upper(), title), "play", play_url, "vod.png", {"profile_id": p["id"]}, {"title": title})
    ui.end(handle)


def sailetv_index(base_url, handle, params):
    count = xtream.index_all()
    notify("Conteúdo Xtream indexado: %s itens." % count)
    show_sailetv(base_url, handle, params)


def show_sailefy(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        return show_profiles(base_url, handle)
    if not profiles.profile_allows(p, "sailefy"):
        notify("Perfil Kids não acessa SaileFy.", "warning")
        return show_home(base_url, handle, params)
    ui.add_directory(handle, base_url, "Busca", "sailefy_search", "search.png", {"profile_id": p["id"]})
    ui.add_directory(handle, base_url, "Playlists", "sailefy_playlists", "playlists.png", {"profile_id": p["id"]})
    ui.add_directory(handle, base_url, "Top Brasil", "sailefy_top_br", "top_brazil.png", {"profile_id": p["id"]})
    ui.add_directory(handle, base_url, "Top Mundo", "sailefy_top_world", "top_world.png", {"profile_id": p["id"]})
    ui.add_directory(handle, base_url, "Categorias", "sailefy_category", "categories.png", {"profile_id": p["id"]})
    ui.end(handle)


def _render_youtube_items(base_url, handle, profile_id, items):
    import urllib.parse
    for item in items:
        play_url = youtube.playback_url(item)
        artwork = item.get("artwork") or "app_sailefy.png"
        add_pl_url = ui.build_url(base_url, "add_to_playlist", profile_id=profile_id, external_id=item.get("id", ""), title=item.get("title", ""), artwork=artwork)
        context_menu = [("Adicionar à Playlist", "RunPlugin(%s)" % add_pl_url)]
        ui.add_playable(handle, base_url, item["title"], "play", play_url, artwork, {"profile_id": profile_id, "provider": "youtube", "media_type": "music", "external_id": item.get("id", ""), "title": item["title"], "artwork": artwork}, {"title": item["title"], "plot": item.get("plot") or item.get("channel") or ""}, context_menu)
    ui.end(handle)


def sailefy_search(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        return show_profiles(base_url, handle)
    import xbmcgui
    q = xbmcgui.Dialog().input("Pesquisar Música")
    if not q:
        return show_sailefy(base_url, handle, params)
    _render_youtube_items(base_url, handle, p["id"], youtube.search(q))


def sailefy_top_br(base_url, handle, params):
    p = _require_profile(params)
    _render_youtube_items(base_url, handle, p["id"], youtube.top_brazil())


def sailefy_top_world(base_url, handle, params):
    p = _require_profile(params)
    _render_youtube_items(base_url, handle, p["id"], youtube.top_world())


def sailefy_category(base_url, handle, params):
    p = _require_profile(params)
    import xbmcgui
    q = xbmcgui.Dialog().input("Categoria musical")
    if not q:
        return show_sailefy(base_url, handle, params)
    _render_youtube_items(base_url, handle, p["id"], youtube.category_query(q))


def sailefy_playlists(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        return show_profiles(base_url, handle)
    ui.add_directory(handle, base_url, "Criar Playlist", "create_playlist", "playlists.png", {"profile_id": p["id"]})
    pls = storage.list_playlists(p["id"])
    for pl in pls:
        ui.add_directory(handle, base_url, pl["title"], "show_playlist_items", "playlists.png", {"profile_id": p["id"], "playlist_id": pl["id"]})
    ui.end(handle)


def create_playlist_route(base_url, handle, params):
    p = _require_profile(params)
    if not p: return
    import xbmcgui
    name = xbmcgui.Dialog().input("Nome da Playlist")
    if name:
        storage.create_playlist(p["id"], name.strip())
        notify("Playlist criada.")
    import xbmc
    xbmc.executebuiltin("Container.Refresh")


def show_playlist_items(base_url, handle, params):
    p = _require_profile(params)
    playlist_id = params.get("playlist_id", "")
    items = storage.list_playlist_items(playlist_id)
    for item in items:
        play_url = "sailefy://" + item["external_id"]
        ui.add_playable(handle, base_url, item["title"], "play", play_url, item["artwork"], {"profile_id": p["id"], "provider": "youtube", "media_type": "music", "external_id": item["external_id"], "title": item["title"], "artwork": item["artwork"]}, {"title": item["title"], "plot": ""})
    ui.end(handle)


def add_to_playlist(base_url, handle, params):
    p = _require_profile(params)
    if not p: return
    pls = storage.list_playlists(p["id"])
    if not pls:
        storage.create_playlist(p["id"], "Minha Playlist")
        pls = storage.list_playlists(p["id"])
    
    import xbmcgui
    if len(pls) == 1:
        pl_id = pls[0]["id"]
    else:
        opts = [pl["title"] for pl in pls]
        idx = xbmcgui.Dialog().select("Escolha a Playlist", opts)
        if idx < 0: return
        pl_id = pls[idx]["id"]
    
    storage.add_to_playlist(pl_id, "youtube", "music", params.get("external_id"), params.get("title"), params.get("artwork"))
    notify("Adicionado à Playlist!")


def show_storrent(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        return show_profiles(base_url, handle)
    if not profiles.profile_allows(p, "storrent"):
        notify("Perfil Kids não acessa sTorrent.", "warning")
        return show_home(base_url, handle, params)
    ui.add_directory(handle, base_url, "YTS.am (Filmes)", "storrent_provider_menu", "app_storrent.png", {"profile_id": p["id"], "provider_id": "yts_am"})
    ui.add_directory(handle, base_url, "Torrent Search (Geral)", "storrent_provider_menu", "app_storrent.png", {"profile_id": p["id"], "provider_id": "torrent_search"})
    ui.add_directory(handle, base_url, "ThePirateBay (Geral)", "storrent_provider_menu", "app_storrent.png", {"profile_id": p["id"], "provider_id": "the_pirate_bay"})
    ui.add_directory(handle, base_url, "JSON Porn (+18)", "storrent_provider_menu", "app_storrent.png", {"profile_id": p["id"], "provider_id": "json_porn"})
    ui.add_directory(handle, base_url, "Continuar assistindo (Todos)", "continue", "continue.png", {"profile_id": p["id"], "provider": "storrent"})
    ui.end(handle)


def storrent_provider_menu(base_url, handle, params):
    p = _require_profile(params)
    provider_id = params.get("provider_id", "yts_am")
    ui.add_directory(handle, base_url, "Recentes / Lançamentos", "storrent_releases", "releases.png", {"profile_id": p["id"], "provider_id": provider_id})
    ui.add_directory(handle, base_url, "Buscar", "storrent_search", "search.png", {"profile_id": p["id"], "provider_id": provider_id})
    ui.end(handle)


def _get_provider_mod(provider_id):
    if provider_id == "yts_am": return yts_am
    if provider_id == "json_porn": return json_porn
    if provider_id == "torrent_search": return torrent_search
    if provider_id == "the_pirate_bay": return the_pirate_bay
    return yts_am


def _render_torrent_items(base_url, handle, profile_id, provider_id, items):
    from providers import tmdb
    mod = _get_provider_mod(provider_id)
    items = tmdb.enrich_items(items)
    for item in items:
        play_url = mod.playback_url(item)
        title = item.get("title") or "Item"
        if play_url:
            ui.add_playable(handle, base_url, title, "play", play_url, item.get("artwork") or "app_storrent.png", {"profile_id": profile_id, "provider": "storrent", "media_type": item.get("type", "video"), "external_id": item.get("id", ""), "title": title}, {"title": title, "plot": item.get("plot") or ""})
        else:
            ui.add_directory(handle, base_url, title + " (sem URL)", "storrent", "app_storrent.png", {"profile_id": profile_id})
    ui.end(handle)


def storrent_releases(base_url, handle, params):
    p = _require_profile(params)
    provider_id = params.get("provider_id", "yts_am")
    mod = _get_provider_mod(provider_id)
    _render_torrent_items(base_url, handle, p["id"], provider_id, mod.releases())


def storrent_search(base_url, handle, params):
    p = _require_profile(params)
    provider_id = params.get("provider_id", "yts_am")
    q = xbmcgui.Dialog().input("Buscar torrent")
    if not q:
        return storrent_provider_menu(base_url, handle, params)
    mod = _get_provider_mod(provider_id)
    _render_torrent_items(base_url, handle, p["id"], provider_id, mod.search(q))


def play(base_url, handle, params):
    play_url = params.get("play_url", "")
    title = params.get("title", "Saile")
    if not play_url:
        notify("Item sem URL de reprodução.", "warning")
        xbmcplugin.setResolvedUrl(handle, False, xbmcgui.ListItem(label=title))
        return
        
    if play_url.startswith("sailefy://"):
        video_id = play_url.replace("sailefy://", "")
        from providers import youtube
        resolved_url = youtube.resolve_stream(video_id)
        if not resolved_url:
            notify("Falha ao extrair áudio.", "error")
            xbmcplugin.setResolvedUrl(handle, False, xbmcgui.ListItem(label=title))
            return
        play_url = resolved_url
        
    li = xbmcgui.ListItem(label=title)
    li.setProperty("IsPlayable", "true")
    xbmcplugin.setResolvedUrl(handle, True, li if not hasattr(li, "setPath") else _set_path(li, play_url))


def _set_path(li, path):
    try:
        li.setPath(path)
    except Exception:
        pass
    return li


def save_favorite(base_url, handle, params):
    p = _require_profile(params)
    if not p:
        return show_profiles(base_url, handle)
    provider = params.get("provider", "")
    media_type = params.get("media_type", "")
    external_id = params.get("external_id", "")
    title = params.get("title", "Item")
    storage.upsert_favorite(p["id"], provider, media_type, external_id, title, payload=params)
    notify("Favorito salvo.")
    show_home(base_url, handle, {"profile_id": p["id"]})


def _payload(value):
    if not value:
        return {}
    try:
        return json.loads(value)
    except Exception:
        return {}
