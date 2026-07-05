---
name: kodi-plugin-routing
title: "Roteamento de Plugins Kodi"
description: "Implementa parsing seguro de sys.argv, URLs plugin:// e dispatch explícito."
domain: "kodi"
triggers:
  - "router Kodi"
  - "sys.argv"
  - "plugin URL"
  - "action route"
---

# Roteamento de Plugins Kodi

## Entrada do plugin

Normalmente:

- `sys.argv[0]`: base `plugin://...`;
- `sys.argv[1]`: handle numérico;
- `sys.argv[2]`: query string.

Valide tamanho antes de acessar em testes ou execução fora do Kodi.

## Construção de URL

```python
from urllib.parse import urlencode

def build_url(base_url: str, action: str, **params: str) -> str:
    query = {"action": action, **params}
    return f"{base_url}?{urlencode(query)}"
```

## Parsing

```python
from urllib.parse import parse_qs

def parse_params(raw: str) -> dict[str, str]:
    values = parse_qs(raw.lstrip("?"), keep_blank_values=True)
    return {key: items[-1] for key, items in values.items()}
```

Adapte tipagem à versão de Python suportada.

## Dispatch

Use allowlist de actions, não `globals()` ou `eval`.

```python
ROUTES = {
    "home": show_home,
    "movies": show_movies,
    "play": play_item,
}
```

## Contratos

- rotas de pasta chamam `endOfDirectory`;
- rota de playback chama `setResolvedUrl`;
- parâmetros são convertidos e validados;
- IDs opacos são preferidos a dados sensíveis na URL;
- actions antigas só são removidas com compatibilidade planejada.

## Erro

Action desconhecida deve gerar log e fallback seguro, não executar função arbitrária.
