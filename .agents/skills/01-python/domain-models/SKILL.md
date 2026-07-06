---
name: domain-models
title: Modelos de domínio
skill_id: 01.03
category: python
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Modelos de domínio

## Missão

Representar canal, filme, série, episódio, faixa e playlist com modelos estáveis.

## Quando ativar

Ative esta skill quando a tarefa envolver **modelos de domínio** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Definir identidade**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Separar dado bruto e normalizado**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Usar dataclasses**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Validar campos mínimos**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Manter serialização explícita**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Definir identidade foi executado e possui evidência verificável.
- [ ] Separar dado bruto e normalizado foi executado e possui evidência verificável.
- [ ] Usar dataclasses foi executado e possui evidência verificável.
- [ ] Validar campos mínimos foi executado e possui evidência verificável.
- [ ] Manter serialização explícita foi executado e possui evidência verificável.
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
