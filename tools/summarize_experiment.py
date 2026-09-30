from ._common import *
class SummarizeExperiment(Tool):
    metadata=ToolMetadata("summarize-experiment","Produce a deterministic summary from experiment runs.",{"type":"object","required":["experiment_name","runs"],"properties":{"experiment_name":{"type":"string"},"runs":{"type":"array"}}})
    def validate(self,p):
        required(p,"experiment_name"); runs=p.get("runs")
        if not isinstance(runs,list): raise ToolValidationError("runs must be a list")
    def execute(self,p):
        runs=p["runs"]; all_metrics={}
        for r in runs:
            if isinstance(r,dict) and isinstance(r.get("metrics"),dict):
                for k,v in r["metrics"].items():
                    if isinstance(v,(int,float)) and not isinstance(v,bool): all_metrics.setdefault(k,[]).append(v)
        aggregates={k:{"count":len(v),"min":min(v),"max":max(v),"mean":sum(v)/len(v)} for k,v in sorted(all_metrics.items()) if v}
        return {"experiment_name":p["experiment_name"],"run_count":len(runs),"metric_summary":aggregates}
tool=SummarizeExperiment()
