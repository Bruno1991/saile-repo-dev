# Engineering Constitution

## Qualidade antes de volume

Entregas pequenas, validadas e reversíveis são preferíveis a grandes reescritas. Abstrações só são introduzidas quando reduzem risco ou duplicação real.

## Contratos

Rotas, settings, schema, modelos e interfaces de providers são APIs internas protegidas. Alterações incompatíveis exigem migração ou versão maior conforme política.

## Evidência

Toda decisão técnica deve ser sustentada por código existente, documentação oficial, teste ou medição. “Provavelmente funciona” não é evidência de compatibilidade.

## Observabilidade

Logs devem permitir diagnosticar módulo, operação e causa sem revelar credenciais. Erros de usuário, provider, rede, banco e programação devem ser distinguíveis.

## Sustentabilidade

Dependências precisam de justificativa, licença compatível e impacto conhecido no ZIP. Código deve ser compreensível por humanos e agentes futuros.
