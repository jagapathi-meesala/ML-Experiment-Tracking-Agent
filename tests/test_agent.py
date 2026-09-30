from core.agent_core import AgentCore
from tools import build_registry

def test_agent_discovers_tools():
    assert AgentCore(build_registry()).discover_tools()==['calculate-metrics','compare-runs','create-experiment','log-run','register-artifact','summarize-experiment']

def test_agent_executes_tool():
    r=AgentCore(build_registry()).execute('create-experiment',{'name':'baseline'})
    assert r.ok and r.data['name']=='baseline'
