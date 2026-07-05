---
name: kodi-security-legal
title: "Segurança, Privacidade e Conformidade Kodi"
description: "Protege usuários e limita integrações a usos autorizados."
domain: "kodi"
triggers:
  - "segurança Kodi"
  - "legalidade addon"
  - "privacidade"
  - "conteúdo remoto"
---

# Segurança, Privacidade e Conformidade Kodi

## Princípios

- mínimo de dados;
- consentimento e transparência;
- nenhum segredo em log;
- TLS e hosts validados;
- dependências auditáveis;
- nenhuma execução de código remoto;
- conteúdo e APIs usados de forma autorizada.

## Fontes de conteúdo

O agente deve confirmar que o add-on acessa conteúdo próprio, licenciado, público de forma legítima ou fornecido por serviço autorizado pelo usuário. Não criar mecanismos destinados a burlar DRM, paywall, autenticação ou bloqueios legais.

## Atualizações

Repositórios devem usar HTTPS. O add-on não deve baixar e executar scripts fora do sistema de atualização do Kodi.

## Privacidade

Histórico, favoritos e perfis são dados do usuário. Armazene localmente, documente exportação/limpeza e não envie telemetria sem requisito e consentimento claros.

## Credenciais

- settings locais;
- mascaramento em UI/log;
- não duplicar no banco;
- não incluir em favoritos/rotas;
- invalidar sessões corretamente.

## Bibliotecas

Verifique licença e origem. Add-ons oficiais exigem código distribuível e compatibilidade com regras do repositório.
