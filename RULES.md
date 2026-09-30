# Rules
- Never fabricate metrics, run results, or artifact metadata.
- Reject malformed input instead of coercing unsafe values.
- Do not execute registered artifacts.
- Do not expose environment secrets in outputs.
- Keep core behavior independent from OpenAI, CrewAI, Claude Code, and Lyzr.
- Treat external framework adapters as translation boundaries, not dependencies of core logic.
