from ._common import *
class RegisterArtifact(Tool):
    metadata=ToolMetadata("register-artifact","Register metadata for a local experiment artifact without copying or executing it.",{"type":"object","required":["path","artifact_type"],"properties":{"path":{"type":"string"},"artifact_type":{"type":"string"}}})
    def validate(self,p):
        path=required(p,"path"); required(p,"artifact_type")
        if ".." in Path(path).parts: raise ToolValidationError("parent traversal is not allowed")
        if not Path(path).is_absolute(): raise ToolValidationError("artifact path must be absolute")
    def execute(self,p):
        path=Path(p["path"])
        if not path.exists() or not path.is_file(): raise FileNotFoundError("artifact file does not exist")
        return {"artifact_id":new_id("artifact"),"path":str(path),"artifact_type":p["artifact_type"],"size_bytes":path.stat().st_size}
tool=RegisterArtifact()
