import time
import xbmcgui

from stv.domain.models import Category, MediaItem
from stv.providers.xtream.client import XtreamClient
from stv.persistence.repository import CatalogRepository


class CatalogOrchestrator:
    def __init__(self, client: XtreamClient, repository: CatalogRepository) -> None:
        self.client = client
        self.repository = repository

    def sync_if_needed(self, media_type: str, ttl_hours: int = 12) -> None:
        try:
            _ = self.client.host
        except ValueError:
            return

        if self.repository.is_cache_valid(media_type, ttl_hours):
            return

        dialog = xbmcgui.DialogProgress()
        dialog.create("sTv", f"Atualizando catálogo de {media_type.upper()}...")
        
        try:
            generation_id = int(time.time())
            
            dialog.update(20, "Baixando dados do servidor Xtream...")
            if media_type == "live":
                raw_cats = self.client.request("get_live_categories")
                raw_streams = self.client.request("get_live_streams")
            elif media_type == "vod":
                raw_cats = self.client.request("get_vod_categories")
                raw_streams = self.client.request("get_vod_streams")
            elif media_type == "series":
                raw_cats = self.client.request("get_series_categories")
                raw_streams = self.client.request("get_series")
            else:
                return

            if dialog.iscanceled():
                return

            dialog.update(50, "Salvando categorias localmente...")
            categories = []
            for c in raw_cats:
                cat_id = str(c.get("category_id", ""))
                if cat_id:
                    categories.append(Category(
                        category_id=cat_id,
                        name=c.get("category_name", "Desconhecida"),
                        parent_id=str(c.get("parent_id", "0")),
                        media_type=media_type,
                        generation_id=generation_id
                    ))
            
            if categories:
                self.repository.upsert_categories(categories)

            if dialog.iscanceled():
                return

            dialog.update(70, "Salvando mídias localmente...")
            items = []
            for s in raw_streams:
                item_id = str(s.get("stream_id") or s.get("series_id", ""))
                if not item_id:
                    continue
                
                cat_id = str(s.get("category_id", ""))
                name = s.get("name") or s.get("title") or "Desconhecido"
                icon = s.get("stream_icon") or s.get("cover") or ""
                extension = s.get("container_extension", "")
                
                items.append(MediaItem(
                    media_type=media_type,
                    item_id=item_id,
                    name=name,
                    category_id=cat_id,
                    icon=icon,
                    extension=extension,
                    generation_id=generation_id
                ))

            if items:
                chunk_size = 500
                for i in range(0, len(items), chunk_size):
                    self.repository.upsert_media_items(items[i:i+chunk_size])
                    
            dialog.update(90, "Limpando registros antigos...")
            self.repository.clean_obsolete_categories(media_type, generation_id)
            self.repository.clean_obsolete_items(media_type, generation_id)
            
            dialog.update(100, "Concluído!")
            time.sleep(0.5)
            
        finally:
            dialog.close()
