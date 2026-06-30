# Implementation Epics

This document translates the verified architecture and requirements into actionable coding epics for the Addon Implementation Phase.

## Epic 1: Kernel & Dependency Injection
**Goal:** Implement the foundational Kernel container and Service Registry.
- Implement `lib.kernel.service_registry.ServiceRegistry` with singleton and transient lifecycle management.
- Implement core services: Logging, Configuration.
- Establish `lib.bootstrap` to initialize the container before any Kodi UI logic runs.

## Epic 2: Capability & Engine Registries
**Goal:** Implement the execution boundaries.
- Implement `lib.kernel.capability_registry.CapabilityRegistry` with deterministic selection.
- Implement `lib.kernel.engine_registry.EngineRegistry` to coordinate Engine states.
- Ensure the Architecture Validation Script runs successfully on CI.

## Epic 3: Plugin Manager
**Goal:** Safely discover, validate, and load Plugins.
- Implement Plugin discovery in `lib.plugins`.
- Implement manifest validation against `PLUGIN_SDK.md` rules.
- Enforce `network.*` permission constraints during load time.

## Epic 4: Base Capabilities
**Goal:** Implement the first concrete capabilities.
- Implement `SearchCapability` contracts.
- Implement `MetadataCapability` contracts.
- Create dummy Plugins to test contract compliance.

## Epic 5: Presentation Layer (Kodi UI)
**Goal:** Connect the Kernel to the Kodi UI.
- Implement `default.py` routing using `xbmcplugin`.
- Connect Kodi directory building to `Engine` workflows.
- Ensure 50ms menu navigation budget is met.
