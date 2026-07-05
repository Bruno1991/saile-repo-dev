# Índice da Biblioteca de Skills

**Total: 57 skills.**

Cada skill está em `.agents/skills/<domínio>/<nome>/SKILL.md` e possui frontmatter com gatilhos de ativação.

## Core do agente (8)

- **Contrato Operacional do Agente** — `.agents/skills/core/agent-operating-contract/SKILL.md`  
  Define como o agente investiga, modifica, valida e relata mudanças de engenharia.
- **Definição de Pronto e Evidências** — `.agents/skills/core/definition-of-done/SKILL.md`  
  Padroniza critérios de conclusão e impede entregas incompletas.
- **Depuração por Causa Raiz** — `.agents/skills/core/root-cause-debugging/SKILL.md`  
  Orienta diagnóstico reproduzível sem aplicar correções aleatórias.
- **Disciplina de Documentação** — `.agents/skills/core/documentation-discipline/SKILL.md`  
  Mantém arquitetura, decisões e estado do projeto sincronizados com o código.
- **Gestão Segura de Mudanças** — `.agents/skills/core/safe-change-management/SKILL.md`  
  Controla impacto, compatibilidade, reversão e prevenção de regressões.
- **Higiene de Git e Segredos** — `.agents/skills/core/git-secret-hygiene/SKILL.md`  
  Protege tokens, credenciais, bancos locais e artefatos indevidos.
- **Leitura e Contexto do Repositório** — `.agents/skills/core/repository-context/SKILL.md`  
  Ensina o agente a compreender um projeto existente antes de editar.
- **Revisão de Código Orientada a Risco** — `.agents/skills/core/code-review/SKILL.md`  
  Fornece uma rotina de revisão para Python, SQLite e Kodi.

## Python (12)

- **Arquitetura Python Modular** — `.agents/skills/python/python-architecture/SKILL.md`  
  Define limites claros entre domínio, infraestrutura, persistência, providers e apresentação.
- **Clientes HTTP Robustos** — `.agents/skills/python/python-http-clients/SKILL.md`  
  Padroniza rede com timeout, codificação, retries limitados e validação de resposta.
- **Concorrência, Threads e Cancelamento** — `.agents/skills/python/python-concurrency-cancellation/SKILL.md`  
  Evita bloqueios, corridas e operações que ignoram cancelamento do usuário.
- **Configuração e Segredos** — `.agents/skills/python/python-configuration-secrets/SKILL.md`  
  Organiza settings, defaults, validação e proteção de credenciais.
- **Dependências e Empacotamento Python** — `.agents/skills/python/python-packaging-dependencies/SKILL.md`  
  Controla bibliotecas, compatibilidade e tamanho do pacote Kodi.
- **Desempenho e Memória em Dispositivos Limitados** — `.agents/skills/python/python-performance-memory/SKILL.md`  
  Orienta otimização para Android TV, Fire TV e hardware modesto.
- **Erros, Exceções e Logging** — `.agents/skills/python/python-errors-logging/SKILL.md`  
  Cria uma taxonomia de erros e logs úteis sem expor dados sensíveis.
- **Estilo, Tipagem e Contratos Python** — `.agents/skills/python/python-style-typing/SKILL.md`  
  Aplica legibilidade, tipos úteis e contratos explícitos sem burocracia excessiva.
- **Filesystem Multiplataforma** — `.agents/skills/python/python-cross-platform-filesystem/SKILL.md`  
  Garante paths seguros em Windows, Linux, Android e VFS do Kodi.
- **Refatoração Controlada** — `.agents/skills/python/python-refactoring/SKILL.md`  
  Melhora estrutura sem misturar mudança comportamental e reescrita ampla.
- **Segurança Aplicada a Python** — `.agents/skills/python/python-security/SKILL.md`  
  Previne injeção, SSRF, traversal, vazamento de segredos e execução insegura.
- **Testes Python para Código Integrado ao Kodi** — `.agents/skills/python/python-testing/SKILL.md`  
  Cria testes úteis isolando módulos Kodi e dependências externas.

## SQLite (10)

- **Conexões e Transações SQLite** — `.agents/skills/sqlite/sqlite-connections-transactions/SKILL.md`  
  Controla ciclo de vida, atomicidade, locks e fechamento de conexões.
- **FTS5 e JSON no SQLite** — `.agents/skills/sqlite/sqlite-fts-json/SKILL.md`  
  Usa recursos avançados somente com detecção e fallback.
- **Integração SQLite em Add-ons Kodi** — `.agents/skills/sqlite/sqlite-kodi-integration/SKILL.md`  
  Aplica SQLite de forma segura dentro do ciclo de vida e filesystem do Kodi.
- **Integridade, Backup e Recuperação** — `.agents/skills/sqlite/sqlite-integrity-backup-recovery/SKILL.md`  
  Protege dados locais e define resposta a corrupção ou falha de migração.
- **Migrações de Schema SQLite** — `.agents/skills/sqlite/sqlite-migrations/SKILL.md`  
  Evolui o banco sem perder dados nem depender de recriação silenciosa.
- **Modelagem de Schema SQLite** — `.agents/skills/sqlite/sqlite-schema-design/SKILL.md`  
  Cria esquemas pequenos, coerentes, versionáveis e adequados ao domínio local.
- **Padrões de Cache com SQLite** — `.agents/skills/sqlite/sqlite-cache-patterns/SKILL.md`  
  Implementa TTL, invalidação e identidade de cache sem mascarar erros.
- **SQL Parametrizado e Consultas Seguras** — `.agents/skills/sqlite/sqlite-parameterization/SKILL.md`  
  Impede injeção e erros de escaping em todas as consultas.
- **WAL e Concorrência SQLite** — `.agents/skills/sqlite/sqlite-wal-concurrency/SKILL.md`  
  Decide quando usar Write-Ahead Logging e como evitar problemas de arquivo.
- **Índices e Planos de Consulta** — `.agents/skills/sqlite/sqlite-indexes-query-plans/SKILL.md`  
  Otimiza com base em consultas reais e EXPLAIN QUERY PLAN.

## Kodi (21)

- **Arquitetura de Add-ons Kodi** — `.agents/skills/kodi/kodi-addon-architecture/SKILL.md`  
  Define uma arquitetura limpa para plugins de vídeo locais, modulares e multiplataforma.
- **Blueprint de Plugin de Vídeo** — `.agents/skills/kodi/kodi-video-addon-blueprint/SKILL.md`  
  Fornece um plano completo para construir plugin de vídeo desde zero.
- **Cache e Banco Local no Kodi** — `.agents/skills/kodi/kodi-cache-database/SKILL.md`  
  Combina SQLite, TTL e sincronização sem travar a interface.
- **Compatibilidade entre Dispositivos Kodi** — `.agents/skills/kodi/kodi-device-compatibility/SKILL.md`  
  Evita dependências e padrões que quebram em Android, Fire TV, Windows ou Linux.
- **Compatibilidade entre Versões do Kodi** — `.agents/skills/kodi/kodi-version-compatibility/SKILL.md`  
  Gerencia diferenças de API, settings e metadata entre versões.
- **Desempenho de UI e Navegação Kodi** — `.agents/skills/kodi/kodi-performance-ui/SKILL.md`  
  Mantém menus responsivos e reduz trabalho por tela.
- **Diretórios e Listagens Kodi** — `.agents/skills/kodi/kodi-directory-listings/SKILL.md`  
  Monta listagens corretas com addDirectoryItems, content type, ordenação e finalização.
- **Diálogos, Progresso e Experiência do Usuário** — `.agents/skills/kodi/kodi-dialogs-progress/SKILL.md`  
  Usa diálogos de forma não invasiva, cancelável e consistente.
- **Empacotamento e Repositório Kodi** — `.agents/skills/kodi/kodi-repository-packaging/SKILL.md`  
  Gera ZIPs, addons.xml, checksum e repositório de forma reproduzível e segura.
- **ListItem, Metadata e Arte** — `.agents/skills/kodi/kodi-listitem-metadata-art/SKILL.md`  
  Preenche itens com metadados e imagens compatíveis com skins e versões Kodi.
- **Logs e Depuração no Kodi** — `.agents/skills/kodi/kodi-debugging-logs/SKILL.md`  
  Cria diagnósticos úteis em dispositivos reais sem vazar dados.
- **Manifesto addon.xml** — `.agents/skills/kodi/kodi-addon-xml/SKILL.md`  
  Cria e valida o manifesto, dependências, extensões, metadados e assets.
- **Pesquisa na Wiki e API Oficial do Kodi** — `.agents/skills/kodi/kodi-wiki-research/SKILL.md`  
  Ensina o agente a verificar APIs e evitar exemplos obsoletos.
- **Playback e setResolvedUrl** — `.agents/skills/kodi/kodi-playback-resolution/SKILL.md`  
  Resolve streams corretamente, configura headers e trata falhas de reprodução.
- **Providers e Integrações de Rede** — `.agents/skills/kodi/kodi-providers-networking/SKILL.md`  
  Cria adapters de fontes externas sem acoplar API, UI e cache.
- **Roteamento de Plugins Kodi** — `.agents/skills/kodi/kodi-plugin-routing/SKILL.md`  
  Implementa parsing seguro de sys.argv, URLs plugin:// e dispatch explícito.
- **Segurança, Privacidade e Conformidade Kodi** — `.agents/skills/kodi/kodi-security-legal/SKILL.md`  
  Protege usuários e limita integrações a usos autorizados.
- **Serviços e Tarefas em Background** — `.agents/skills/kodi/kodi-service-addons/SKILL.md`  
  Implementa loops de serviço respeitando encerramento, energia e recursos.
- **Settings e Localização** — `.agents/skills/kodi/kodi-settings-localization/SKILL.md`  
  Cria configurações modernas, tipadas, localizadas e seguras.
- **Testes e Release Kodi** — `.agents/skills/kodi/kodi-testing-release/SKILL.md`  
  Define matriz de testes e gate de publicação.
- **xbmcvfs e special://** — `.agents/skills/kodi/kodi-xbmcvfs-special-paths/SKILL.md`  
  Manipula arquivos, diretórios e paths virtuais de maneira portátil.

## Workflows completos (6)

- **Workflow: Adicionar Funcionalidade com Segurança** — `.agents/skills/workflows/add-feature-safely/SKILL.md`  
  Adiciona recurso preservando arquitetura, dados e rotas existentes.
- **Workflow: Auditar Add-on Existente** — `.agents/skills/workflows/audit-existing-addon/SKILL.md`  
  Executa auditoria técnica completa antes de continuar desenvolvimento.
- **Workflow: Construir Plugin de Vídeo Kodi** — `.agents/skills/workflows/build-kodi-video-addon/SKILL.md`  
  Orquestra a construção completa de um plugin de vídeo desde requisitos até ZIP instalável.
- **Workflow: Corrigir Bug no Kodi** — `.agents/skills/workflows/fix-kodi-bug/SKILL.md`  
  Reproduz, localiza e corrige defeitos em roteamento, UI, banco, rede ou playback.
- **Workflow: Projetar Banco SQLite** — `.agents/skills/workflows/design-sqlite-database/SKILL.md`  
  Vai de requisitos e consultas a schema, migração, índices e testes.
- **Workflow: Publicar Repositório Kodi** — `.agents/skills/workflows/publish-kodi-repository/SKILL.md`  
  Empacota e publica add-ons por processo repetível, validado e seguro.

## Ordem recomendada por tarefa

### Novo add-on

1. Contrato Operacional do Agente.
2. Leitura e Contexto do Repositório.
3. Arquitetura de Add-ons Kodi.
4. Blueprint de Plugin de Vídeo.
5. Workflow: Construir Plugin de Vídeo Kodi.

### Alterar SQLite

1. Modelagem de Schema SQLite.
2. Conexões e Transações.
3. Migrações.
4. Índices e Planos.
5. Integração SQLite em Add-ons Kodi.

### Corrigir playback

1. Depuração por Causa Raiz.
2. Roteamento de Plugins Kodi.
3. Playback e setResolvedUrl.
4. Logs e Depuração no Kodi.
5. Workflow: Corrigir Bug no Kodi.

