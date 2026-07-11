from __future__ import annotations

from sfy.navigation_contract import HOME_ENTRIES
from sfy.routing import Request


def _show_home(request: Request, fanart: str, app: 'AppContainer') -> None:
    from saile_core.artwork import artwork_path
    from sfy.ui.directory import add_folder, finish_directory

    for label, action, scope, filename in HOME_ENTRIES:
        add_folder(
            request.handle,
            label,
            request.url(action=action),
            artwork_path(scope, filename),
            fanart,
        )

    # Historic tracks on home
    history = app.catalog.get_history()
    for track in history:
        url = request.url(action="play", track_id=track.track_id)
        context_menu = [
            ("Adicionar à Playlist", f"RunPlugin({request.url(action='add_to_playlist', track_id=track.track_id)})")
        ]
        add_folder(
            request.handle,
            f"{track.title} - {track.artist}",
            url,
            track.thumbnail,
            fanart,
            is_folder=False,
            is_playable=True,
            context_menu=context_menu
        )

    finish_directory(request.handle, "songs")


def run(argv: list[str]) -> None:
    import xbmc
    import xbmcgui
    import xbmcaddon
    import xbmcplugin
    
    from saile_core.notifications import notify_info, notify_error
    from sfy.app.services import AppContainer

    request = Request.from_argv(argv)
    addon = xbmcaddon.Addon()
    fanart = addon.getAddonInfo("fanart")
    profile_path = xbmc.translatePath(addon.getAddonInfo("profile"))
    settings = {"profile_path": profile_path}
    
    app = AppContainer(settings)

    if request.action in {"", "home"}:
        _show_home(request, fanart, app)
        return

    if request.action == "search":
        from sfy.ui.directory import finish_directory, add_folder
        keyboard = xbmc.Keyboard("", "Buscar Músicas...")
        keyboard.doModal()
        if keyboard.isConfirmed() and keyboard.getText():
            query = keyboard.getText()
            tracks = app.catalog.search_and_cache(app.ytm, query)
            for track in tracks:
                url = request.url(action="play", track_id=track.track_id)
                context_menu = [
                    ("Adicionar à Playlist", f"RunPlugin({request.url(action='add_to_playlist', track_id=track.track_id)})")
                ]
                add_folder(
                    request.handle,
                    f"{track.title} - {track.artist}",
                    url,
                    track.thumbnail,
                    fanart,
                    is_folder=False,
                    is_playable=True,
                    context_menu=context_menu
                )
        finish_directory(request.handle, "songs")
        return

    if request.action == "play":
        track_id = request.params.get("track_id")
        if not track_id:
            return
            
        # Resolve stream via YtmClient (which uses yt-dlp)
        try:
            stream_url = app.ytm.resolve_stream(track_id)
            app.repo.log_playback(track_id)
            
            track = app.repo.get_track(track_id)
            li = xbmcgui.ListItem(path=stream_url)
            if track:
                li.setLabel(track.title)
                li.setArt({"thumb": track.thumbnail, "icon": track.thumbnail})
                li.setInfo("music", {"title": track.title, "artist": track.artist, "album": track.album})
                
            xbmcplugin.setResolvedUrl(request.handle, True, listitem=li)
        except Exception as e:
            notify_error("sFy", f"Erro ao resolver: {e}")
            xbmcplugin.setResolvedUrl(request.handle, False, listitem=xbmcgui.ListItem())
        return

    if request.action == "sync":
        notify_info("sFy", "Sincronização LAN manual ainda não implementada")
        _show_home(request, fanart, app)
        return

    if request.action == "playlists":
        from sfy.ui.directory import finish_directory, add_folder
        # Add 'Create Playlist' button
        add_folder(
            request.handle,
            "+ Criar Nova Playlist",
            request.url(action="create_playlist"),
            "",
            fanart,
            is_folder=False
        )
        playlists = app.repo.get_playlists()
        for pl in playlists:
            add_folder(
                request.handle,
                pl["name"],
                request.url(action="view_playlist", playlist_id=pl["playlist_id"]),
                "",
                fanart
            )
        finish_directory(request.handle, "songs")
        return

    if request.action == "create_playlist":
        keyboard = xbmc.Keyboard("", "Nome da Playlist")
        keyboard.doModal()
        if keyboard.isConfirmed() and keyboard.getText():
            name = keyboard.getText().strip()
            if name:
                app.repo.create_playlist(name)
                notify_info("sFy", f"Playlist '{name}' criada!")
                xbmc.executebuiltin("Container.Refresh")
        return

    if request.action == "view_playlist":
        from sfy.ui.directory import finish_directory, add_folder
        playlist_id = request.params.get("playlist_id")
        if playlist_id:
            tracks = app.repo.get_playlist_tracks(int(playlist_id))
            for track in tracks:
                url = request.url(action="play", track_id=track.track_id)
                context_menu = [
                    ("Adicionar à Playlist", f"RunPlugin({request.url(action='add_to_playlist', track_id=track.track_id)})")
                ]
                add_folder(
                    request.handle,
                    f"{track.title} - {track.artist}",
                    url,
                    track.thumbnail,
                    fanart,
                    is_folder=False,
                    is_playable=True,
                    context_menu=context_menu
                )
        finish_directory(request.handle, "songs")
        return

    if request.action == "add_to_playlist":
        track_id = request.params.get("track_id")
        if track_id:
            playlists = app.repo.get_playlists()
            if not playlists:
                notify_info("sFy", "Nenhuma playlist criada.")
                return
            names = [pl["name"] for pl in playlists]
            dialog = xbmcgui.Dialog()
            index = dialog.select("Escolha a Playlist", names)
            if index >= 0:
                pl_id = playlists[index]["playlist_id"]
                app.repo.add_track_to_playlist(pl_id, track_id)
                notify_info("sFy", "Adicionado à playlist!")
        return
        
    _show_home(request, fanart, app)
