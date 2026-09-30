from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]
def test_manifest_static_constraints():
    d=yaml.safe_load((ROOT/'agent.yaml').read_text())
    assert d['spec_version']=='0.1.0'
    assert d['name']=='ml-experiment-tracking-agent'
    assert isinstance(d['tools'],list) and all(isinstance(x,str) for x in d['tools'])
    assert all((ROOT/'tools'/f'{x}.yaml').is_file() for x in d['tools'])
    assert all((ROOT/'skills'/x/'SKILL.md').is_file() for x in d['skills'])
    assert not any(k in d for k in ['display_name','entrypoint','portability'])
