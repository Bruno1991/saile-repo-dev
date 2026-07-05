---
name: python-packaging-dependencies
title: "Dependências e Empacotamento Python"
description: "Controla bibliotecas, compatibilidade e tamanho do pacote Kodi."
domain: "python"
triggers:
  - "dependência Python"
  - "empacotar biblioteca"
  - "addon.xml requires"
  - "módulo externo"
---

# Dependências e Empacotamento Python

## Decisão de dependência

Antes de adicionar uma biblioteca, avalie:

- já existe na biblioteca padrão do Python embarcado?
- está disponível como módulo Kodi compatível?
- é pura Python ou possui extensão nativa?
- funciona em Android, Windows, Linux e arquiteturas distintas?
- tamanho e licença são aceitáveis?
- manutenção está ativa?

## Add-ons Kodi

Dependências oficiais devem ser declaradas em `addon.xml` quando apropriado. Não confiar em pacote instalado manualmente na máquina do desenvolvedor.

## Extensões nativas

São alto risco em add-ons multiplataforma. Exigem binários por plataforma/arquitetura e não devem ser introduzidas como se fossem biblioteca Python comum.

## Vendoring

Ao incorporar código de terceiros:

- preserve licença e avisos;
- fixe versão;
- documente origem;
- evite incluir testes/docs gigantes no ZIP;
- verifique conflitos de import.

## Reprodutibilidade

O build deve partir da fonte e gerar o mesmo layout. Não editar ZIP manualmente.

## Auditoria

Liste dependências diretas, motivo, licença, versão e risco de plataforma.
