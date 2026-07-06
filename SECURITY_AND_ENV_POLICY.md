# Política de `.env`, APIs e segredos

## Classificação

| Valor | Onde pode existir | Pode ir para Git? | Pode ir no ZIP? |
|---|---|---:|---:|
| GitHub PAT | `.env` local ou GitHub Secret | não | não |
| `GITHUB_TOKEN` de Actions | contexto do workflow | não | não |
| TMDB bearer token dedicado | `.env` local; estratégia runtime documentada | não como segredo real | somente se o risco for aceito e a credencial for dedicada |
| Xtream host/usuário/senha | settings do usuário no Kodi | não | não |
| cookies do yt-dlp | armazenamento local do usuário, opcional | não | não |
| URLs temporárias de mídia | memória/cache curtíssimo | não | não |

## Limitação inevitável do cliente local

Um segredo usado diretamente por software distribuído ao usuário pode ser extraído. Como o projeto não terá backend próprio, o agente não deve fingir que um token TMDB embutido permanece secreto. A opção preferida é permitir token do usuário. Caso o projeto forneça um token padrão, ele deve ser dedicado, de baixo impacto, monitorado e substituível.

## GitHub

O PAT de administração serve apenas para operações locais autorizadas. Em CI, preferir o `GITHUB_TOKEN` automático com permissões mínimas (`contents: read`, `pages: write`, `id-token: write`) e ambientes protegidos. Nenhum addon precisa falar com a API GitHub para funcionar; ele acessa somente os arquivos estáticos do repositório.

## `.env.example`

O arquivo de exemplo contém nomes e comentários, nunca valores reais:

```dotenv
TMDB_BEARER_TOKEN=
GITHUB_PAT=
SREPO_PAGES_BASE_URL=
```

## Redação de logs

Mascarar chaves e query params como `username`, `password`, `api_key`, `token`, `sig`, `expire`, `authorization` e cookies. Não registrar resposta integral de endpoints de autenticação.
