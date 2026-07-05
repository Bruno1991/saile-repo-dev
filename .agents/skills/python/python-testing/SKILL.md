---
name: python-testing
title: "Testes Python para Código Integrado ao Kodi"
description: "Cria testes úteis isolando módulos Kodi e dependências externas."
domain: "python"
triggers:
  - "testes"
  - "pytest"
  - "unittest"
  - "mock Kodi"
  - "regressão"
---

# Testes Python para Código Integrado ao Kodi

## Pirâmide prática

1. muitos testes de domínio e parsing;
2. testes de repositório SQLite com banco temporário;
3. testes de adaptadores com stubs de Kodi/HTTP;
4. poucos testes manuais end-to-end no Kodi real.

## Isolamento

Código de domínio não deve importar `xbmc`. Para adaptadores Kodi, injete funções ou use stubs no ambiente de teste.

## Casos essenciais

- parsing de rota e parâmetros ausentes;
- transformação de payload incompleto;
- timeout e erro HTTP;
- criação e migração de banco;
- deduplicação;
- expiração de cache;
- construção de URL de playback;
- sanitização de logs.

## Banco temporário

Use diretório temporário real para testar WAL, arquivos auxiliares e migrações. `:memory:` é útil, mas não reproduz todos os comportamentos de arquivo.

## Fixtures

Payloads devem ser mínimos e anonimizados. Não grave respostas completas contendo credenciais ou conteúdo protegido.

## Teste de contrato

Providers diferentes devem produzir o mesmo modelo interno esperado pelos casos de uso.

## End-to-end

Mantenha um roteiro manual com versão do Kodi, plataforma, instalação limpa, configuração, navegação e playback.
