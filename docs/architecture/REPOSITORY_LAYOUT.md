# Estrutura oficial do monorepo

Esta é a estrutura física obrigatória do projeto. A pasta `.agents/` contém apenas
instruções para o agente; código executável vive em `addons/`, ferramentas em `tools/`
e testes em `tests/`.

```text
saile-repo-dev/
├── .agents/skills/
├── .github/workflows/
├── addons/
│   ├── repository.srepo/
│   ├── plugin.video.stv/
│   └── plugin.audio.sfy/
├── artwork/generic/
├── docs/
├── examples/
├── schemas/
├── site/                       # gerado pelo build
├── templates/
├── tests/
├── tools/
├── .env.example
├── .gitignore
├── AGENTS.md
├── Makefile
├── README.md
└── pyproject.toml
```

## Regras

1. `.env` e `.vscode/` são locais e não fazem parte do pacote nem do Git.
2. Cada add-on é autocontido e tem seu próprio `addon.xml`.
3. `plugin.video.stv` e `plugin.audio.sfy` não importam código um do outro.
4. Bancos SQLite são criados no perfil do add-on em tempo de execução, nunca no Git.
5. `site/` é saída gerada para o GitHub Pages.
6. `artwork/generic/` é a origem dos placeholders; o runtime usa cópias em `addons/`.
