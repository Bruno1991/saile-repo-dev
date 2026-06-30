# RFC Template

Version: 1.0.0
Status: Official Template
Project: SAILE
Classification: Authoritative
Last Updated: 2026-06-30

## Purpose

This template defines the required structure for a SAILE RFC artifact.

Every completed artifact created from this template must be specific to SAILE, compatible with Local-First execution and aligned with Kernel-First architecture.

## Required Header

~~~text
# <Artifact Title>

Version: <semantic version>
Status: Draft | Proposed | Accepted | Deprecated | Superseded
Project: SAILE
Owner: <person, role or working group>
Related Documents:
- .agents/SAILE_MASTER_SPEC.md
- .agents/ENGINEERING_CONSTITUTION.md
- .agents/docs/architecture/ARCHITECTURE.md
~~~

## Purpose

Explain why the artifact exists and what decision, design, workflow or review it governs.

## Responsibilities

List the responsibilities owned by the artifact and explicitly list responsibilities it does not own.

## Dependencies

List authoritative documents, contracts, Capabilities, Engines, Kernel services, Plugins, tools or policies that constrain the artifact.

## Inputs

List approved inputs. Reject undocumented assumptions, provider-specific shortcuts and implementation-first decisions.

## Outputs

List concrete outputs, such as contracts, diagrams, checklists, decisions, review evidence, risks or release artifacts.

## Architecture

Describe the artifact using the SAILE canonical model:

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

## Business Rules

Include the rules that future implementation must obey. At minimum:

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

## Extension Points

Describe how the artifact can evolve without breaking architecture.

## Failure Modes

Document expected failure scenarios, detection signals and recovery or escalation paths.

## Performance Notes

State performance budgets, measurement requirements and regression risks.

## Security Notes

State permission, resource, secret-handling, input-validation and privacy requirements.

## Acceptance Criteria

A completed artifact using this template is accepted only when it is specific, reviewable, versioned, internally consistent and does not require unstated assumptions.
## SAILE-Specific Scope

- Defines top-level governance for the Engineering Framework.
- Must remain authoritative for all future implementation work.

