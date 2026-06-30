# -*- coding: utf-8 -*-
"""
Configuration Service.
Manages secure storage of settings and API keys.
"""

class ConfigurationService:
    def __init__(self):
        self._settings = {}
        self._hidden_settings = {}

    def get(self, key: str, default=None):
        """Retrieve a setting by key."""
        if key in self._hidden_settings:
            return self._hidden_settings[key]
        return self._settings.get(key, default)

    def set(self, key: str, value: str, hidden: bool = False):
        """
        Store a setting.
        If hidden is True, the value is stored securely and should not be exported.
        """
        if hidden:
            self._hidden_settings[key] = value
            # Note: in real Kodi this would write to secure addon settings
        else:
            self._settings[key] = value
            
    def dump_public_config(self) -> dict:
        """Returns public config for diagnostics, explicitly omitting hidden settings."""
        return self._settings.copy()

def configuration_factory():
    return ConfigurationService()
