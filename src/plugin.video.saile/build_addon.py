# -*- coding: utf-8 -*-
"""
Build script to package the SAILE addon for Kodi deployment.
Creates a zip file conforming to Kodi addon structure.
"""
import os
import zipfile

def build_zip():
    addon_id = "plugin.video.saile"
    version = "1.0.0"
    zip_name = f"{addon_id}-{version}.zip"
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(base_dir, 'dist')
    
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
        
    zip_path = os.path.join(dist_dir, zip_name)
    
    included_dirs = ['lib', '.agents']
    included_files = ['addon.xml', 'default.py', 'LICENSE', 'README.md']
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in included_files:
            file_path = os.path.join(base_dir, file)
            if os.path.exists(file_path):
                # Put inside a folder named after addon_id as required by Kodi
                zipf.write(file_path, arcname=os.path.join(addon_id, file))
                
        for d in included_dirs:
            dir_path = os.path.join(base_dir, d)
            if os.path.exists(dir_path):
                for root, _, files in os.walk(dir_path):
                    for f in files:
                        file_path = os.path.join(root, f)
                        arc_name = os.path.join(addon_id, os.path.relpath(file_path, base_dir))
                        zipf.write(file_path, arcname=arc_name)

    print(f"Build complete: {zip_path}")

if __name__ == "__main__":
    build_zip()
