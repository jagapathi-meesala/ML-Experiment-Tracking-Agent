# ML Experiment Tracking Agent

A framework-independent OpenGAP 0.1.0 agent for creating experiment records, logging runs, comparing metrics, calculating classification metrics, registering local artifact metadata, and summarizing experiment runs.

## Architecture
`AgentCore` depends on a dynamic `ToolRegistry`; tools implement a framework-neutral contract; portable adapters expose the same interface to OpenAI SDK, CrewAI, Claude Code, and Lyzr boundaries.

## Installation
Create a virtual environment, install `requirements.txt`, and run `pytest -q` from the repository root.

## Configuration
Runtime configuration is read from `ML_EXPERIMENT_STORAGE_DIR`, `ML_EXPERIMENT_MAX_ARTIFACT_BYTES`, and `ML_EXPERIMENT_ALLOW_EXTERNAL_PATHS`. No production secrets are stored in the repository.

## Tools
- create-experiment
- log-run
- compare-runs
- calculate-metrics
- register-artifact
- summarize-experiment

## Skills
- experiment-lifecycle
- run-comparison
- metric-analysis
- artifact-registration

## Usage
```python
from adapters.registry import ToolRegistry
from core.agent_core import AgentCore
from tools import build_registry
agent = AgentCore(build_registry())
result = agent.execute("calculate-metrics", {"true_positive": 8, "true_negative": 7, "false_positive": 2, "false_negative": 3})
```

## Testing
Run `pytest -q` and `python verification/readiness_audit.py`.

## Portability
The core has no dependency on an agent framework. Adapter classes provide a stable translation boundary; this repository does not claim external framework execution was tested locally.

## Limitations
No remote tracking backend, model training, artifact upload, or arbitrary artifact execution is implemented.
