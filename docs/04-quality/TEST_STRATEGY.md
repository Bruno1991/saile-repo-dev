# Test Strategy

## Pirâmide

- unitários: domínio, parsing, validação, cache e SQL helpers;
- contrato: providers e repositories;
- integração: SQLite real temporário, roteador e gateway fake;
- smoke Kodi: instalação, menus, settings e playback controlado;
- dispositivo: Android/Fire TV e desktop conforme impacto.

## Regras

Testes são determinísticos, sem internet por padrão e sem segredo. Fixtures remotas são sanitizadas. Teste live é opt-in e não bloqueia CI principal. Bugs recebem teste de regressão antes ou junto da correção.

## Cobertura

Percentual não substitui risco. Caminhos críticos exigem casos de sucesso, falha e recuperação.
