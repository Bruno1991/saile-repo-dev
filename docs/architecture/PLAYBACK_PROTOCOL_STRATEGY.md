# Estratégia de reprodução por protocolo

O sTv não força um único método para todos os streams.

| Origem | Estratégia inicial |
|---|---|
| HTTP TS direto | player Kodi |
| HLS simples | player Kodi; fallback controlado |
| HLS/DASH adaptativo | InputStream Adaptive quando disponível |
| stream problemático compatível | InputStream FFmpeg Direct quando disponível |

A seleção deve detectar protocolo, capacidade instalada e erro anterior. Dependências opcionais não podem impedir a abertura da home.
