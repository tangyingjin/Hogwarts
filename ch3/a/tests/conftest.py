import pytest
import tasks
from tasks import Task

@pytest.fixture()
def tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir),'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_just_a_few():
    return (
        Task('write some code','brian',True),
        Task("code review brian's code",'katie',False),
        Task('Fix what Brian did','Michlle',False)
    )