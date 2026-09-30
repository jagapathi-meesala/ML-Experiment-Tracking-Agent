import os
from dataclasses import dataclass

class ConfigurationError(ValueError):
    pass

def _required(name: str) -> str:
    value=os.getenv(name)
    if value is None or not value.strip():
        raise ConfigurationError(f"Required environment variable {name} is not set")
    return value.strip()

@dataclass(frozen=True)
class Settings:
    storage_dir: str
    max_artifact_bytes: int
    allow_external_paths: bool

    @classmethod
    def from_env(cls):
        storage=_required("ML_EXPERIMENT_STORAGE_DIR")
        raw_max=_required("ML_EXPERIMENT_MAX_ARTIFACT_BYTES")
        raw_paths=_required("ML_EXPERIMENT_ALLOW_EXTERNAL_PATHS").lower()
        try: max_bytes=int(raw_max)
        except ValueError as e: raise ConfigurationError("ML_EXPERIMENT_MAX_ARTIFACT_BYTES must be an integer") from e
        if max_bytes <= 0: raise ConfigurationError("ML_EXPERIMENT_MAX_ARTIFACT_BYTES must be positive")
        if raw_paths not in {"true","false"}: raise ConfigurationError("ML_EXPERIMENT_ALLOW_EXTERNAL_PATHS must be true or false")
        return cls(storage, max_bytes, raw_paths=="true")
