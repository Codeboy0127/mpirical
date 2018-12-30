import pytest

from mpipytest.tests.utils import mpi_bcast
from mpipytest.tasks import Task


def test_task_init():
    task = Task(mpi_bcast, 'x')
    assert isinstance(task, Task)


def test_task_func_not_callable_raises_exception():
    with pytest.raises(ValueError):
        Task(1, 'x')

