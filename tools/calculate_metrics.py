from ._common import *
class CalculateMetrics(Tool):
    metadata=ToolMetadata("calculate-metrics","Calculate common classification metrics from counts.",{"type":"object","required":["true_positive","true_negative","false_positive","false_negative"],"properties":{}})
    def validate(self,p):
        for k in ("true_positive","true_negative","false_positive","false_negative"):
            v=p.get(k)
            if not isinstance(v,int) or isinstance(v,bool) or v<0: raise ToolValidationError(f"{k} must be a non-negative integer")
    def execute(self,p):
        tp,tn,fp,fn=[p[k] for k in ("true_positive","true_negative","false_positive","false_negative")]
        precision=tp/(tp+fp) if tp+fp else 0.0; recall=tp/(tp+fn) if tp+fn else 0.0
        f1=2*precision*recall/(precision+recall) if precision+recall else 0.0
        accuracy=(tp+tn)/(tp+tn+fp+fn) if tp+tn+fp+fn else 0.0
        return {"precision":precision,"recall":recall,"f1":f1,"accuracy":accuracy}
tool=CalculateMetrics()
