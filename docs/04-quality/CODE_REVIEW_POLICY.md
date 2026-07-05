# Code Review Policy

Revisão verifica correção, arquitetura, segurança, dados, compatibilidade, testes e clareza. O revisor procura especialmente:

- chamadas de rede/SQL na UI;
- broad `except` escondendo defeitos;
- log de credenciais;
- mudanças de contrato sem migração;
- trabalho em import time;
- path handling nativo incompatível;
- loops sem cancelamento;
- dependência desnecessária;
- código morto e artefato gerado editado manualmente.

Aprovação exige resposta às observações ou justificativa registrada.
