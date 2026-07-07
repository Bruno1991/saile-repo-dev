# Sincronização LAN manual

## Experiência

O usuário seleciona `Sincronizar Dados` na home do sTv ou sFy. Nada é executado automaticamente.

## Descoberta

A implementação futura pode usar broadcast/multicast UDP apenas para descobrir dispositivos com add-on e versão de protocolo compatíveis. A transferência deve usar sessão autenticada/confirmada e possuir timeout.

## Dados do sTv

- favoritos separados por `live`, `vod` e `series`;
- progresso de VOD/episódio;
- preferências não sensíveis.

## Dados do sFy

- playlists e seus itens;
- histórico opcional;
- preferências não sensíveis.

## Não sincronizar

- bancos SQLite completos;
- catálogos Xtream e cache TMDB;
- resultados/cache musical;
- credenciais, tokens, cookies e URLs temporárias.

## Conflitos

- registros possuem ID estável, `updated_at` e tombstone;
- favoritos: last-write-wins;
- progresso: atualização mais recente, preservando estado concluído;
- playlists: operações por item, nunca substituição silenciosa da lista inteira.

## Segurança operacional

Exibir dispositivo de origem/destino e resumo antes de aplicar. Permitir cancelamento. Registrar somente contagens e códigos sanitizados.
