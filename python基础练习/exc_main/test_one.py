import pytest
from collections import namedtuple
Task=namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

def test_defaults():
    t1=Task()
    t2=Task(None,None,False,None)
    assert t1==t2
@pytest.mark.run_these_place
def test_member_success():
    t=Task('buy milk','brian')
    assert t.summary=='buy milk'
    assert t.owner=='brian'
    assert (t.done,t.id)==(False,None)

def test_assdict():
    t_task=Task('do something','okken',True,21)
    t_dict=t_task._asdict()
    expected={
        'summary':'do something',
        'owner':'okken',
        'done':True,
        'id':21
    }
    assert expected == t_dict

@pytest.mark.not_run_these_place
def test_replace():
    t_before=Task('do something','okken',True,22)
    t_replace=t_before._replace(summary='do something',owner='okken',done=False,id=22)
    t_expected=Task(summary='do something',owner='okken',done=False,id=11)
    assert t_replace==t_expected
