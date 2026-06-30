Read the complete `.agents` Engineering Framework.

Do not code yet.

Perform an Architecture Readiness Review for implementation.

Verify:

1. Is the Master Spec complete?
2. Is the Engineering Constitution complete?
3. Is ARCHITECTURE.md complete?
4. Is DOMAIN_MODEL.md complete?
5. Are KERNEL.md, PLUGIN_SDK.md and PROVIDER_SDK.md complete?
6. Are the required Skills, Templates, ADRs, Roadmap, Backlog and Project Status files present?
7. Are there contradictions between documents?
8. Are there missing decisions that would block implementation?
9. Is the architecture still 100% Local-First?
10. Is the Kernel in-process and not a server, daemon or external process?

If anything is missing, fix the engineering documentation first.

Only if the framework is implementation-ready, create a file:

.agents/IMPLEMENTATION_READINESS_REPORT.md

The report must say either:

READY_FOR_IMPLEMENTATION

or

NOT_READY_FOR_IMPLEMENTATION

Do not implement code in this step.