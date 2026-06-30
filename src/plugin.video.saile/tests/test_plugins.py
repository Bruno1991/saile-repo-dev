# -*- coding: utf-8 -*-
"""
Test suite for the Plugin Manager.
"""
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.kernel.plugin_manager import PluginManager

class TestPluginManager(unittest.TestCase):
    def setUp(self):
        self.plugins_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', 'plugins'))
        self.pm = PluginManager(self.plugins_dir)

    def test_discover_plugins(self):
        self.pm.discover_plugins()
        # The dummy plugin should be loaded
        self.assertIn("saile.plugin.dummy", self.pm._plugins)
        
        manifest = self.pm.get_plugin_manifest("saile.plugin.dummy")
        self.assertEqual(manifest["version"], "1.0.0")
        self.assertIn("network.http", manifest["permissions"])

if __name__ == '__main__':
    unittest.main()
