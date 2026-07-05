---
name: python-architecture
title: "Arquitetura Python Modular"
description: "Define limites claros entre domínio, infraestrutura, persistência, providers e apresentação."
domain: "python"
triggers:
  - "arquitetura Python"
  - "organizar módulos"
  - "separar responsabilidades"
  - "refatorar arquivo grande"
---

# Arquitetura Python Modular

## Estrutura recomendada

```text
resources/lib/
├── core/          # bootstrap, configuração, erros, logging
├── domain/        # entidades, tipos e regras puras
├── application/   # casos de uso e orquestração
├── providers/     # integrações externas
├── persistence/   # SQLite, repositórios e migrações
├── presentation/  # adaptadores Kodi e view models
└── utils/         # utilitários realmente genéricos
```

## Regras de dependência

- domínio não importa Kodi, HTTP ou SQLite;
- aplicação depende de interfaces, não de detalhes concretos;
- providers convertem respostas externas em modelos internos;
- persistência não cria diálogos nem itens de UI;
- apresentação não executa SQL e não conhece detalhes de autenticação.

## Entry point fino

O entry point deve apenas:

1. ler `sys.argv`;
2. construir dependências;
3. despachar a rota;
4. converter erro final em log/UI.

Não concentre centenas de linhas de regra de negócio em `main.py` ou `default.py`.

## Interfaces

Em projetos compatíveis com runtimes mais antigos, use protocolos simples ou classes abstratas com moderação. O objetivo é tornar dependências substituíveis em testes, não criar camadas cerimoniais.

## Critérios de módulo

Um módulo merece existir quando representa uma responsabilidade estável. Evite:

- `helpers.py` como depósito universal;
- ciclos de importação;
- singletons globais ocultos;
- imports com efeitos colaterais que criam banco ou fazem rede.

## Validação

Desenhe o grafo de imports. Se UI for necessária para testar domínio ou SQLite, os limites ainda estão errados.
