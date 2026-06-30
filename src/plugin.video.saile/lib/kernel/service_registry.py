# -*- coding: utf-8 -*-
"""
Service Registry implementation for the Kernel.
Manages dependency injection, lifecycles (singleton/transient), and isolates services.
"""

class ServiceRegistryError(Exception):
    """Base exception for ServiceRegistry errors."""
    pass

class ServiceRegistry:
    def __init__(self):
        self._services = {}
        self._singletons = {}

    def register(self, interface_name, implementation_factory, is_singleton=True):
        """
        Registers a service factory.
        :param interface_name: Unique name of the service (e.g. 'ILoggingService').
        :param implementation_factory: Callable that returns the service instance.
        :param is_singleton: If True, the factory is called once and cached.
        """
        if interface_name in self._services:
            raise ServiceRegistryError(f"Service {interface_name} is already registered.")
        
        self._services[interface_name] = {
            'factory': implementation_factory,
            'is_singleton': is_singleton
        }

    def resolve(self, interface_name):
        """
        Resolves a service by its interface name.
        """
        if interface_name not in self._services:
            raise ServiceRegistryError(f"Service {interface_name} not found.")

        service_def = self._services[interface_name]

        if service_def['is_singleton']:
            if interface_name not in self._singletons:
                self._singletons[interface_name] = service_def['factory']()
            return self._singletons[interface_name]
        else:
            return service_def['factory']()

    def clear(self):
        """Clears all registered services. Useful for testing."""
        self._services.clear()
        self._singletons.clear()
