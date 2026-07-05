# Traceability Matrix

| Requisito | Documento | Implementação esperada | Teste | Evidência |
|---|---|---|---|---|
| Execução local-first | Master Spec / ADR-0001 | bootstrap e storage local | smoke offline | pendente no repo real |
| UI sem rede direta | System Architecture | application/providers | dependency tests | pendente |
| SQLite versionado | Database/Migration | repositories/migrations | migration suite | pendente |
| Provider substituível | Provider Contract | registry/adapters | contract suite | pendente |
| Playback oficial Kodi | Playback Pipeline | kodi gateway | playback integration | pendente |
| Segredos fora do Git | Secrets Policy | config/redaction | secret scan | workflow incluído |
| Release reproduzível | Build and Release | build tool | artifact validation | workflow incluído |

A matriz deve ser expandida com IDs de requisitos e caminhos reais após o inventário.
