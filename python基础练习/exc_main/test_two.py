import pytest
def test_passing():
    print('hello,i am test-passing')
    assert (1,2,3) == (1,2,3)

@pytest.mark.run_these_place
def test_failed():
    assert (1,2) ==(2,1)
def test_pass():
    assert (1,2,3) == (1,2,2)