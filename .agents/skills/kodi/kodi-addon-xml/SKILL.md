---
name: kodi-addon-xml
title: "Manifesto addon.xml"
description: "Cria e valida o manifesto, dependências, extensões, metadados e assets."
domain: "kodi"
triggers:
  - "addon.xml"
  - "manifesto Kodi"
  - "dependência Kodi"
  - "ID do addon"
---

# Manifesto addon.xml

## Responsabilidade

`addon.xml` identifica o add-on, versão, provider, dependências e pontos de extensão. O ID é contrato público e não deve mudar após publicação sem plano de migração.

## Plugin de vídeo básico

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="plugin.video.exemplo"
       name="Exemplo"
       version="1.0.0"
       provider-name="Equipe Exemplo">
  <requires>
    <import addon="xbmc.python" version="3.0.0"/>
  </requires>
  <extension point="xbmc.python.pluginsource" library="main.py">
    <provides>video</provides>
  </extension>
  <extension point="xbmc.addon.metadata">
    <summary lang="pt_BR">Resumo objetivo.</summary>
    <description lang="pt_BR">Descrição completa.</description>
    <platform>all</platform>
    <license>GPL-3.0-or-later</license>
    <assets>
      <icon>icon.png</icon>
      <fanart>fanart.jpg</fanart>
    </assets>
  </extension>
</addon>
```

## Checklist

- ID em minúsculas e estável;
- versão SemVer coerente com ZIP e repositório;
- entry point existente;
- dependências declaradas;
- `<provides>video</provides>` para plugin de vídeo;
- idioma e assets existentes;
- licença incluída;
- XML bem formado e UTF-8.

## Dependências

Não declare módulo apenas porque está instalado no ambiente do desenvolvedor. Confirme disponibilidade no repositório e compatibilidade da versão Kodi-alvo.

## Versão

Mudança de schema, rotas públicas ou requisitos pode exigir incremento maior/minor conforme política do projeto. Nunca editar versão apenas no ZIP.
