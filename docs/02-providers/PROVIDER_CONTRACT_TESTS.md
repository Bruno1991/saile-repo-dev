# Provider Contract Tests

Todo provider deve passar a mesma suíte comportamental:

1. identidade e capabilities estáveis;
2. configuração ausente produz `ConfigurationError`;
3. autenticação falha não vaza segredo;
4. categorias e itens retornam modelos válidos;
5. payload parcial não causa `KeyError` não tratado;
6. busca sanitiza entrada e limites;
7. playback retorna `PlaybackSource` válido ou erro tipado;
8. timeout e rate limit são distintos;
9. cancelamento interrompe operação com segurança;
10. logs e exceptions passam por redaction.

Testes de contrato usam fake transport ou fixtures sanitizadas. Testes live são separados e opt-in.
