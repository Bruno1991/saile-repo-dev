# Artwork genérico temporário

Esta pasta é a fonte de bootstrap. O runtime nunca aponta diretamente para ela.

- `repository.srepo`, `plugin.video.stv`, `plugin.audio.sfy`, `resource.images.saile` e `script.module.saile.core` possuem `icon.png` e `fanart.jpg` genéricos.
- Os nove ícones fixos estão em `artwork/generic/resource.images.saile/resources/media/`.
- `python tools/bootstrap_artwork.py` copia cada arquivo para o destino descrito em `artwork/artwork-manifest.json`.
- Artes finais podem substituir os arquivos mantendo nomes e proporções.
