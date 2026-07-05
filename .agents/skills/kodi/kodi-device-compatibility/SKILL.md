---
name: kodi-device-compatibility
title: "Compatibilidade entre Dispositivos Kodi"
description: "Evita dependências e padrões que quebram em Android, Fire TV, Windows ou Linux."
domain: "kodi"
triggers:
  - "compatibilidade Kodi"
  - "Android TV"
  - "Firestick"
  - "Windows Linux"
---

# Compatibilidade entre Dispositivos Kodi

## Matriz mínima

Documente:

- versões Kodi suportadas;
- Python mínimo implícito;
- plataformas testadas;
- arquiteturas CPU relevantes;
- dependências binárias;
- protocolos de mídia.

## Riscos comuns

- paths absolutos;
- diferença de maiúsculas/minúsculas;
- extensão nativa disponível só em x86_64;
- processo externo inexistente no Android;
- memória limitada;
- remote control sem teclado;
- DNS/TLS diferente;
- permissões de storage.

## UI para TV

- labels curtos e claros;
- navegação por controle remoto;
- foco previsível;
- nenhuma dependência de hover;
- diálogos mínimos;
- imagens otimizadas.

## Desempenho

Fire TV e caixas modestas exigem paginação, poucas threads e baixo uso de memória. Teste instalação limpa, primeiro carregamento e cache quente.

## Dependências

Prefira Python puro e módulos Kodi oficiais. Binários exigem estratégia multiplataforma explícita.

## Teste real

Emulador ou desktop não substitui teste em pelo menos um dispositivo Android/TV quando esse é alvo principal.
