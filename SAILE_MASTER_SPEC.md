# SAILE Master Specification

**Status:** baseline normativa inicial  
**Projeto:** SAILE  
**Add-on principal:** `plugin.video.saile.mc`  
**Repositório Kodi:** `repository.saile`

## 1. Visão

SAILE é uma plataforma de mídia **local-first** cuja camada de apresentação atual é o Kodi. Kodi não é o domínio do produto; é o frontend responsável por navegação, apresentação, settings e acionamento do player.

O sistema deve executar no dispositivo do usuário. Serviços externos limitam-se a APIs e fontes de terceiros expressamente configuradas. O projeto não depende de servidor central próprio para autenticação, catálogo, telemetria ou reprodução.

## 2. Objetivos

- oferecer uma arquitetura de providers substituíveis;
- suportar IPTV por interfaces compatíveis com Xtream;
- suportar música por APIs autorizadas do YouTube ou providers aprovados;
- suportar fontes de vídeo autorizadas, inclusive metadados torrent quando legalmente permitido;
- manter estado, cache, favoritos, histórico e preferências localmente;
- funcionar em dispositivos Kodi com recursos limitados;
- publicar atualizações por repositório Kodi hospedado estaticamente;
- preservar segurança, privacidade, desempenho e rastreabilidade.

## 3. Não objetivos

- operar um backend central do SAILE;
- hospedar, retransmitir ou redistribuir conteúdo de terceiros;
- contornar DRM, autenticação, bloqueios ou termos de serviço;
- embutir listas, credenciais, tokens ou chaves privadas;
- acessar diretamente bancos internos do Kodi;
- prometer suporte universal sem matriz de testes.

## 4. Princípios arquiteturais

1. **Kodi como apresentação:** UI, navegação e player.
2. **Domínio independente:** modelos e casos de uso não importam APIs Kodi.
3. **Providers isolados:** rede, autenticação e transformação ficam em adapters.
4. **Persistência local:** SQLite gerenciado por camada própria.
5. **UI não bloqueante:** operações longas exibem progresso e aceitam cancelamento.
6. **Falha previsível:** erro remoto não destrói cache válido nem banco.
7. **Contratos explícitos:** rotas, settings, schema e provider APIs são versionados.
8. **Build reproduzível:** artefatos são gerados, não editados manualmente.
9. **Compatibilidade comprovada:** suporte é baseado em evidência.
10. **Conteúdo autorizado:** o sistema é neutro quanto à fonte, mas não facilita uso ilícito.

## 5. Camadas obrigatórias

```text
Kodi Presentation
    ↓
Application / Use Cases
    ↓
Domain Models and Contracts
    ↓
Provider Adapters | SQLite Repositories | Kodi Gateways
    ↓
Third-party APIs | Local Files | Kodi Runtime
```

Dependências apontam para dentro. Domínio não importa `xbmc`, `xbmcgui`, `xbmcplugin`, `xbmcvfs` nem clientes HTTP concretos.

## 6. Domínios

- catálogo e categorias;
- busca;
- detalhes de mídia;
- resolução de playback;
- perfis locais;
- favoritos e progresso;
- settings e credenciais locais;
- cache e sincronização manual;
- diagnóstico e atualização.

## 7. Contratos públicos protegidos

- ID do add-on e do repositório;
- nomes de settings persistidos;
- parâmetros de rotas já publicados;
- schema e migrações do banco;
- formato do repositório Kodi;
- diretórios especiais usados pelo runtime;
- interfaces de providers;
- comportamento do fluxo de playback.

Quebra exige ADR, plano de migração e versão compatível com o impacto.

## 8. Persistência

SQLite é o armazenamento padrão para estado estruturado, cache indexado e progresso. Cada conexão deve declarar pragmas suportados, usar transações explícitas e consultas parametrizadas. Mudanças de schema são monotônicas, versionadas e testadas contra cópia de banco anterior.

## 9. Rede

- timeouts obrigatórios;
- retries limitados apenas para operações idempotentes;
- cancelamento quando aplicável;
- user-agent identificável sem dados pessoais;
- redaction de credenciais e query strings sensíveis;
- cache condicionado à validade e às regras do provider;
- TLS validado por padrão.

## 10. Playback

A UI solicita reprodução por identificador de domínio. O provider resolve uma `PlaybackSource`. A camada Kodi converte a fonte em `ListItem` e conclui com a API apropriada. Erros são apresentados ao usuário e registrados sem segredos.

## 11. Compatibilidade

A versão-alvo do Kodi e de `xbmc.python` deve estar declarada no release. Recursos opcionais dependem de capability detection. Teste mínimo: uma plataforma desktop e pelo menos um dispositivo de sala quando a funcionalidade afetar playback ou performance.

## 12. Segurança e privacidade

- nenhum segredo no Git;
- nenhum log de senha, token ou URL autenticada;
- arquivos locais com menor exposição permitida pelo ambiente;
- sem telemetria remota por padrão;
- validação de entrada, caminhos e payloads;
- dependências mínimas e auditáveis;
- artefatos com hash e procedência documentada.

## 13. Qualidade

Código novo deve ter validação sintática, testes proporcionais ao risco, tratamento de erro, documentação e evidência. Mudança de bug deve incluir regressão; mudança de banco deve incluir migração; mudança de release deve incluir inspeção do pacote.

## 14. Governança documental

`PROJECT_STATUS.md` representa o estado operacional. ADRs representam decisões. Os documentos em `docs/` representam contratos. Em divergência, a mudança deve atualizar todos os artefatos relacionados de acordo com `DOCUMENT_UPDATE_MATRIX.md`.

## 15. Critérios de aceitação globais

- instalação e inicialização sem exceção não tratada;
- navegação encerra diretórios corretamente;
- playback válido é resolvido pelo fluxo oficial;
- cancelamento não corrompe estado;
- cache e banco sobrevivem a reinicialização;
- credenciais não aparecem em logs ou artefatos;
- pacote contém apenas arquivos necessários;
- versão e repositório permanecem consistentes;
- documentação e status refletem o comportamento entregue.
