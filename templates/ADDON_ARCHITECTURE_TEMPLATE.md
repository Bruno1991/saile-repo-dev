# Arquitetura do Add-on

## Identidade

- ID:
- Nome:
- Versão:
- Kodi mínimo:
- Plataformas:

## Escopo

### Incluído

### Fora do escopo

## Fluxo de execução

```text
Kodi -> Router -> Use Case -> Provider/Repository -> View/Playback
```

## Componentes

| Componente | Responsabilidade | Dependências permitidas |
|---|---|---|
| Entry point | bootstrap e dispatch | core, router |
| Presentation | API Kodi | application |
| Application | orquestração | domain, ports |
| Provider | integração externa | HTTP/config |
| Persistence | SQLite/cache | domain |
| Domain | regras e modelos | biblioteca padrão |

## Rotas públicas

| Action | Parâmetros | Tipo | Finalização |
|---|---|---|---|
| home | — | diretório | endOfDirectory |
| play | item_id | playback | setResolvedUrl |

## Dados e cache

- banco:
- schema version:
- TTLs:
- dados permanentes:
- recuperação:

## Segurança

- segredos:
- logs:
- TLS:
- permissões:

## Compatibilidade

- APIs dependentes de versão:
- dependências binárias:
- limitações:
