---
name: python-style-typing
title: "Estilo, Tipagem e Contratos Python"
description: "Aplica legibilidade, tipos úteis e contratos explícitos sem burocracia excessiva."
domain: "python"
triggers:
  - "type hints"
  - "qualidade Python"
  - "padronização"
  - "API interna"
---

# Estilo, Tipagem e Contratos Python

## Objetivos

- tornar entradas e saídas previsíveis;
- reduzir erros de `None`, strings numéricas e dicionários inconsistentes;
- melhorar revisão e manutenção.

## Regras

- tipar funções públicas e fronteiras entre camadas;
- usar `dataclass` para dados estruturados estáveis;
- preferir `Mapping`/`Sequence` quando não há necessidade de mutação;
- evitar `Any` como solução padrão;
- converter dados externos na borda;
- representar ausência com `None` somente quando semanticamente válida.

## Exemplo

```python
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class VideoItem:
    media_id: str
    title: str
    stream_url: Optional[str] = None
```

## Dicionários externos

Não espalhe `payload.get("name")` pelo projeto. Crie um parser:

```python
def parse_video(payload: dict) -> VideoItem:
    media_id = str(payload["id"])
    title = str(payload.get("title") or "Sem título").strip()
    return VideoItem(media_id=media_id, title=title)
```

## Docstrings

Use docstrings para contrato, efeitos colaterais e exceções relevantes. Não repita o nome da função em prosa.

## Compatibilidade

Antes de usar sintaxe recente, confirme a versão do Python embarcada no Kodi-alvo. Não introduza `match`, tipos parametrizados modernos ou recursos de biblioteca sem verificar suporte.
