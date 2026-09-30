from ._common import *
class LogRun(Tool):
    metadata=ToolMetadata("log-run","Record a model run with parameters and metrics.",{"type":"object","required":["experiment_id","run_name"],"properties":{"experiment_id":{"type":"string"},"run_name":{"type":"string"},"parameters":{"type":"object"},"metrics":{"type":"object"}}})
    def validate(self,p): required(p,"experiment_id"); required(p,"run_name");
    def execute(self,p):
        metrics=p.get("metrics",{}); params=p.get("parameters",{})
        if not isinstance(metrics,dict) or not isinstance(params,dict): raise ToolValidationError("parameters and metrics must be objects")
        for k,v in metrics.items():
            if not isinstance(k,str) or not isinstance(v,(int,float)) or isinstance(v,bool): raise ToolValidationError("metrics must map strings to numeric values")
        return {"run_id":new_id("run"),"experiment_id":p["experiment_id"],"run_name":p["run_name"],"parameters":params,"metrics":metrics,"logged_at":iso_now()}
tool=LogRun()
