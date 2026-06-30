# Dependency Graph

Version: 1.0.0
Status: Official Dependency Reference
Project: SAILE
Last Updated: 2026-06-30

## Purpose

This document defines allowed and forbidden dependency direction for SAILE.

## Canonical Graph

~~~mermaid
flowchart TD
    Presentation["Presentation Layer"]
    Runtime["SAILE Runtime"]
    Kernel["SAILE Kernel"]
    PluginManager["Plugin Manager"]
    CapabilityRegistry["Capability Registry"]
    Engines["Media Engines"]
    Plugins["Plugins"]
    APIs["Third-party APIs"]

    Presentation --> Runtime
    Runtime --> Kernel
    Kernel --> PluginManager
    PluginManager --> CapabilityRegistry
    CapabilityRegistry --> Engines
    Engines --> Kernel
    Kernel --> Plugins
    Plugins --> APIs
~~~

## Allowed Dependencies

| Component | May Depend On |
| --- | --- |
| Presentation Layer | Kernel-facing presentation contracts |
| SAILE Runtime | Kernel, lifecycle configuration, local bootstrap services |
| SAILE Kernel | Kernel contracts, registries, managers, Engine contracts, Plugin contracts |
| Media Engines | Domain Model, Kernel contracts, Capability contracts |
| Plugins | Plugin SDK, Capability contracts, permissioned Kernel services |
| Infrastructure | Contracts it implements, local platform APIs |
| Domain | Domain-local abstractions only |

## Forbidden Dependencies

- Presentation Layer to Plugin implementation.
- Presentation Layer to third-party API.
- Engine to Plugin implementation.
- Engine to provider implementation.
- Engine to direct HTTP, direct SQLite or direct filesystem persistence.
- Plugin to another Plugin.
- Plugin to Engine internals.
- Domain to Kodi, SQLite, HTTP, JSON, filesystem or Plugin implementation.
- Kernel to provider-specific business logic.
## SAILE-Specific Scope

- Defines top-level governance for the Engineering Framework.
- Must remain authoritative for all future implementation work.

## Required Section Completion

The following sections complete the mandatory SAILE Engineering Framework review surface for this artifact without changing any earlier record content.

## Responsibilities

This artifact owns its documented engineering record and must keep future implementation aligned with SAILE architecture.

## Dependencies

This artifact depends on the Master Specification, Engineering Constitution, Architecture, ADRs and relevant subject documents.

## Inputs

Accepted inputs are approved documents, reviewed decisions, measured evidence and explicit architecture constraints.

## Outputs

Expected outputs are reviewable guidance, decisions, risks, plans, checklists or status records usable before implementation.

## Architecture

This artifact participates in the canonical flow: Presentation Layer -> SAILE Runtime -> SAILE Kernel -> Plugin Manager -> Capability Registry -> Media Engines -> Plugins -> Third-party APIs.

## Business Rules

The Kernel coordinates; Engines own business rules; Plugins implement Capabilities; Engines consume Capabilities through the Kernel; Plugins never communicate directly.

## Extension Points

Extensions may add more specific records, checklists or diagrams when they do not contradict authoritative architecture.

## Failure Modes

Failure modes include stale records, undocumented assumptions, ambiguous ownership, architecture drift and implementation work beginning before readiness.

## Performance Notes

Performance guidance must preserve startup under 2 seconds, navigation under 100 milliseconds, Capability lookup under 5 milliseconds and predictable memory growth.

## Security Notes

Security guidance must preserve least privilege, local-only diagnostics, secret redaction, explicit Plugin permissions and no hidden network communication.

## Acceptance Criteria

This artifact is accepted when it is specific to SAILE, internally consistent, reviewable, versioned and compatible with Local-First Kernel-mediated execution.

