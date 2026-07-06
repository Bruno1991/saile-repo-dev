# Pacote de artes genéricas

Este diretório contém artes temporárias prontas para evitar ícones ausentes durante o desenvolvimento de `repository.srepo`, `plugin.video.stv` e `plugin.audio.sfy`.

## Regra de uso

1. Copie cada arquivo para o destino indicado em `artwork-manifest.json`.
2. Não renomeie os arquivos usados pelo código ou pelo `addon.xml` sem atualizar todas as referências.
3. As artes são placeholders e devem ser substituídas pela identidade visual final.
4. Ao substituir, preserve proporção, formato e finalidade:
   - `icon.png`: quadrado, PNG;
   - `fanart.jpg`: 16:9, JPG;
   - ícones de menu: quadrados, PNG;
   - pôster: proporção vertical;
   - capa de álbum/artista: quadrada.
5. O build não pode publicar um add-on sem `icon.png` e `fanart.jpg`.

## Estrutura

```text
artwork/
├── artwork-manifest.json
└── generic/
    ├── repository.srepo/
    ├── plugin.video.stv/
    │   └── resources/media/
    └── plugin.audio.sfy/
        └── resources/media/
```

Consulte `docs/ui/ARTWORK_CATALOG.md` para o catálogo completo e as regras de fallback.
