import pytest

@pytest.fixture()
def some_data():
    x= 42
    assert x==32

def test_some_data(some_data):
    assert some_data == 2

@pytest.fixture()
def a_tuple():
    return (1,'foo',None,{'bar':23})


def test_a_tuple(a_tuple):
    assert a_tuple[3]['bar']==23

def test_tasks_just_a_few(tasks_just_a_few):
    assert tasks_just_a_few