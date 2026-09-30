from ._common import *
class CompareRuns(Tool):
    metadata=ToolMetadata("compare-runs","Compare two or more run metric dictionaries.",{"type":"object","required":["runs"],"properties":{"runs":{"type":"array"},"metric":{"type":"string"}}})
    def validate(self,p):
        runs=p.get("runs")
        if not isinstance(runs,list) or len(runs)<2: raise ToolValidationError("runs must contain at least two run objects")
        for r in runs:
            if not isinstance(r,dict) or not isinstance(r.get("metrics"),dict): raise ToolValidationError("each run must contain metrics")
    def execute(self,p):
        runs=p["runs"]; metric=p.get("metric")
        common=set.intersection(*(set(r["metrics"]) for r in runs))
        if metric:
            if metric not in common: raise ToolValidationError(f"metric is not common to all runs: {metric}")
            metrics=[metric]
        else: metrics=sorted(common)
        comparisons={m:{"values":[r["metrics"][m] for r in runs],"min":min(r["metrics"][m] for r in runs),"max":max(r["metrics"][m] for r in runs),"mean":sum(r["metrics"][m] for r in runs)/len(runs)} for m in metrics}
        return {"run_count":len(runs),"metrics":comparisons}
tool=CompareRuns()
