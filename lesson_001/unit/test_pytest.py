import os,sys
sys.path.append(os.getcwd())
def inc(x):
    return x+1
def test_answer():
    assert inc(3)==5

