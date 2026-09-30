from datetime import datetime, timezone
from pathlib import Path
import re, uuid
from contracts.tool_contract import Tool, ToolMetadata, ToolValidationError

def required(payload,key,typ=str):
    if key not in payload or not isinstance(payload[key],typ) or (isinstance(payload[key],str) and not payload[key].strip()):
        raise ToolValidationError(f"{key} is required and must be a non-empty {typ.__name__}")
    return payload[key]
def iso_now(): return datetime.now(timezone.utc).isoformat()
def new_id(prefix): return f"{prefix}-{uuid.uuid4().hex[:12]}"
def safe_name(v):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}",v): raise ToolValidationError("identifier contains unsupported characters")
    return v
