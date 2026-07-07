# Detecção de capacidades

`script.module.saile.core` contém um detector inicial para:

- versão do Python e SQLite;
- sistema operacional e arquitetura;
- SQLite FTS5;
- `resource.images.saile`;
- InputStream Adaptive;
- InputStream FFmpeg Direct.

A futura tela `Diagnóstico do dispositivo` deve exibir resultados sem dados pessoais e orientar recursos indisponíveis. Detecção não deve instalar dependências silenciosamente.
