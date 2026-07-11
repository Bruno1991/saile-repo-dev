from __future__ import annotations

import os

from sfy.persistence.database import Database
from sfy.persistence.repository import MusicRepository
from sfy.domain.catalog import CatalogOrchestrator


class AppContainer:
    """Dependency injection container for sFy."""

    def __init__(self, settings: dict[str, str]) -> None:
        self.settings = settings
        self._database: Database | None = None
        self._repo: MusicRepository | None = None
        self._catalog: CatalogOrchestrator | None = None
        self._ytm = None

    @property
    def database(self) -> Database:
        if self._database is None:
            db_path = os.path.join(self.settings.get("profile_path", ""), "sfy.db")
            self._database = Database(db_path)
            self._database.initialize()
        return self._database

    @property
    def repo(self) -> MusicRepository:
        if self._repo is None:
            self._repo = MusicRepository(self.database)
        return self._repo

    @property
    def catalog(self) -> CatalogOrchestrator:
        if self._catalog is None:
            self._catalog = CatalogOrchestrator(self.repo)
        return self._catalog

    @property
    def ytm(self) -> 'YtmClient':
        if self._ytm is None:
            from saile_ytdlp.client import YtmClient
            self._ytm = YtmClient()
        return self._ytm
