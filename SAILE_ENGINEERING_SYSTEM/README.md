# SAILE Engineering System

Sistema integrado de engenharia para orientar agentes de programação e desenvolvedores humanos na construção do **SAILE**, uma plataforma de mídia local-first apresentada pelo Kodi.

Este pacote reúne:

- biblioteca de skills para Python, SQLite e Kodi;
- especificação mestre do produto;
- arquitetura e contratos de módulos;
- governança de banco, cache, segurança, testes e releases;
- protocolos de trabalho para agentes;
- templates de engenharia;
- validadores locais;
- workflows de CI para GitHub.

## Instalação

Copie o conteúdo desta pasta para a raiz do repositório SAILE. Mescle arquivos existentes conscientemente; não sobrescreva código funcional sem revisão.

Estrutura esperada após a integração:

```text
SAILE/
├── .agents/
├── .github/
├── docs/
├── templates/
├── tools/
├── tests/
├── plugin.video.saile.mc/
├── repository.saile/
├── AGENTS.md
├── SAILE_MASTER_SPEC.md
└── PROJECT_STATUS.md
```

## Ordem obrigatória de leitura do agente

1. `AGENTS.md`;
2. `AGENT_CONSTITUTION.md`;
3. `SAILE_MASTER_SPEC.md`;
4. `PROJECT_STATUS.md`;
5. `docs/00-governance/SCOPE_AND_NON_GOALS.md`;
6. `docs/01-architecture/SYSTEM_ARCHITECTURE.md`;
7. skills selecionadas em `SKILLS_INDEX.md`;
8. documentos específicos da tarefa.

## Limite de responsabilidade

`.agents/` contém conhecimento operacional. O add-on, o repositório Kodi, os testes e as ferramentas de produção permanecem fora de `.agents/`.

## Validação

Execute na raiz do projeto:

```bash
python tools/validate_engineering_system.py
python tools/project_health.py
```

O primeiro comando valida este sistema documental. O segundo inspeciona o repositório SAILE e gera um relatório proporcional ao que estiver presente.

## Uso responsável

Providers e mecanismos de reprodução devem operar apenas com conteúdo, contas e fontes que o usuário esteja autorizado a acessar. O projeto não deve embutir credenciais, contornar proteções, distribuir catálogos ilícitos ou prometer compatibilidade não testada.
