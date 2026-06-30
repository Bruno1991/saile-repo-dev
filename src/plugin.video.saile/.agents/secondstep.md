Read `.agents/AGENTS.md` and `.agents/IMPLEMENTATION_READINESS_REPORT.md`.

If the project is marked READY_FOR_IMPLEMENTATION, begin Phase 1 implementation.

Do not implement features yet.

Create only the production source structure and minimal runnable skeleton for the Kodi addon.

Implement:

1. addon root structure
2. addon.xml
3. default.py entrypoint
4. bootstrap
5. in-process Runtime skeleton
6. Kernel skeleton
7. Plugin Manager skeleton
8. Capability Registry skeleton
9. Service Registry skeleton
10. basic Logging service
11. basic Configuration service
12. empty Engine Registry
13. empty Plugin directory
14. architecture validation notes

Rules:

- No Xtream implementation yet.
- No YouTube implementation yet.
- No torrent implementation yet.
- No external API calls yet.
- No database schema yet unless required for boot.
- No business features yet.
- Must run inside Kodi.
- Must remain 100% local.
- Must follow `.agents` documentation.
- Update `.agents/PROJECT_STATUS.md`.
- Update `.agents/BACKLOG.md`.
- Create `.agents/IMPLEMENTATION_LOG.md`.

Stop after the skeleton is created.