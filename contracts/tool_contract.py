from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable

class ToolValidationError(ValueError): pass
class ToolExecutionError(RuntimeError): pass

@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: dict[str, Any]

@dataclass
class ToolResult:
    ok: bool
    data: dict[str, Any] = field(default_factory=dict)
    error: dict[str, str] | None = None

class Tool:
    metadata: ToolMetadata
    validate: Callable[[dict[str, Any]], None]
    execute: Callable[[dict[str, Any]], dict[str, Any]]

    def __call__(self, payload: dict[str, Any]) -> ToolResult:
        if not isinstance(payload, dict):
            return ToolResult(False, error={"type":"validation_error","message":"Input must be an object"})
        try:
            self.validate(payload)
            return ToolResult(True, data=self.execute(payload))
        except ToolValidationError as exc:
            return ToolResult(False, error={"type":"validation_error","message":str(exc)})
        except Exception as exc:
            return ToolResult(False, error={"type":"execution_error","message":str(exc)})
