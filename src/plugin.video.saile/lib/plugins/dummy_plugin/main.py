# -*- coding: utf-8 -*-
"""
Dummy plugin implementation to test capabilities.
"""

def search_handler(request: dict) -> dict:
    query = request.get('query', '')
    return {
        "results": [
            {"id": "dummy_1", "title": f"Dummy Result for '{query}'"}
        ]
    }

def metadata_handler(request: dict) -> dict:
    item_id = request.get('item_id', '')
    return {
        "title": "Dummy Movie",
        "plot": "This is a dummy plot.",
        "cast": ["Actor A", "Actor B"]
    }

def register(capability_registry):
    capability_registry.register("media.search", "1.0.0", search_handler)
    capability_registry.register("media.metadata", "1.0.0", metadata_handler)
