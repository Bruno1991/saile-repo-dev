# Plugin DomAIn

Version: 1.0.0
Status: Official Engineering Framework Document
Project: SAILE
Classification: Authoritative
Last Updated: 2026-06-30

Related Documents:
- .agents/SAILE_MASTER_SPEC.md
- .agents/ENGINEERING_CONSTITUTION.md
- .agents/docs/architecture/ARCHITECTURE.md

## Purpose

Plugin DomAIn defines domain vocabulary, invariants and business ownership for SAILE.

This document exists before production implementation so every future contributor can work from a shared architecture, vocabulary and quality bar.

## Responsibilities

This document is responsible for:

- Preserving Kernel-First, Local-First, Plugin-First, Capability-First and Domain-First design.
- Defining the responsibilities owned by this subject area.
- Preventing Kodi, storage, HTTP, Plugin and business concerns from crossing architectural boundaries.
- Giving human engineers and autonomous AI agents reviewable instructions before implementation begins.
- Defining acceptance criteria that can be used during planning, review and validation.

This document is not responsible for implementing addon behavior, Python modules, Kodi screens, database code or third-party integrations.

## Dependencies

This subject depends on:

- SAILE Master Specification for product intent and non-goals.
- Engineering Constitution for immutable engineering laws.
- Architecture reference for dependency direction and runtime ownership.
- Domain Model for business vocabulary.
- Kernel specifications for orchestration boundaries.
- SDK specifications when external contributors or Plugins are affected.

It must not depend on provider-specific implementation details, remote SAILE services, hidden background workers or undocumented conventions.

## Inputs

Accepted inputs are:

- Approved architectural documents.
- Approved ADRs and RFCs.
- Versioned Capability, Engine, Plugin and Kernel contracts.
- Local runtime constraints from Kodi addon execution.
- Measured performance, diagnostics and security evidence.

Unaccepted inputs are undocumented assumptions, direct provider behavior, convenience-driven coupling and implementation-first decisions.

## Outputs

Expected outputs are:

- Clear ownership rules.
- Stable vocabulary.
- Reviewable contracts.
- Checklists for contributors.
- Failure handling expectations.
- Security, privacy and performance constraints.
- Acceptance criteria for future implementation work.

## Architecture

SAILE uses this canonical execution model:

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

For this document, $Title must be interpreted through that model. Work begins at documentation, flows through Kernel-mediated contracts, and only then becomes implementation-ready.

## Business Rules

- SAILE is a Local-First Media Runtime.
- Kodi is the current Presentation Layer, not the platform.
- Everything executes inside the Kodi addon process.
- There is no SAILE backend, cloud, daemon, background service or server.
- The Kernel coordinates lifecycle, registries, permissions, resources and orchestration.
- The Kernel never contains business rules.
- Business rules belong to Media Engines and the Domain.
- Plugins implement Capabilities.
- Engines consume Capabilities through the Kernel.
- Plugins never communicate directly with other Plugins.
- Provider is only a Plugin specialization.

Additional rules for this subject:

- Every responsibility must have exactly one owning architectural component.
- Any cross-boundary communication must use a documented contract.
- Any business policy must belong to a Media Engine or the Domain, never to the Kernel or Presentation Layer.
- Any external communication must be performed by a permissioned Plugin.
- Any deviation requires an ADR before implementation.

## Extension Points

Allowed extension points include:

- New documents that refine this subject without contradicting higher-level specifications.
- New templates or checklists that make review easier.
- New Capability contracts when existing contracts cannot represent a required behavior.
- New Plugins that implement existing contracts.
- New Engines only when a distinct business workflow exists.

Extensions must preserve deterministic execution, local operation and Kernel mediation.

## Failure Modes

Failures this document must help prevent:

- Implementation begins before documentation is complete.
- A subsystem bypasses the Kernel.
- Provider-specific behavior leaks into the Kernel, Presentation Layer or Domain.
- Plugins communicate directly.
- Capability contracts become ambiguous or unversioned.
- Local user data leaves the device without explicit user action.
- Performance budgets are ignored until late implementation.
- Security and privacy controls are treated as optional.

## Performance Notes

The architecture targets:

- Addon startup under 2 seconds in normal local conditions.
- Menu navigation under 100 milliseconds.
- Capability lookup under 5 milliseconds.
- Common SQLite lookup under 20 milliseconds once implementation exists.
- Predictable memory growth on low-power devices.

Any future implementation derived from this document must include measurement points and regression checks.

## Security Notes

Security is enforced through the Kernel, Permission Manager, Resource Manager, Capability Registry and Plugin Manager.

This subject must preserve:

- Least privilege for Plugins.
- Explicit permission declarations.
- No hidden network communication.
- No arbitrary downloaded code execution.
- Secret redaction in logs and diagnostics.
- Local-only diagnostics unless the user explicitly exports data.

## Acceptance Criteria

This document is acceptable when:

- It is specific to SAILE and does not describe a generic media addon.
- It preserves Kernel-First, Local-First, Plugin-First, Capability-First and Domain-First architecture.
- It contains enough detail to guide future implementation without inventing missing rules.
- It names dependencies, outputs, failure modes, performance constraints and security constraints.
- It can be used by a human engineer or AI contributor during review.
- It introduces no production addon code.
## SAILE-Specific Scope

- Defines technology-independent business language used by Engines, Capabilities and Plugins.
- Must remain free of Kodi, SQLite, HTTP, JSON, filesystem and Plugin implementation details.

