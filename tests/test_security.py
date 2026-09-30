from tools import build_registry

def test_invalid_metric_types_rejected():
    r=build_registry().execute('calculate-metrics',{'true_positive':'1','true_negative':1,'false_positive':0,'false_negative':0})
    assert not r.ok and r.error['type']=='validation_error'

def test_artifact_traversal_rejected():
    r=build_registry().execute('register-artifact',{'path':'/tmp/../secret','artifact_type':'model'})
    assert not r.ok
