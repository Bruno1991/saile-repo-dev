# Backlog

Version: 1.0.0
Status: Official Backlog
Project: SAILE
Last Updated: 2026-06-30

## Critical

All initial critical items have been addressed.

## High

- Expand Engine-specific workflow state machines.
- Create contract examples for Playback, Search, Metadata, Artwork and Subtitle Capabilities.
- Define Plugin manifest validation rules before coding.
- Refine risk scoring and mitigation ownership.
- Prepare contribution and review checklists for first external contributors.

## Medium

- Add onboarding paths for human maintainers and AI agents.
- Add glossary cross-links to all major documents.
- Add release-readiness checklists.
- Add compatibility matrices for SDK, Kernel and Capability versions.
- Add benchmark scenario catalog.

## Low

- Improve diagrams after implementation package names are finalized.
- Add example ADRs for rejected alternatives.
- Add sample RFC walkthroughs.
- Add documentation style guide refinements.

## Future

- Prepare Plugin development starter guide after SDK contracts are accepted.
- Prepare release automation after the source tree exists.

## Completed

- Prepare initial Kodi Presentation Layer implementation plan (Phase 1 Skeleton).
- Review Capability contracts for ambiguity before SDK implementation begins.
- Define architecture validation checks that can detect forbidden dependencies.
- Review security and privacy documents for hidden network, telemetry or secret-handling gaps.
- Validate every document against Kernel-First, Local-First, Plugin-First, Capability-First and Domain-First principles.
- Review performance budgets against target Kodi devices.
- Prepare implementation epics after documentation completion.
## SAILE-Specific Scope

- Defines top-level governance for the Engineering Framework.
- Must remain authoritative for all future implementation work.

## Required Section Completion

The following sections complete the mandatory SAILE Engineering Framework review surface for this artifact without changing any earlier record content.

## Purpose

This artifact exists to support the SAILE Engineering Framework for BACKLOG while preserving Kernel-First and Local-First architecture.

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

