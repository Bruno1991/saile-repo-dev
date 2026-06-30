# ADR-0001 SAILE Kernel Architecture

Version: 1.0.0
Status: Accepted
Project: SAILE
Date: 2026-06-30
Decision Owners: SAILE Architecture Board

## Purpose

This ADR records the foundational decision that SAILE is a Kernel-First, Local-First Media Runtime executed entirely inside the Kodi addon process.

## Context

SAILE must remain a long-lived open-source media platform rather than a tightly coupled Kodi addon. The project requires a stable architecture before production implementation begins.

## Decision

SAILE shall use the following architecture:

~~~text
Presentation Layer
-> SAILE Runtime
-> SAILE Kernel
-> Plugin Manager
-> Capability Registry
-> Media Engines
-> Plugins
-> Third-party APIs
~~~

The Kernel coordinates platform execution. Business rules belong to Media Engines and the Domain. Plugins implement Capabilities. Engines consume Capabilities through the Kernel. Plugins never communicate directly.

## Consequences

- Provider-specific code cannot leak into the Kernel.
- Engines remain independent from Plugin implementations.
- Plugins can be added or replaced without rewriting business workflows.
- Local-First privacy remains enforceable.
- AI and human contributors have a stable decision boundary.

## Alternatives Considered

Provider-centered architecture was rejected because Provider is only one Plugin specialization.

Direct Kodi-to-provider flow was rejected because it couples presentation to external services.

Backend-assisted architecture was rejected because SAILE has no server, cloud or daemon.

## Acceptance Criteria

This decision is implemented when every authoritative document uses Runtime, Kernel, Plugin Manager, Capability Registry, Media Engine, Plugin and Capability consistently and no direct Plugin-to-Plugin or Engine-to-Plugin implementation path exists.
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

