from adapters.registry import ToolRegistry
from tools.create_experiment import tool

def test_register_and_duplicate():
    r=ToolRegistry(); r.register(tool)
    assert r.get('create-experiment') is tool
    try: r.register(tool); assert False
    except ValueError: pass

def test_unknown_tool():
    r=ToolRegistry(); result=r.execute('missing',{})
    assert not result.ok and result.error['type']=='not_found'
