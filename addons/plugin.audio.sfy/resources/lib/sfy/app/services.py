"""Application services for search, local playlists, history and playback resolution."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from sfy.providers.ytdlp.resolver import YtDlpResolver


@dataclass(frozen=True)
class ChartPlaylist:
    title: str
    url: str
    thumbnail: str


class ChartsService:
    def __init__(self, resolver: YtDlpResolver | None = None) -> None:
        self.resolver = resolver or YtDlpResolver()

    def get_home_charts(self) -> Iterator[ChartPlaylist]:
        # Em uma implementação real, os URLs viriam do yt-dlp ou de constantes confirmadas.
        # Estamos criando as entradas dinâmicas para provar o contrato de navegação.
        yield ChartPlaylist(
            title="Top Brasil",
            url="https://music.youtube.com/playlist?list=PL4fGSI1pccIONp_hX-gQZep5d5oE7b0s7",
            thumbnail="https://lh3.googleusercontent.com/vH-qP0yM3_b4wWj_vXfXhN7p_Uv-qQfM6w"
        )
        yield ChartPlaylist(
            title="Top Mundo",
            url="https://music.youtube.com/playlist?list=PL4fGSI1pccIPo3p3E5f7zM8j_5y7xJ-oG",
            thumbnail="https://lh3.googleusercontent.com/mO_T-jKjQ_"
        )
