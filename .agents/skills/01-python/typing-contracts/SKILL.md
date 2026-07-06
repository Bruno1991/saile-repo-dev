---
name: typing-contracts
title: Tipagem e contratos
skill_id: 01.02
category: python
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Tipagem e contratos

## Missão

Usar tipos para tornar payloads externos e respostas internas verificáveis.

## Quando ativar

Ative esta skill quando a tarefa envolver **tipagem e contratos** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Tipar funções públicas**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Usar protocol quando útil**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Normalizar optional**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Evitar any propagado**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Executar checagem estática fora do kodi**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Tipar funções públicas foi executado e possui evidência verificável.
- [ ] Usar protocol quando útil foi executado e possui evidência verificável.
- [ ] Normalizar optional foi executado e possui evidência verificável.
- [ ] Evitar any propagado foi executado e possui evidência verificável.
- [ ] Executar checagem estática fora do kodi foi executado e possui evidência verificável.
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
