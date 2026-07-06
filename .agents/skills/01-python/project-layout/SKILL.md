---
name: project-layout
title: Layout Python modular
skill_id: 01.01
category: python
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Layout Python modular

## Missão

Organizar módulos por domínio, infraestrutura, aplicação e apresentação.

## Quando ativar

Ative esta skill quando a tarefa envolver **layout python modular** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Definir pacote raiz**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Separar domínio de kodi**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Isolar clientes externos**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Isolar persistência**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Evitar imports circulares**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Definir pacote raiz foi executado e possui evidência verificável.
- [ ] Separar domínio de kodi foi executado e possui evidência verificável.
- [ ] Isolar clientes externos foi executado e possui evidência verificável.
- [ ] Isolar persistência foi executado e possui evidência verificável.
- [ ] Evitar imports circulares foi executado e possui evidência verificável.
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
