from __future__ import annotations
from contracts.tool_contract import Tool, ToolResult

class ToolRegistry:
    def __init__(self): self._tools: dict[str,Tool]={}
    def register(self, tool: Tool):
        name=tool.metadata.name
        if not name: raise ValueError("Tool name cannot be empty")
        if name in self._tools: raise ValueError(f"Tool already registered: {name}")
        self._tools[name]=tool
    def names(self): return sorted(self._tools)
    def get(self, name): return self._tools.get(name)
    def execute(self, name, payload):
        tool=self.get(name)
        if tool is None: return ToolResult(False,error={"type":"not_found","message":f"Unknown tool: {name}"})
        return tool(payload)
