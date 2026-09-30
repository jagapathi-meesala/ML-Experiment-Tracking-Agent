# Agent Architecture
The core is implemented in Python without an LLM or agent-framework dependency. A dynamic registry discovers registered tool objects, while portable adapters translate the same core interface for OpenAI SDK, CrewAI, Claude Code, and Lyzr integration boundaries without claiming those frameworks were executed during local tests.
