---
name: kodi-dialogs-progress
title: "Diálogos, Progresso e Experiência do Usuário"
description: "Usa diálogos de forma não invasiva, cancelável e consistente."
domain: "kodi"
triggers:
  - "DialogProgress"
  - "notificação Kodi"
  - "mensagem de erro"
  - "UX Kodi"
---

# Diálogos, Progresso e Experiência do Usuário

## Escolha do componente

- notification: confirmação breve e não crítica;
- ok: informação que exige leitura;
- yes/no: decisão real e reversível;
- select: escolha curta;
- progress: operação longa bloqueante;
- progress background: operação acompanhável sem bloquear tanto.

## Progresso

Atualize por lote e cheque cancelamento. Evite atualização por item em milhares de registros.

## Mensagens

Inclua ação possível:

- “Configure o provedor nas configurações.”
- “Não foi possível conectar. Verifique a rede e tente novamente.”
- “O cache local será mantido.”

Não exponha traceback, senha ou URL autenticada.

## Frequência

Não mostre notificação a cada navegação bem-sucedida. Use UI para estado relevante, não como log visual.

## Cancelamento

Cancelar deve interromper de forma segura, preservar dados anteriores e fechar progresso em `finally`.

## Internacionalização

Textos visíveis vêm de `strings.po`, inclusive erros e botões específicos.
