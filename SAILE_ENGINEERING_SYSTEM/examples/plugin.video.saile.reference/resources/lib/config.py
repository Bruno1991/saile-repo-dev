from __future__ import annotations

from dataclasses import dataclass

import xbmcaddon


@dataclass(frozen=True)
class AppConfig:
    demo_url: str


def load_config() -> AppConfig:
    addon = xbmcaddon.Addon()
    return AppConfig(demo_url=addon.getSettingString("demo.url").strip())
