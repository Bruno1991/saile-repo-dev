# -*- coding: utf-8 -*-
"""
Main entrypoint for Kodi (Presentation Layer).
Initializes the runtime, handles routing, and renders the Kodi UI.
"""
import sys
import os
import urllib.parse

# Add lib directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from bootstrap import bootstrap
from lib.kernel.plugin_manager import PluginManager

# Import Kodi libraries (Only allowed in Presentation Layer)
try:
    import xbmc
    import xbmcgui
    import xbmcplugin
except ImportError:
    # Fallback for local execution/testing outside Kodi
    xbmc = xbmcgui = xbmcplugin = None

def parse_routing(args):
    """Parse the query parameters from sys.argv."""
    if len(args) > 2:
        return dict(urllib.parse.parse_qsl(args[2][1:]))
    return {}

def render_directory_item(addon_handle, url, title, is_folder):
    """Helper to render a single Kodi list item."""
    if xbmcgui is None:
        return  # Mock behavior
        
    li = xbmcgui.ListItem(title)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=is_folder)

def main():
    # Setup args
    addon_url = sys.argv[0]
    
    try:
        addon_handle = int(sys.argv[1])
    except (IndexError, ValueError):
        addon_handle = -1

    params = parse_routing(sys.argv)
    action = params.get('action', 'root')

    # 1. Bootstrap the core
    registry = bootstrap()
    log = registry.resolve('ILoggingService')
    engine_reg = registry.resolve('IEngineRegistry')
    log.info(f"Starting SAILE Addon - Action: {action}")

    # 2. Initialize Plugin Manager
    plugins_dir = os.path.join(os.path.dirname(__file__), 'lib', 'plugins')
    pm = PluginManager(plugins_dir)
    try:
        pm.discover_plugins()
        log.info(f"Loaded {len(pm._plugins)} plugins.")
    except Exception as e:
        log.error(f"Plugin load failed: {e}")

    # 3. Handle Routing & UI Generation
    if action == 'root':
        log.info("Rendering Main Menu...")
        # Create a search action
        url = f"{addon_url}?action=search&q=avatar"
        render_directory_item(addon_handle, url, "Test Search (Query: 'avatar')", is_folder=True)
        
    elif action == 'search':
        query = params.get('q', '')
        log.info(f"Executing search workflow for: {query}")
        
        # Execute Engine workflow
        try:
            results = engine_reg.execute_workflow('SearchEngine', 'execute_search', query=query)
            
            for item in results:
                title = item.get('title', 'Unknown Title')
                item_id = item.get('id', '')
                # A real plugin would route to a 'play' action next
                url = f"{addon_url}?action=play&id={item_id}"
                render_directory_item(addon_handle, url, title, is_folder=False)
                
        except Exception as e:
            log.error(f"Engine execution failed: {e}")

    # 4. Finalize Kodi Directory
    if xbmcplugin is not None and addon_handle != -1:
        xbmcplugin.endOfDirectory(addon_handle)
        
    log.info("SAILE Addon finished execution.")

if __name__ == '__main__':
    main()
