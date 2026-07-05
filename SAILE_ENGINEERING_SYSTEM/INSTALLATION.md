# Instalação no Projeto SAILE

## 1. Backup

Faça commit ou cópia da árvore atual. Não use este pacote para sobrescrever silenciosamente arquivos existentes.

## 2. Copiar

Extraia `SAILE_ENGINEERING_SYSTEM.zip` e copie o conteúdo interno para a raiz do repositório SAILE.

## 3. Mesclar

- preserve `.env` local e mantenha-o ignorado;
- compare `AGENTS.md`, `.gitignore` e workflows existentes;
- copie `.gitignore.recommended` para regras apropriadas do `.gitignore` real;
- não copie o plugin de referência para o diretório de produção;
- mantenha `plugin.video.saile.mc/` e `repository.saile/` fora de `.agents/`.

## 4. Baseline

Execute:

```bash
python tools/validate_engineering_system.py
python tools/project_health.py
```

Depois atualize `PROJECT_STATUS.md`, `DATABASE_SCHEMA.md`, `COMPATIBILITY_MATRIX.md` e `TRACEABILITY_MATRIX.md` com fatos do repositório.

## 5. Ativação do agente

Use `PROMPT_DE_ATIVACAO.md` como mensagem inicial. O agente deve primeiro inventariar, não reestruturar automaticamente.
