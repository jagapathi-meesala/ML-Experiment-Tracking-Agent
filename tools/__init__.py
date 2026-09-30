from .create_experiment import tool as create_experiment
from .log_run import tool as log_run
from .compare_runs import tool as compare_runs
from .calculate_metrics import tool as calculate_metrics
from .register_artifact import tool as register_artifact
from .summarize_experiment import tool as summarize_experiment

def build_registry():
    from adapters.registry import ToolRegistry
    r=ToolRegistry()
    for t in [create_experiment,log_run,compare_runs,calculate_metrics,register_artifact,summarize_experiment]: r.register(t)
    return r
