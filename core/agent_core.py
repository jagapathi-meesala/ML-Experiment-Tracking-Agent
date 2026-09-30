from contracts.tool_contract import ToolResult
from adapters.registry import ToolRegistry

class AgentCore:
    def __init__(self, registry: ToolRegistry): self.registry=registry
    def discover_tools(self): return self.registry.names()
    def execute(self, tool_name: str, payload: dict) -> ToolResult:
        return self.registry.execute(tool_name, payload)
