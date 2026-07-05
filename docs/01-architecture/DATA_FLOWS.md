# Data Flows

## Listagem

Route → use case → cache lookup → provider quando necessário → normalização → persistência transacional → view model → Kodi directory.

## Sincronização manual

Ação explícita → dialog de progresso → operações canceláveis → escrita por lotes → commit por unidade consistente → resumo de sucesso/falha. Cancelamento preserva último estado válido.

## Playback

Clique → rota protegida → localizar item → provider resolve fonte → validar expiração e esquema → gateway Kodi configura item → player recebe resolução.

## Progresso

Eventos do player → filtro de intervalo → update idempotente → commit curto. Falha de progresso não interrompe reprodução.

## Erro remoto

Timeout/provider error → usar cache stale quando política permitir → informar degradação → registrar sem credenciais.
