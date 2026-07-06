---
name: url-query-safety
title: URLs e query strings seguras
skill_id: 01.07
category: python
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# URLs e query strings seguras

## Missão

Montar endpoints sem corromper encoding e sem vazar parâmetros sensíveis.

## Quando ativar

Ative esta skill quando a tarefa envolver **urls e query strings seguras** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Normalizar host**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Usar urlencode**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Redigir logs**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Validar esquema**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Evitar dupla barra**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Normalizar host foi executado e possui evidência verificável.
- [ ] Usar urlencode foi executado e possui evidência verificável.
- [ ] Redigir logs foi executado e possui evidência verificável.
- [ ] Validar esquema foi executado e possui evidência verificável.
- [ ] Evitar dupla barra foi executado e possui evidência verificável.
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
