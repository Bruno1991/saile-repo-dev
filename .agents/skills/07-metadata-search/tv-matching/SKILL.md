---
name: tv-matching
title: Correspondência de séries
skill_id: 07.04
category: metadata
version: 1.0.0
applies_to:
  - repository.srepo
  - plugin.video.stv
  - plugin.audio.sfy
---

# Correspondência de séries

## Missão

Encontrar série por nome, ano e tipo preservando temporadas do provider.

## Quando ativar

Ative esta skill quando a tarefa envolver **correspondência de séries** ou quando a mudança tocar diretamente o contrato descrito nesta página.

## Entradas mínimas

- Estado atual do repositório ou arquivos envolvidos.
- Objetivo funcional expresso em comportamento observável.
- Restrições de plataforma, versão do Kodi e dados existentes.
- Decisões anteriores registradas em ADRs, roadmap e constituição do projeto.

## Procedimento obrigatório

1. **Normalizar nome**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
2. **Buscar tv**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
3. **Comparar first_air_date**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
4. **Registrar tmdb_id**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.
5. **Não alterar identidade xtream**: produza uma decisão concreta, registre o arquivo/componente afetado e defina como verificar o resultado.

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

- [ ] Normalizar nome foi executado e possui evidência verificável.
- [ ] Buscar tv foi executado e possui evidência verificável.
- [ ] Comparar first_air_date foi executado e possui evidência verificável.
- [ ] Registrar tmdb_id foi executado e possui evidência verificável.
- [ ] Não alterar identidade xtream foi executado e possui evidência verificável.
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
