---
name: progress-cancellation
title: Progresso e cancelamento
skill_id: 01.10
category: python
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Progresso e cancelamento

## Missão

Tornar sincronizações e buscas longas visíveis e canceláveis.

## Quando ativar

Ative esta skill quando a tarefa envolver **progresso e cancelamento** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Estimar etapas**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Atualizar progresso**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Verificar cancelamento**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Reverter transação**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Não deixar estado parcial**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Estimar etapas foi executado e possui evidência verificável.
- [ ] Atualizar progresso foi executado e possui evidência verificável.
- [ ] Verificar cancelamento foi executado e possui evidência verificável.
- [ ] Reverter transação foi executado e possui evidência verificável.
- [ ] Não deixar estado parcial foi executado e possui evidência verificável.
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
