# Política de Segurança

## Relato

Vulnerabilidades não devem ser publicadas em issue aberta antes da correção. Use canal privado configurado pelo proprietário do repositório.

## Escopo

- exposição de credenciais;
- execução de código ou comandos não autorizados;
- path traversal;
- SQL injection;
- SSRF ou manipulação insegura de URLs;
- ZIP malformado ou supply-chain compromise;
- logs contendo dados sensíveis;
- corrupção ou perda previsível do banco.

## Regras

Não inclua segredo real em prova de conceito. Preserve evidência mínima, versão, plataforma e passos de reprodução. Correções críticas devem gerar teste de regressão, changelog e orientação de rotação de credenciais quando houver exposição.
