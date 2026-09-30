from ._common import *
class CreateExperiment(Tool):
    metadata=ToolMetadata("create-experiment","Create a validated experiment record.",{"type":"object","required":["name"],"properties":{"name":{"type":"string"},"description":{"type":"string"},"tags":{"type":"array"}}})
    def validate(self,p): safe_name(required(p,"name"));
    def execute(self,p): return {"experiment_id":new_id("exp"),"name":p["name"],"description":p.get("description",""),"tags":p.get("tags",[]),"created_at":iso_now()}
tool=CreateExperiment()
