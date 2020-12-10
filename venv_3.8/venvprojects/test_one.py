from collections import namedtuple
Task=namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__=(None,None,None,None)


def test_asdict():
     t=Task('do something','okken',True,21)
     t_dict=t._asdict()
     ecpected={'summary':'do something',
               'owner':'okken',
               'done':True,
               'id':21}
     assert t_dict==ecpected


def test_passing():
    assert 1 in (1,2,3)
    assert "abc" not in 'hhhhh'
    assert 1>2