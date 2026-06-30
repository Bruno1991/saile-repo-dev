import os
import ast
import sys

FORBIDDEN_NETWORK_IMPORTS = {'urllib', 'requests', 'http', 'http.client', 'socket'}
FORBIDDEN_KODI_IMPORTS = {'xbmc', 'xbmcgui', 'xbmcplugin', 'xbmcaddon', 'xbmcvfs'}

def validate_file(filepath):
    errors = []
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read(), filename=filepath)
        except SyntaxError as e:
            return [f"Syntax error in {filepath}: {e}"]

    # Determine context based on path
    parts = filepath.replace('\\', '/').split('/')
    is_kernel = 'kernel' in parts
    is_domain = 'domain' in parts
    is_plugin = 'plugins' in parts
    is_engine = 'engines' in parts

    current_plugin = None
    if is_plugin:
        # e.g., lib/plugins/myplugin/file.py
        idx = parts.index('plugins')
        if len(parts) > idx + 1:
            current_plugin = parts[idx + 1]

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                module_name = alias.name.split('.')[0]
                errors.extend(check_import(module_name, filepath, is_kernel, is_domain, is_plugin, is_engine, current_plugin))
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                module_name = node.module.split('.')[0]
                errors.extend(check_import(module_name, filepath, is_kernel, is_domain, is_plugin, is_engine, current_plugin))

    return errors

def check_import(module_name, filepath, is_kernel, is_domain, is_plugin, is_engine, current_plugin):
    errors = []
    
    # 1. Local-first check (no network)
    if module_name in FORBIDDEN_NETWORK_IMPORTS:
        errors.append(f"Forbidden network import '{module_name}' found in {filepath}. Use isolated SDK wrappers instead.")

    # 2. Kodi decoupling check
    if (is_kernel or is_domain) and module_name in FORBIDDEN_KODI_IMPORTS:
        errors.append(f"Forbidden Kodi import '{module_name}' found in {filepath}. Kernel and Domain must remain decoupled from presentation layer.")

    # 3. Cross-plugin communication check
    if is_plugin and module_name == 'plugins':
        # More complex analysis needed in a real scenario, but simple heuristic for now
        errors.append(f"Potential cross-plugin import '{module_name}' found in {filepath}. Plugins must not communicate directly.")

    return errors

def main():
    lib_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    all_errors = []

    for root, _, files in os.walk(lib_dir):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                errors = validate_file(filepath)
                all_errors.extend(errors)

    if all_errors:
        print("Architecture Validation Failed:")
        for err in all_errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("Architecture Validation Passed.")
        sys.exit(0)

if __name__ == '__main__':
    main()
