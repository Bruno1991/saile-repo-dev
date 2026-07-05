---
name: kodi-playback-resolution
title: "Playback e setResolvedUrl"
description: "Resolve streams corretamente, configura headers e trata falhas de reprodução."
domain: "kodi"
triggers:
  - "playback Kodi"
  - "setResolvedUrl"
  - "stream URL"
  - "IsPlayable"
---

# Playback e setResolvedUrl

## Fluxo preferido

1. usuário seleciona item reproduzível;
2. Kodi chama rota `play`;
3. add-on resolve URL final ou manifest;
4. cria `ListItem(path=url)`;
5. adiciona propriedades necessárias;
6. chama `setResolvedUrl` uma vez.

```python
play_item = xbmcgui.ListItem(path=stream_url)
xbmcplugin.setResolvedUrl(handle, True, play_item)
```

## Falha

Em erro:

```python
xbmcplugin.setResolvedUrl(handle, False, xbmcgui.ListItem())
```

Registre causa e mostre mensagem adequada.

## Headers

Quando Kodi aceita headers anexados à URL, construa-os com codificação correta e nunca registre valores sensíveis. Prefira mecanismos suportados pelo protocolo/add-on usado.

## InputStream Adaptive

Para HLS/DASH/DRM avançado, detecte e declare dependência apropriada, configure MIME type e propriedades conforme documentação da versão-alvo. Não invente propriedades.

## URL direta versus rota

Use rota de resolução quando:

- URL expira;
- exige token;
- precisa selecionar qualidade;
- precisa atualizar sessão;
- requer validação antes de tocar.

## Monitoramento

Não considere sucesso apenas porque `setResolvedUrl` foi chamado. Teste no player real e registre falhas de resolução separadas de falhas do decoder/rede.
