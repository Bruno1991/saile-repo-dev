# -*- coding: utf-8 -*-
"""
Engine Registry implementation.
Coordinates media engines which own business rules and workflows.
"""

class EngineRegistryError(Exception):
    pass

class EngineRegistry:
    def __init__(self):
        self._engines = {}

    def register(self, engine_id: str, engine_instance):
        """
        Registers an Engine instance.
        """
        if engine_id in self._engines:
            raise EngineRegistryError(f"Engine {engine_id} is already registered.")
            
        self._engines[engine_id] = engine_instance

    def get_engine(self, engine_id: str):
        """
        Retrieves a registered Engine.
        """
        if engine_id not in self._engines:
            raise EngineRegistryError(f"Engine {engine_id} not found.")
            
        return self._engines[engine_id]

    def execute_workflow(self, engine_id: str, workflow_name: str, **kwargs):
        """
        Executes a specific workflow on an engine.
        """
        engine = self.get_engine(engine_id)
        if not hasattr(engine, workflow_name):
            raise EngineRegistryError(f"Workflow {workflow_name} not found on Engine {engine_id}.")
            
        workflow_func = getattr(engine, workflow_name)
        return workflow_func(**kwargs)

    def clear(self):
        self._engines.clear()
