# Threat Model

## Ativos

Credenciais de providers, banco local, perfis, histórico, arquivos do add-on, pipeline de release e confiança do usuário.

## Fronteiras

- entrada de settings;
- respostas remotas;
- rotas do plugin;
- filesystem do perfil;
- ZIP/repositório de atualização;
- dependências e GitHub Actions.

## Ameaças principais

- segredo em log/commit;
- SQL injection ou payload malformado;
- URL manipulada/SSRF;
- path traversal e sobrescrita;
- resposta remota causando memória excessiva;
- ZIP contaminado;
- atualização adulterada;
- dependência comprometida;
- corrupção do banco após desligamento;
- feature opcional expondo rede local sem consentimento.

## Controles

Validação, parametrização, allowlist de esquemas, limites, timeouts, redaction, menor privilégio, checksums, revisão de dependências, backup e capability detection.
