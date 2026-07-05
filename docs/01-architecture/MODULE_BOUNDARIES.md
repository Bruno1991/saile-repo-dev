# Module Boundaries

## Dependências permitidas

- `ui` → `application`, `domain`, `kodi_gateway`;
- `application` → `domain` e interfaces;
- `providers` → `domain` e HTTP abstraction;
- `repositories` → `domain` e SQLite;
- `kodi_gateway` → APIs Kodi e `domain`;
- `domain` → biblioteca padrão apenas.

## Proibições

- `domain` importando `xbmc*`;
- `ui` executando SQL ou `urllib`;
- provider construindo `ListItem`;
- repository mostrando dialogs;
- funções globais lendo settings em qualquer camada;
- módulos importando credenciais em tempo de importação.

## Diretriz de tamanho

Módulos devem ter uma responsabilidade clara. Dividir por comportamento e contrato, não para atingir quantidade arbitrária de linhas.
