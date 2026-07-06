---
name: xtream-configuration
title: Configuração Xtream
skill_id: 05.01
category: stv
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Configuração Xtream

## Missão

Ler e validar host, login e senha do sTv sem expor credenciais.

## Quando ativar

Ative esta skill quando a tarefa envolver **configuração xtream** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Normalizar host**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Validar campos**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Testar autenticação**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Mascarar logs**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Abrir settings em ausência**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- sTv é `plugin.video.stv`, cliente pessoal de um único provedor Xtream por perfil do addon.
- Host, usuário e senha vêm das configurações do Kodi; nunca do `.env` distribuído.
- API Xtream é encapsulada por cliente e adaptadores; a UI não monta endpoints diretamente.
- Live, VOD e séries compartilham modelos normalizados, mas mantêm regras de reprodução específicas.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Normalizar host foi executado e possui evidência verificável.
- [ ] Validar campos foi executado e possui evidência verificável.
- [ ] Testar autenticação foi executado e possui evidência verificável.
- [ ] Mascarar logs foi executado e possui evidência verificável.
- [ ] Abrir settings em ausência foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Credenciais no código.
- Urls xtream espalhadas.
- Usar nome como chave primária.
- Repetir download de catálogo a cada abertura.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
