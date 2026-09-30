from dataclasses import dataclass
from typing import Any
from core.agent_core import AgentCore

@dataclass
class PortableAdapter:
    """Framework-neutral adapter boundary. External frameworks can translate their request/response objects here."""
    core: AgentCore
    framework_name: str = "framework-neutral"
    def invoke(self, tool_name: str, inputs: dict[str, Any]) -> dict[str, Any]:
        result=self.core.execute(tool_name, inputs)
        return {"ok": result.ok, "data": result.data, "error": result.error, "framework": self.framework_name}

class OpenAIAdapter(PortableAdapter):
    def __init__(self, core): super().__init__(core, "openai-sdk")
class CrewAIAdapter(PortableAdapter):
    def __init__(self, core): super().__init__(core, "crewai")
class ClaudeCodeAdapter(PortableAdapter):
    def __init__(self, core): super().__init__(core, "claude-code")
class LyzrAdapter(PortableAdapter):
    def __init__(self, core): super().__init__(core, "lyzr")
