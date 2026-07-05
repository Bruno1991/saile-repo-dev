---
name: kodi-settings-localization
title: "Settings e Localização"
description: "Cria configurações modernas, tipadas, localizadas e seguras."
domain: "kodi"
triggers:
  - "settings.xml"
  - "configuração Kodi"
  - "strings.po"
  - "localização"
---

# Settings e Localização

## Formato moderno

Para Kodi 19+, prefira o formato de settings com `version="1"`, `section`, `category`, `group` e controles explícitos, conforme documentação oficial.

## Regras

- IDs de settings são contratos persistidos;
- labels e help usam IDs de idioma;
- strings começam normalmente na faixa reservada do add-on;
- valores lidos devem ser convertidos para tipo correto;
- senha visualmente oculta ainda é armazenada localmente e não deve ser logada.

## Estrutura de idioma

```text
resources/language/resource.language.pt_br/strings.po
resources/language/resource.language.en_gb/strings.po
```

## Leitura

Centralize:

```python
addon = xbmcaddon.Addon()
host = addon.getSettingString("provider.host").strip()
limit = addon.getSettingInt("ui.page_size")
```

Confirme disponibilidade dos getters tipados na versão-alvo; forneça conversão segura quando necessário.

## Mudança de ID

Se um ID mudar, implemente migração de settings ou compatibilidade temporária. Não perca configuração do usuário silenciosamente.

## UX

Agrupe por responsabilidade, forneça ajuda, valide antes de salvar/usar e evite dezenas de opções internas sem necessidade.
