from tools import build_registry

def test_metrics():
    r=build_registry().execute('calculate-metrics',{'true_positive':8,'true_negative':7,'false_positive':2,'false_negative':3})
    assert r.ok and round(r.data['f1'],6)==round(2*(8/10)*(8/11)/((8/10)+(8/11)),6)

def test_compare():
    r=build_registry().execute('compare-runs',{'runs':[{'metrics':{'accuracy':.8}},{'metrics':{'accuracy':.9}}]})
    assert r.ok and abs(r.data['metrics']['accuracy']['mean']-.85)<1e-12

def test_summary():
    r=build_registry().execute('summarize-experiment',{'experiment_name':'x','runs':[{'metrics':{'loss':.4}},{'metrics':{'loss':.2}}]})
    assert r.ok and r.data['metric_summary']['loss']['min']==.2
