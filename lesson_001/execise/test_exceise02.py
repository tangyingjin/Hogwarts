import pytest
# 只跑特定的case
def fun(a, b):
    return a / b

@pytest.mark.test
def test_case01():
    assert fun(10,2)==5
    assert fun('a','b')==None

@pytest.mark.test1
def test_case02():
    assert fun(10,3)==3.3333

def test_case03():
    assert fun(-9,1)==-9

