# -*- coding: utf-8 -*-
"""
Search Engine.
Owns the business logic for fetching search results via capabilities
and normalizing them into a domain model format.
"""

class SearchEngine:
    def __init__(self, capability_registry, logger):
        self.registry = capability_registry
        self.logger = logger

    def execute_search(self, query: str):
        """
        Executes a search workflow.
        """
        self.logger.info(f"Engine starting search for: {query}")
        
        try:
            # According to Capability_Registry.md, lookup by capability_id and version
            handler = self.registry.lookup("media.search", "1.0.0")
        except Exception as e:
            self.logger.error(f"Capability lookup failed: {e}")
            return []

        # Execute capability contract
        request_model = {"query": query}
        
        try:
            response = handler(request_model)
            results = response.get('results', [])
            self.logger.info(f"Search yielded {len(results)} items.")
            
            # Normalize to our internal domain models (in a real scenario)
            return results
        except Exception as e:
            self.logger.error(f"Capability execution failed: {e}")
            return []
