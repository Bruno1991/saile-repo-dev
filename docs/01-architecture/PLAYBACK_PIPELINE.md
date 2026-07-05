# Playback Pipeline

## Etapas

1. receber apenas identificadores necessários;
2. carregar item e configuração no application service;
3. solicitar ao provider uma `PlaybackSource`;
4. validar URL, esquema, expiração, headers e propriedades;
5. criar `xbmcgui.ListItem(path=...)` no gateway;
6. aplicar MIME/propriedades sem registrar segredo;
7. concluir por `xbmcplugin.setResolvedUrl` na rota de plugin;
8. observar início e registrar erro normalizado.

## Regras

- URL autenticada não deve permanecer em histórico, banco ou log sem necessidade;
- não executar resolução remota ao montar menus;
- playback live e VOD possuem semânticas distintas;
- inputstream adaptativo é capability opcional;
- retry não pode disparar múltiplas sessões desnecessárias;
- fonte expirada deve ser resolvida novamente.

## Critérios de teste

Sucesso, credencial inválida, timeout, cancelamento, URL expirada, MIME ausente, item removido, cache stale e retorno inválido do provider.
