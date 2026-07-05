---
name: kodi-addon-architecture
title: "Arquitetura de Add-ons Kodi"
description: "Define uma arquitetura limpa para plugins de vídeo locais, modulares e multiplataforma."
domain: "kodi"
triggers:
  - "novo addon Kodi"
  - "arquitetura Kodi"
  - "plugin de vídeo"
  - "organizar addon"
---

# Arquitetura de Add-ons Kodi

## Modelo mental

Kodi é a camada de apresentação, navegação e player. O add-on contém adaptadores para Kodi, casos de uso, providers e persistência local.

```text
Kodi UI
  -> Router/Controller
  -> Application Use Cases
  -> Provider Registry
  -> Provider Client
  -> SQLite Repository/Cache
```

## Estrutura sugerida

```text
plugin.video.exemplo/
├── addon.xml
├── main.py
├── icon.png
├── fanart.jpg
├── LICENSE.txt
└── resources/
    ├── settings.xml
    ├── language/
    ├── media/
    └── lib/
        ├── core/
        ├── application/
        ├── domain/
        ├── providers/
        ├── persistence/
        └── presentation/
```

## Limites

- `main.py`: bootstrap e dispatch;
- presentation: `ListItem`, diálogos, diretórios;
- application: casos de uso;
- providers: HTTP e transformação externa;
- persistence: SQLite;
- domain: modelos e regras puras.

## Fluxos

### Listagem

```text
rota -> caso de uso -> cache/provider -> modelos -> ListItems -> endOfDirectory
```

### Playback

```text
rota play -> resolver fonte -> ListItem(path=...) -> setResolvedUrl
```

## Regras

- nenhuma chamada de rede em import;
- nenhuma escrita SQLite na UI sem repositório;
- nenhum provider retorna `ListItem`;
- nenhum erro de rede vira lista vazia silenciosamente;
- toda rota termina exatamente pelo mecanismo apropriado.
