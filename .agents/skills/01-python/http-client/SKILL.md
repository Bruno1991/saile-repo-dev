---
name: http-client
title: Cliente HTTP resiliente
skill_id: 01.06
category: python
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Cliente HTTP resiliente

## Missão

Centralizar timeout, headers, erros, retries limitados e parsing JSON.

## Quando ativar

Ative esta skill quando a tarefa envolver **cliente http resiliente** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Definir timeouts**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Usar https quando disponível**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Validar status**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Limitar retries**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Normalizar resposta**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Definir timeouts foi executado e possui evidência verificável.
- [ ] Usar https quando disponível foi executado e possui evidência verificável.
- [ ] Validar status foi executado e possui evidência verificável.
- [ ] Limitar retries foi executado e possui evidência verificável.
- [ ] Normalizar resposta foi executado e possui evidência verificável.
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
