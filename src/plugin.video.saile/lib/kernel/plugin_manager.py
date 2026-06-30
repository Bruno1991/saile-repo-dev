# -*- coding: utf-8 -*-
"""
Plugin Manager implementation.
Handles safe discovery, validation, and loading of Plugins.
"""

import os
import json

class PluginManagerError(Exception):
    pass

class PluginManager:
    def __init__(self, plugins_dir: str):
        self._plugins_dir = plugins_dir
        self._plugins = {}

    def discover_plugins(self):
        """Scans the plugins directory and validates manifests."""
        if not os.path.exists(self._plugins_dir):
            return

        for entry in os.listdir(self._plugins_dir):
            plugin_path = os.path.join(self._plugins_dir, entry)
            if os.path.isdir(plugin_path):
                self._load_plugin(plugin_path)

    def _load_plugin(self, plugin_path: str):
        """Validates and loads a single plugin manifest."""
        manifest_path = os.path.join(plugin_path, 'plugin.json')
        if not os.path.exists(manifest_path):
            # Try yaml if json doesn't exist. For now, strict json requirement for simplicity.
            return

        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
        except Exception as e:
            raise PluginManagerError(f"Failed to parse manifest at {manifest_path}: {e}")

        # Validation per PLUGIN_SDK.md
        required_fields = ['id', 'version', 'capabilities', 'permissions']
        for field in required_fields:
            if field not in manifest:
                raise PluginManagerError(f"Plugin at {plugin_path} missing required field '{field}'.")

        plugin_id = manifest['id']
        if plugin_id in self._plugins:
            raise PluginManagerError(f"Plugin {plugin_id} is already loaded.")

        # In a real implementation, we would register capabilities with the CapabilityRegistry here
        self._plugins[plugin_id] = {
            'manifest': manifest,
            'path': plugin_path
        }

    def get_plugin_manifest(self, plugin_id: str) -> dict:
        if plugin_id not in self._plugins:
            raise PluginManagerError(f"Plugin {plugin_id} not found.")
        return self._plugins[plugin_id]['manifest']

    def clear(self):
        self._plugins.clear()
