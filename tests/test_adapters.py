from adapters import OpenAIAdapter, CrewAIAdapter, ClaudeCodeAdapter, LyzrAdapter
from core.agent_core import AgentCore
from tools import build_registry

def test_adapters_share_core():
    core=AgentCore(build_registry())
    for cls,name in [(OpenAIAdapter,'openai-sdk'),(CrewAIAdapter,'crewai'),(ClaudeCodeAdapter,'claude-code'),(LyzrAdapter,'lyzr')]:
        r=cls(core).invoke('calculate-metrics',{'true_positive':1,'true_negative':1,'false_positive':0,'false_negative':0})
        assert r['ok'] and r['framework']==name
