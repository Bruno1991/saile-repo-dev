# ADR-0007 — Protocolo de Sincronização LAN

## Status
Aceito

## Contexto
O usuário precisa de uma forma de propagar dados de progresso de visualização e favoritos entre instâncias do sTv/sFy na mesma rede local (ex: da TV da sala para o celular na mesma casa). Sem um backend de nuvem (ADR-0002), a solução precisa ser ponto a ponto.

## Decisão
- Utilizar UDP Broadcast na porta local para descobrimento. A mensagem trafegará de forma criptográfica usando SHA-256 (hash de host e username do provedor) garantindo que apenas dispositivos da mesma conta falem entre si, sem vazamento na LAN.
- O Kodi levanta um Background Service (`service.py`) de forma transparente que responde na porta TCP fornecendo um JSON estruturado ao dispositivo solicitante.
- Cada addon tem independência e faz merge (`UPSERT`) considerando timestamps.

## Consequências
- A segurança é resguardada na LAN porque senhas não viajam no fio.
- Os dispositivos funcionam de forma descentralizada.
