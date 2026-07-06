---
name: logging-sanitization
title: Logging sanitizado
skill_id: 01.05
category: python
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Logging sanitizado

## Missão

Criar logs úteis sem expor credenciais ou dados temporários.

## Quando ativar

Ative esta skill quando a tarefa envolver **logging sanitizado** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Usar níveis corretos**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Adicionar contexto**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Mascarar segredos**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Evitar payload integral**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Preservar traceback em debug**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- Usar Python 3 compatível com o runtime alvo do Kodi e evitar recursos não suportados por esse runtime.
- Preferir biblioteca padrão e dependências pequenas; toda dependência adicional precisa de justificativa e licença revisada.
- Funções públicas têm tipos, docstrings úteis e contratos claros; erros de domínio não usam exceções genéricas silenciosas.
- Código de rede, banco, domínio, UI e reprodução permanece separado por módulos.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Usar níveis corretos foi executado e possui evidência verificável.
- [ ] Adicionar contexto foi executado e possui evidência verificável.
- [ ] Mascarar segredos foi executado e possui evidência verificável.
- [ ] Evitar payload integral foi executado e possui evidência verificável.
- [ ] Preservar traceback em debug foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Funções gigantes.
- Estado global mutável.
- Capturar `exception` e ignorar.
- Dependência pesada sem necessidade.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
