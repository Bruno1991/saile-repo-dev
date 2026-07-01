# SAILE_MASTER_SPEC.md

## 1. Visão do produto

Saile Media Center é um Media Center local-first para Kodi. Ele reúne IPTV, música e streaming indexado em três apps internos controlados por perfis, PIN, favoritos, histórico e SQLite local.

O objetivo não é criar apenas um addon IPTV. O objetivo é criar uma plataforma local de mídia onde cada fonte externa é apenas um provider. O Kodi exibe a interface, chama rotas e entrega itens ao player. A lógica do produto fica em módulos Python internos, testáveis e separados por domínio.

## 2. Restrições absolutas

1. Runtime somente local no dispositivo do usuário.
2. Linguagem do addon: Python.
3. Persistência: SQLite local.
4. Publicação: GitHub Pages com HTML, XML, checksums e zips.
5. Sem servidor próprio obrigatório.
6. Sem token no Git (dados sensíveis devem ser injetados apenas no build local/privado).
7. Sem `.env` no Git.
8. [REMOVIDO] Permitido configurar hardcoded endpoints de torrent e conteúdo adulto para uso estritamente pessoal/privado.
9. [REMOVIDO] Permitido conteúdo adulto explícito via APIs de terceiros.
10. Sem dependência nativa obrigatória no MVP (resolver libs via download em tempo de execução).

## 3. Arquitetura

```text
Kodi UI
  -> Router
     -> Controllers de app
        -> Providers
           -> APIs externas configuradas pelo usuário
        -> SQLite local
     -> Player Kodi
```

Camadas:

- Entrada: `main.py`.
- Roteamento: `resources/lib/router.py`.
- UI: `resources/lib/ui.py`.
- Banco: `resources/lib/storage.py`.
- Perfis e PIN: `resources/lib/profiles.py`.
- Providers: `resources/lib/providers/`.
- Utilitários Kodi: `resources/lib/kodi.py`.

## 4. Domínios

### 4.1 Perfil

Modelo:

```text
Profile
- id
- name
- kind: adult | kids
- avatar
- created_at
```

Regras:

- Adulto pode acessar tudo.
- Kids acessa somente SaileTV.
- Configurações podem exigir PIN.
- PIN deve ter 4 a 6 dígitos.

### 4.2 Favorito

Modelo:

```text
Favorite
- id
- profile_id
- provider
- media_type
- external_id
- title
- artwork
- payload_json
- created_at
```

Regras:

- Favoritos são por perfil.
- O mesmo item não deve duplicar para o mesmo perfil.
- O payload deve guardar dados suficientes para reabrir o item sem refazer a busca quando possível.

### 4.3 Continuar assistindo

Modelo:

```text
ContinueWatching
- id
- profile_id
- provider
- media_type
- external_id
- title
- artwork
- position_seconds
- duration_seconds
- payload_json
- updated_at
```

Regras:

- Atualizar em vez de duplicar.
- Exibir no menu principal e dentro do app correspondente.

### 4.4 Provider

Contrato mínimo:

```text
Provider
- list_categories()
- list_items(category_id)
- search(query)
- resolve_playback(item)
```

Providers atuais:

- Xtream.
- YouTube.
- Torrent JSON genérico.

## 5. Fluxos principais

### 5.1 Inicialização

```text
Abrir addon
  -> iniciar SQLite
  -> garantir perfis padrão
  -> exibir tela de perfil
```

### 5.2 Perfil Adulto

```text
Selecionar Adulto
  -> se PIN existir, pedir PIN
  -> abrir Home
  -> mostrar SaileTV, SaileFy, sTorrent, Continuar assistindo, Favoritos, Configurações
```

### 5.3 Perfil Kids

```text
Selecionar Kids
  -> abrir Home Kids
  -> mostrar somente SaileTV e favoritos permitidos do SaileTV
```

### 5.4 SaileTV

```text
SaileTV
  -> TV ao vivo | VOD | Séries | Busca | Favoritos | Atualizar Conteúdo
```

### 5.5 SaileFy

```text
SaileFy
  -> Top Brasil | Top Mundo | Categorias | Minhas playlists | Busca | Favoritos
```

### 5.6 sTorrent

```text
sTorrent
  -> Lançamentos | Categorias | Ranking TMDB | Busca | Favoritos | Continuar assistindo
```

## 6. Decisões de engenharia

### ADR-001: Kodi é frontend, não plataforma

A lógica do produto não deve ficar presa na UI do Kodi. A UI chama rotas e renderiza listas. Providers, cache, perfis, favoritos e histórico ficam em módulos próprios.

### ADR-002: SQLite é a fonte local de estado

Perfis, favoritos, histórico, cache e indexação local ficam em SQLite. JSON solto só pode ser usado para payload dentro do banco ou configuração do Kodi.

### ADR-003: Provedores são plugáveis

Xtream, YouTube e Torrent JSON devem seguir contrato semelhante. A UI não deve saber se o item veio de IPTV, YouTube ou torrent.

### ADR-004: Sem servidor intermediário

O addon roda no dispositivo do usuário. GitHub Pages apenas hospeda arquivos estáticos de instalação/atualização.

### ADR-005: sTorrent é genérico e seguro

O addon não deve distribuir endpoint de pirataria ou bypass. O usuário configura uma API JSON legal/autorizada.

## 7. Convenções

- IDs de ação usam snake_case.
- Arquivos Python usam snake_case.
- Tabelas SQLite usam snake_case.
- Providers ficam em `resources/lib/providers/`.
- Funções públicas devem ter docstring objetiva.
- Nenhum arquivo deve importar provider diretamente dentro de outro provider.
- Nenhuma UI deve montar SQL manual.

## 8. Critérios de qualidade

- O addon abre sem credenciais e orienta a configurar.
- O addon não quebra se API externa falhar.
- Toda rota inválida volta para Home com mensagem de erro.
- Falha de rede deve ser mostrada em diálogo ou log, nunca em traceback bruto para o usuário.
- Kids não enxerga SaileFy nem sTorrent.
- Build nunca inclui `.env`.
- `tools/preflight_no_secrets.py` deve passar antes do commit.
- `python tools/build_repo.py` deve gerar zips e XML sem erro.
