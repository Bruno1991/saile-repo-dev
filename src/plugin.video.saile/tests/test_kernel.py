# -*- coding: utf-8 -*-
"""
Test suite for the Kernel Service Registry.
"""
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.kernel.service_registry import ServiceRegistry, ServiceRegistryError

class DummyService:
    pass

class TestServiceRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = ServiceRegistry()

    def test_register_and_resolve_singleton(self):
        self.registry.register("IDummy", lambda: DummyService(), is_singleton=True)
        instance1 = self.registry.resolve("IDummy")
        instance2 = self.registry.resolve("IDummy")
        self.assertIs(instance1, instance2, "Singleton should return the exact same instance")

    def test_register_and_resolve_transient(self):
        self.registry.register("IDummy", lambda: DummyService(), is_singleton=False)
        instance1 = self.registry.resolve("IDummy")
        instance2 = self.registry.resolve("IDummy")
        self.assertIsNot(instance1, instance2, "Transient should return a new instance every time")

if __name__ == '__main__':
    unittest.main()
