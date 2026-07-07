# Estrutura oficial do monorepo

```text
saile-repo-dev/
├── .agents/skills/
├── .github/workflows/
├── addons/
│   ├── repository.srepo/
│   ├── resource.images.saile/
│   ├── script.module.saile.core/
│   ├── plugin.video.stv/
│   └── plugin.audio.sfy/
├── artwork/generic/
├── docs/
├── examples/
├── schemas/
├── site/                  # gerado
├── templates/
├── tests/
└── tools/
```

`.agents` nunca contém produção. Plugins não importam um ao outro. O runtime usa `resource.images.saile`, não `artwork/generic`. Bancos ficam no perfil Kodi.
