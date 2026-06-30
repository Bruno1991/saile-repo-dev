# -*- coding: utf-8 -*-
"""
Bootstrap script to initialize the Runtime and Kernel.
"""
from lib.kernel.service_registry import ServiceRegistry
from lib.services.logging_service import logging_factory
from lib.services.configuration_service import configuration_factory
from lib.kernel.capability_registry import CapabilityRegistry
from lib.kernel.engine_registry import EngineRegistry

def bootstrap() -> ServiceRegistry:
    """
    Initializes the in-process Runtime and Kernel.
    Returns the initialized ServiceRegistry.
    """
    registry = ServiceRegistry()
    
    # Core Services
    registry.register('ILoggingService', logging_factory, is_singleton=True)
    registry.register('IConfigurationService', configuration_factory, is_singleton=True)
    
    # Registries
    registry.register('ICapabilityRegistry', lambda: CapabilityRegistry(), is_singleton=True)
    registry.register('IEngineRegistry', lambda: EngineRegistry(), is_singleton=True)
    
    # Initialize basic logging
    log = registry.resolve('ILoggingService')
    log.info("SAILE Kernel Bootstrapped successfully.")
    
    # Instantiate and register Engines
    cap_reg = registry.resolve('ICapabilityRegistry')
    engine_reg = registry.resolve('IEngineRegistry')
    
    from lib.engines.search_engine import SearchEngine
    engine_reg.register('SearchEngine', SearchEngine(cap_reg, log))
    
    return registry

if __name__ == "__main__":
    bootstrap()
