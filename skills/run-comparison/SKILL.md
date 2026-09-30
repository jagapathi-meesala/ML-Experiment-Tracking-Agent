---
name: run-comparison
description: Compare multiple completed runs over common numeric metrics and expose deterministic aggregates.
---

# Run Comparison

## Purpose
Compare multiple completed runs over common numeric metrics and expose deterministic aggregates.

## Inputs
Structured JSON-like objects containing the fields required by the associated tools. Inputs must be explicit; missing values are not inferred.

## Processing
Validate types and required fields first, then perform deterministic calculations or record construction. Errors are returned as structured failures rather than being hidden.

## Outputs
Return structured identifiers, metrics, aggregates, or artifact metadata suitable for downstream processing.

## Limitations
This skill does not train models, upload artifacts to third-party services, or infer experiment provenance that was not supplied. External framework behavior is outside this skill.

## Expected Behavior
The skill must reject malformed inputs and preserve the supplied experiment facts. It must never fabricate successful results merely to satisfy a caller.
