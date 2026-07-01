# Biblioteca de skills para desenvolvimento do Saile Media Center

Esta biblioteca é o manual operacional do agente de IA e dos desenvolvedores. Antes de modificar qualquer arquivo, o agente deve escolher quais skills se aplicam e seguir suas regras.

## Skill 01 - Ler o roadmap antes de codar

Objetivo: impedir que o agente fuja da lógica visual definida.

Entrada obrigatória:

- `docs/00_ROADMAP_IMPLEMENTATION.md`.
- `docs/assets/roadmap-saile-media-center.png`.

Regras:

1. Todo menu criado deve existir no roadmap ou estar documentado como suporte técnico.
2. Adulto, Kids e Configurações são portas de entrada principais.
3. SaileTV, SaileFy e sTorrent são apps internos, não addons separados.
4. SQLite é obrigatório para estado local.

Checklist:

- A mudança respeita os três apps?
- A mudança respeita Kids sem SaileFy e sem sTorrent?
- A mudança preserva favoritos e continuar assistindo?

## Skill 02 - Roteamento Kodi seguro

Objetivo: criar rotas sem quebrar o plugin.

Arquivos principais:

- `plugin.video.saile.mc/main.py`.
- `plugin.video.saile.mc/resources/lib/router.py`.
- `plugin.video.saile.mc/resources/lib/ui.py`.

Regras:

1. `main.py` deve apenas preparar path e chamar o router.
2. Toda action deve ser validada.
3. Query string deve usar URL encode.
4. Diretórios precisam chamar `xbmcplugin.endOfDirectory`.
5. Itens reproduzíveis precisam de `IsPlayable=true`.

Checklist:

- A rota tem fallback?
- O item tem título claro?
- O item tem ícone?
- O player recebe URL resolvida?

## Skill 03 - SQLite local-first

Objetivo: preservar estado local sem servidor.

Arquivo principal:

- `plugin.video.saile.mc/resources/lib/storage.py`.

Regras:

1. Sempre usar `sqlite3` da biblioteca padrão.
2. Sempre usar parâmetros SQL, nunca interpolar valores do usuário.
3. Criar índices quando a consulta virar frequente.
4. Não salvar senha de provider em tabela própria; configurações sensíveis ficam no sistema de settings do Kodi.
5. Payload JSON no banco deve ser opcional e resiliente.

Checklist:

- A migração é idempotente?
- O banco é criado no perfil do addon?
- Existe unique key para evitar duplicados?

## Skill 04 - Provider Xtream

Objetivo: integrar IPTV sem acoplar UI à API.

Arquivo principal:

- `plugin.video.saile.mc/resources/lib/providers/xtream.py`.

Regras:

1. Ler host, usuário e senha das configurações do Kodi.
2. Normalizar host com scheme HTTP/HTTPS.
3. Usar timeout.
4. Tratar JSON inválido.
5. Não quebrar se o servidor retornar lista vazia.
6. Não salvar senha no SQLite.

Fluxos:

- Live categories.
- VOD categories.
- Series categories.
- Live streams.
- VOD streams.
- Series list.
- Seasons/episodes quando disponível.

## Skill 05 - Provider YouTube/SaileFy

Objetivo: listar músicas e metadados via YouTube Data API.

Arquivo principal:

- `plugin.video.saile.mc/resources/lib/providers/youtube.py`.

Regras:

1. Exigir API key para chamadas reais.
2. Não extrair stream do YouTube por scraping.
3. Para playback, preferir URL compatível com addon oficial do YouTube ou resolver autorizado futuro.
4. Cachear resultados úteis no SQLite quando fizer sentido.
5. Top Brasil e Top Mundo devem ser consultas explícitas, não listas inventadas.

## Skill 06 - Provider sTorrent genérico

Objetivo: permitir integração futura sem embutir pirataria.

Arquivo principal:

- `plugin.video.saile.mc/resources/lib/providers/torrent_json.py`.

Regras:

1. Nenhum endpoint pirata hardcoded.
2. Nenhum bypass anti-bloqueio.
3. Nenhuma fonte pornográfica embutida.
4. A API deve ser configurada pelo usuário.
5. O adapter aceita JSON em formatos previsíveis e normaliza para itens internos.
6. Só reproduzir se houver `stream_url`, `play_url`, `url` ou magnet resolvível pelo ambiente Kodi.

Formato JSON recomendado para API futura:

```json
{
  "items": [
    {
      "id": "movie-1",
      "title": "Título",
      "type": "movie",
      "year": 2026,
      "plot": "Sinopse",
      "artwork": "https://.../poster.jpg",
      "stream_url": "https://.../video.mp4",
      "magnet": "magnet:?xt=urn:btih:...",
      "category": "lancamentos",
      "tmdb_rating": 8.2
    }
  ]
}
```

## Skill 07 - Perfis, PIN e Kids

Objetivo: manter controle dos pais funcional.

Arquivos:

- `plugin.video.saile.mc/resources/lib/profiles.py`.
- `plugin.video.saile.mc/resources/lib/router.py`.
- `plugin.video.saile.mc/resources/settings.xml`.

Regras:

1. PIN deve aceitar somente números.
2. PIN deve ter 4 a 6 dígitos.
3. Kids não pode acessar SaileFy.
4. Kids não pode acessar sTorrent.
5. Configurações exigem PIN quando PIN existir.

## Skill 08 - Favoritos e continuar assistindo

Objetivo: entregar a navegação do roadmap.

Regras:

1. Favoritos são por perfil.
2. Continuar assistindo é por perfil.
3. O item salvo precisa guardar provider, tipo, id externo e payload.
4. Duplicatas devem atualizar, não criar outra linha.

## Skill 09 - Build GitHub Pages

Objetivo: gerar repositório instalável pelo Kodi.

Arquivo:

- `tools/build_repo.py`.

Saídas obrigatórias:

- `addons.xml`.
- `addons.xml.md5`.
- `index.html`.
- `zips/plugin.video.saile.mc/plugin.video.saile.mc-<version>.zip`.
- `zips/repository.saile/repository.saile-<version>.zip`.

Regras:

1. O zip deve conter a pasta do addon na raiz do zip.
2. `addons.xml` deve concatenar os `addon.xml` dos addons.
3. Checksum deve bater com `addons.xml`.
4. Não incluir `.env`, banco, logs, dumps ou cache.

## Skill 10 - Gitignore blindado e preflight

Objetivo: evitar vazamento do token que existe no `.env` local.

Arquivos:

- `.gitignore`.
- `docs/04_GITIGNORE_BLINDADO.md`.
- `tools/preflight_no_secrets.py`.

Regras:

1. Rodar preflight antes de commit.
2. Se `.env` já estiver rastreado, remover do índice com `git rm --cached .env`.
3. Nunca mostrar token em logs.
4. Nunca criar arquivo de backup com segredo.

## Skill 11 - Teste mínimo de release

Objetivo: garantir que o pacote abre no Kodi.

Checklist:

1. `python tools/preflight_no_secrets.py` passa.
2. `python tools/build_repo.py --repo-url https://bruno1991.github.io/saile-repo-dev/` passa.
3. Zip do plugin instala no Kodi.
4. Addon abre.
5. Tela Adulto/Kids/Configurações aparece.
6. Kids não mostra SaileFy/sTorrent.
7. Configurações abrem.
8. SaileTV informa para configurar quando Xtream está vazio.
9. SaileFy informa para configurar quando API key está vazia.
10. sTorrent informa para configurar quando API URL está vazia.

## Skill 12 - Entrega de código pelo Antigravity

Objetivo: evitar alterações quebradas e incompletas.

Regras:

1. Sempre informar caminho completo do arquivo modificado.
2. Entregar arquivo completo quando alterar estrutura relevante.
3. Não renomear arquivos sem justificar.
4. Não apagar módulo sem listar impacto.
5. Não misturar refactor grande com feature nova.
6. Manter documentação atualizada quando mudar regra de produto.
