---
name: safe-change-management
title: "Gestão Segura de Mudanças"
description: "Controla impacto, compatibilidade, reversão e prevenção de regressões."
domain: "core"
triggers:
  - "refatoração"
  - "mudança estrutural"
  - "migração"
  - "alteração de API interna"
---

# Gestão Segura de Mudanças

## Classificação de risco

Classifique a mudança:

- **baixo**: texto, documentação, validação isolada;
- **médio**: comportamento interno preservando contratos;
- **alto**: esquema SQLite, roteamento, playback, autenticação, empacotamento;
- **crítico**: migração destrutiva, credenciais, atualização automática, publicação pública.

Quanto maior o risco, maior deve ser a evidência de validação.

## Técnica de alteração incremental

1. Capture o comportamento atual com teste, exemplo reproduzível ou log.
2. Faça uma alteração por responsabilidade.
3. Execute validação imediatamente.
4. Revise o diff por efeitos colaterais.
5. Só então prossiga para o próximo arquivo.

## Compatibilidade

Preserve, salvo decisão explícita:

- IDs de add-on;
- nomes de actions e parâmetros de rota;
- IDs de settings;
- nomes e significado de colunas;
- formato do cache persistido;
- paths `plugin://` usados em favoritos;
- versão mínima de Python/Kodi.

## Reversibilidade

Mudanças de alto risco devem possuir pelo menos uma estratégia:

- migração reversa;
- backup antes da alteração;
- feature flag;
- fallback para implementação anterior;
- reconstrução segura de cache descartável.

## Revisão final

Procure por:

- arquivos esquecidos na antiga arquitetura;
- imports mortos;
- referências a nomes antigos;
- rotas que deixaram de ser alcançáveis;
- settings não lidos;
- tabelas sem migração;
- documentação divergente.
