from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
required_files=['agent.yaml','SOUL.md','README.md','AGENTS.md','DUTIES.md','RULES.md','EXPLAINABILITY.md','.env.example','.gitignore','requirements.txt','pytest.ini']
required_dirs=['adapters','config','contracts','core','skills','tools','tests','verification']
errors=[]
def check(c,msg):
    if not c: errors.append(msg)
for f in required_files: check((ROOT/f).is_file(),f'missing file: {f}')
for d in required_dirs: check((ROOT/d).is_dir(),f'missing directory: {d}')
text=(ROOT/'EXPLAINABILITY.md').read_text()
heads=['## Inputs and Data Sources','## Decision and Reasoning','## Limits and Constraints']
for h in heads: check(text.count(h)==1,f'required heading missing/duplicated: {h}')
for bad in ['## Inputs','## Decision','## Limits']: check(bad not in text.split('## Inputs and Data Sources')[0],f'conflicting heading: {bad}')
for h in heads:
    start=text.index(h)+len(h); nxt=text.find('\n## ',start); section=text[start:] if nxt==-1 else text[start:nxt]
    sentences=re.findall(r'(?<=[.!?])\s+',section.strip())
    check(len(sentences)>=1,f'heading section too short: {h}')
agent=(ROOT/'agent.yaml').read_text()
check('spec_version: "0.1.0"' in agent,'spec_version 0.1.0 missing')
check('display_name:' not in agent and 'entrypoint:' not in agent and 'portability:' not in agent,'unsupported legacy property detected')
for name in ['experiment-lifecycle','run-comparison','metric-analysis','artifact-registration']:
    check((ROOT/'skills'/name/'SKILL.md').is_file(),f'missing skill: {name}')
for name in ['create_experiment.py','log_run.py','compare_runs.py','calculate_metrics.py','register_artifact.py','summarize_experiment.py']:
    check((ROOT/'tools'/name).is_file(),f'missing tool: {name}')
if errors:
    print('READINESS AUDIT: FAIL')
    print('\n'.join('- '+e for e in errors))
    sys.exit(1)
print('READINESS AUDIT: PASS')
print(f'Files checked: {len(required_files)}; directories checked: {len(required_dirs)}; tools: 6; skills: 4')
