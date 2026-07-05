# System Architecture

## Contexto

```text
User → Kodi UI → SAILE Application → Domain Contracts
                                  ↘ SQLite
                                  ↘ Provider Adapters → Third-party APIs
                                  ↘ Kodi Playback Gateway
```

## Componentes

### Presentation

Interpreta `sys.argv`, constrói diretórios, `ListItem`, dialogs e player. Não contém SQL, autenticação de provider ou regra de catálogo.

### Application

Casos de uso: listar categorias, buscar, detalhar, sincronizar, favoritar, registrar progresso e resolver playback.

### Domain

Modelos imutáveis ou controlados: `MediaItem`, `Category`, `Series`, `Episode`, `Profile`, `PlaybackSource`, `ProviderError`, `Page`.

### Infrastructure

Clients HTTP, adapters de providers, repositórios SQLite, filesystem Kodi, logging e relógio.

## Regra de dependência

Presentation e infrastructure dependem de contratos internos. Domain não depende de Kodi, HTTP ou SQLite.

## Processo de inicialização

1. obter contexto Kodi;
2. carregar configuração sem logar segredos;
3. abrir banco e aplicar migrações;
4. registrar providers disponíveis;
5. interpretar rota;
6. executar caso de uso;
7. renderizar resposta;
8. fechar recursos.

## Falhas

Exceções externas são convertidas em erros tipados. A fronteira da UI registra contexto sanitizado e mostra mensagem adequada. Exceções de programação não são silenciadas como “sem resultados”.
