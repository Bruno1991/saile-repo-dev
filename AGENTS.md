# AGENTS.md — Protocolo Raiz do SAILE

Este arquivo é vinculante para qualquer agente que opere no repositório.

## Inicialização obrigatória

Antes de alterar qualquer arquivo:

1. leia `AGENT_CONSTITUTION.md`;
2. leia `SAILE_MASTER_SPEC.md`;
3. leia `PROJECT_STATUS.md`;
4. identifique a tarefa, o domínio e os contratos afetados;
5. carregue as skills adequadas por meio de `SKILLS_INDEX.md`;
6. leia `docs/00-governance/DOCUMENT_UPDATE_MATRIX.md`;
7. produza um plano de mudança curto e verificável.

## Regras de localização

- `.agents/`: skills e instruções; nunca código de produção;
- `docs/`: verdade técnica específica do SAILE;
- `plugin.video.saile.mc/`: add-on de produção;
- `repository.saile/`: add-on de repositório;
- `tests/`: testes e fixtures sem segredos;
- `tools/`: build, validação e manutenção;
- `github/` ou `zips/`: artefatos gerados, conforme a arquitetura vigente.

## Regras de mudança

- preserve IDs, rotas, schema, nomes de settings e contratos públicos;
- não reescreva módulos inteiros sem necessidade demonstrada;
- nunca use tokens encontrados em `.env` sem autorização explícita;
- nunca publique `.env`, credenciais Xtream, chaves de API, cookies ou URLs autenticadas;
- não invente comportamento do Kodi; consulte a documentação da versão-alvo;
- não execute chamadas de rede na camada de UI;
- toda alteração de schema exige migração, teste e atualização documental;
- toda correção de bug exige teste de regressão quando tecnicamente possível;
- todo release exige validação do ZIP, XML, versão, hashes e changelog.

## Entrega obrigatória

Ao concluir, informe:

- arquivos criados, modificados e removidos;
- motivo técnico;
- contratos preservados;
- testes e validadores executados;
- resultados observados;
- riscos, limitações e testes não executados;
- atualização realizada em `PROJECT_STATUS.md`.

A palavra “concluído” só pode ser usada quando os quality gates aplicáveis tiverem evidência.
