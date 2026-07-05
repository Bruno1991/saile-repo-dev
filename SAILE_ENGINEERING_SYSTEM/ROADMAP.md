# Roadmap de Engenharia SAILE

## Fase 0 — Fundação

- integrar este sistema ao repositório;
- inventariar código e contratos existentes;
- validar IDs, versões, rotas e settings;
- registrar baseline no `PROJECT_STATUS.md`;
- aceitar ou substituir ADRs iniciais.

## Fase 1 — Runtime mínimo confiável

- bootstrap e roteamento determinísticos;
- menus principais e settings;
- logging com redaction;
- banco versionado com migrações;
- health check local;
- build e instalação reproduzíveis.

## Fase 2 — Provider Xtream

- autenticação e capability check;
- categorias live, VOD e séries;
- paginação ou carregamento controlado;
- cache com TTL e fallback;
- playback e erros normalizados;
- testes de contrato com fixtures sanitizadas.

## Fase 3 — Perfis e estado local

- perfis locais;
- favoritos;
- histórico e progresso;
- política de retenção;
- backup e recuperação do banco.

## Fase 4 — Música

- provider autorizado;
- busca, detalhes e filas;
- compatibilidade de playback;
- tratamento de limites de API;
- persistência mínima de metadados permitidos.

## Fase 5 — Providers adicionais de vídeo

- contrato comum;
- fontes configuradas pelo usuário;
- conteúdo autorizado;
- resolução local segura;
- isolamento de falhas e dependências opcionais.

## Fase 6 — Qualidade multiplataforma

- matriz Kodi/dispositivo;
- budgets de desempenho;
- testes em Android/Fire TV e desktop;
- diagnóstico exportável sem segredos;
- hardening de build e supply chain.

## Critério de avanço

Nenhuma fase avança por quantidade de código. Avança quando critérios de aceitação, testes, compatibilidade e documentação possuem evidência.
