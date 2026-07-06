---
name: metadata-fallbacks
title: Fallbacks de metadados
skill_id: 07.09
category: metadata
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Fallbacks de metadados

## Missão

Priorizar provider, TMDB e assets locais de forma determinística.

## Quando ativar

Ative esta skill quando a tarefa envolver **fallbacks de metadados** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Definir precedência**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Não substituir valor por vazio**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Marcar origem**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Usar fallback local**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Registrar baixa confiança**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

## Regras específicas do projeto

- TMDB enriquece filmes e séries; não é fonte de streams nem substitui os IDs do provedor.
- Busca de metadados usa normalização de título, ano e tipo; resultados incertos não sobrescrevem dados confiáveis.
- Capas e sinopses têm cache com TTL e fallback para artwork do provedor.
- Um token embarcado em addon local público não é secreto; usar credencial dedicada e nunca reutilizar token privilegiado.

## Contrato de saída

- Lista de arquivos e componentes afetados.
- Contratos de entrada, saída e erro.
- Decisões e trade-offs relevantes.
- Passos de implementação em ordem segura.
- Testes, comandos ou inspeções usados como evidência.

## Critérios de aceitação

- [ ] Definir precedência foi executado e possui evidência verificável.
- [ ] Não substituir valor por vazio foi executado e possui evidência verificável.
- [ ] Marcar origem foi executado e possui evidência verificável.
- [ ] Usar fallback local foi executado e possui evidência verificável.
- [ ] Registrar baixa confiança foi executado e possui evidência verificável.
- [ ] Nenhum segredo foi incluído em código, documentação de exemplo, log ou artefato.
- [ ] A mudança respeita as fronteiras sRepo/sTv/sFy e continua local-first.
- [ ] O agente informa explicitamente o que não conseguiu verificar.

## Anti-padrões

- Aceitar primeiro resultado por título apenas.
- Buscar tmdb em cada renderização.
- Substituir artwork válido por vazio.
- Logar token.

## Encerramento

A skill só é considerada aplicada quando existe evidência de validação. Explicações sem arquivo, teste, log, consulta, inspeção do ZIP ou reprodução controlada não constituem conclusão.
