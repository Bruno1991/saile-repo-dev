# AGENTS.md — Contrato operacional do agente

## Identidade do sistema

O agente trabalha em um monorepo chamado **sRepo**, responsável por `repository.srepo`, `plugin.video.stv` e `plugin.audio.sfy`.

## Regra de localização

- `.agents/` contém apenas skills, políticas e instruções.
- Código de produção vive em `addons/<addon-id>/`.
- Ferramentas de build vivem em `tools/`.
- Saída gerada vive em `dist/` ou `site/` e nunca é editada manualmente.
- Artes temporárias de origem vivem em `artwork/generic/`; o código usa cópias dentro de `addons/<addon-id>/`.

## Fluxo obrigatório por tarefa

1. Ler a constituição e a skill correspondente.
2. Inspecionar os arquivos reais antes de propor alteração.
3. Produzir plano por arquivo.
4. Implementar a menor mudança coerente.
5. Executar validações apropriadas.
6. Atualizar documentação/ADR quando a arquitetura mudar.
7. Informar caminhos completos, arquivos criados, modificados e removidos.
8. Ao criar o scaffolding de um add-on, copiar os assets definidos em `artwork/artwork-manifest.json` e validar que abrem corretamente.

## Formato de entrega

Toda entrega deve conter:

- diretório de trabalho;
- caminhos exatos;
- arquivos completos quando solicitado;
- comandos em ordem;
- resultado real dos testes;
- riscos ou itens não verificados;
- instrução de rollback quando aplicável.

## Proibições

- Não criar o addon dentro de `.agents`.
- Não inventar testes executados.
- Não apagar banco para resolver migração.
- Não adicionar microserviço ou backend obrigatório.
- Não registrar senha Xtream, cookie, token TMDB, PAT GitHub ou URL assinada.
- Não usar emojis como assets de UI.
- Não publicar add-on sem `icon.png` e `fanart.jpg`; na ausência de arte final, usar os assets genéricos do pacote.
- Não referenciar diretamente `artwork/generic/` no runtime; copiar para o diretório real do add-on.
- Não misturar chamadas remotas dentro de renderização de cada item.
- Não empacotar `.env`, `.git`, `__pycache__`, `.db`, logs ou ferramentas locais.
