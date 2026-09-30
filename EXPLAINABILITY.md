# Explainability

## Inputs and Data Sources
Inputs are supplied directly by callers as structured objects containing experiment names, run metadata, parameters, metrics, confusion-matrix counts, or local artifact paths depending on the selected tool. Data sources are therefore the caller-provided experiment records and local filesystem metadata; the agent does not silently retrieve external experiment data.

### Input Requirements
Each tool validates required fields and expected types before processing. Numeric metrics must be numeric, identifiers must be non-empty, and artifact paths must be absolute and free of parent-directory traversal.

### Failure Handling
Invalid inputs produce structured validation errors instead of fabricated outputs. Missing local artifact files produce execution errors rather than a successful registration.

## Decision and Reasoning
The decision process is deterministic and rule-based: the registry selects a named tool, the tool validates its input schema, and then the tool applies its documented calculation or record-construction rules. Metric calculations use explicit formulas such as precision = TP/(TP+FP), recall = TP/(TP+FN), F1 = 2PR/(P+R), and accuracy = (TP+TN)/(TP+TN+FP+FN), with zero returned when a denominator is zero.

### Rules Applied
Run comparison uses only metrics shared by every supplied run unless a specific common metric is requested. Experiment summaries aggregate numeric values using count, minimum, maximum, and arithmetic mean, without selecting a model or declaring an unprovided business objective to be optimal.

### Expected Outputs
Successful execution returns structured data containing identifiers, metrics, aggregates, or artifact metadata. Failed execution returns a typed error object with a human-readable message and does not masquerade as success.

### Worked Example
For classification counts TP=8, TN=7, FP=2, and FN=3, the metric tool computes precision, recall, F1, and accuracy directly from those counts. For two runs sharing a metric, the comparison tool reports the supplied values and deterministic min, max, and mean aggregates.

## Limits and Constraints
The agent is limited to the information supplied to its tools and the local filesystem checks performed by artifact registration. It does not train models, execute artifacts, upload data to remote experiment trackers, or infer missing experimental facts.

### Constraints
Runtime configuration is obtained from environment variables rather than embedded production credentials or secret defaults. Framework adapters provide a stable translation interface, but framework-specific runtime compatibility is not claimed unless separately tested in that framework.

### Known Issues
The local test suite cannot prove compatibility with every external agent framework or a separately hosted experiment-tracking service. OpenGAP CLI availability is environment-dependent and must be reported as unverified when the executable is absent.

### Unsupported Behavior
Remote artifact uploads, model training, hyperparameter optimization, and external credential management are outside this implementation. The agent also does not execute arbitrary filesystem commands from tool inputs.
