---
name: definition-of-done
title: "Definição de Pronto e Evidências"
description: "Padroniza critérios de conclusão e impede entregas incompletas."
domain: "core"
triggers:
  - "concluir tarefa"
  - "entrega"
  - "release"
  - "validação final"
---

# Definição de Pronto e Evidências

## Evidências mínimas

### Código

- sintaxe validada;
- imports resolvidos no ambiente suportado ou isolados por stubs;
- teste do caminho principal;
- teste de erro relevante;
- diff revisado.

### Banco

- schema criado em banco vazio;
- migração testada em versão anterior;
- rollback ou recuperação documentada;
- `PRAGMA integrity_check` quando aplicável;
- consultas críticas analisadas.

### Kodi

- ZIP com diretório raiz correto;
- `addon.xml` válido e versão coerente;
- abertura do menu principal;
- navegação de pasta;
- playback ou resolução simulada/real;
- settings acessíveis;
- log sem traceback inesperado.

### Documentação

- caminhos e comandos corretos;
- nenhuma referência a nome antigo;
- changelog objetivo;
- limitações declaradas.

## Resultado parcial

Quando algo não puder ser validado no ambiente atual, o agente deve declarar exatamente:

- o que foi validado;
- o que não foi;
- por que não foi;
- qual comando ou teste deve ser executado no dispositivo real.

Nunca substituir evidência por confiança.
