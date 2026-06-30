# -*- coding: utf-8 -*-
"""
Capability Registry implementation.
Coordinates registration and lookup of capabilities (e.g. media.search).
"""

class CapabilityRegistryError(Exception):
    pass

class CapabilityRegistry:
    def __init__(self):
        self._capabilities = {}

    def register(self, capability_id: str, version: str, handler):
        """
        Registers a handler for a capability.
        """
        if capability_id not in self._capabilities:
            self._capabilities[capability_id] = {}
        
        # Simple exact version mapping for now
        if version in self._capabilities[capability_id]:
            # In a real system, we might allow multiple plugins, but we enforce determinism
            raise CapabilityRegistryError(f"Capability {capability_id} v{version} is already registered.")
            
        self._capabilities[capability_id][version] = handler

    def lookup(self, capability_id: str, version: str):
        """
        Looks up a handler for a specific capability and version.
        """
        if capability_id not in self._capabilities:
            raise CapabilityRegistryError(f"No handlers registered for capability {capability_id}.")
            
        handlers = self._capabilities[capability_id]
        
        # For this skeleton, we do an exact version match.
        if version not in handlers:
            raise CapabilityRegistryError(f"Version {version} not found for capability {capability_id}.")
            
        return handlers[version]

    def clear(self):
        self._capabilities.clear()
