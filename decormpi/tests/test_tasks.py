import os
import pytest

from decormpi.tests.utils import mpi_bcast
from decormpi.serialization import serialize, deserialize
from decormpi.tasks import Task


def main_test_func(*args, **kwargs):
    return args, kwargs


def test_main_func_task():
    task = Task(main_test_func, 1, 'a', x='y')
    assert task.compute() == main_test_func(1, 'a', x='y')


def test_local_func_task():
    def local_test_func(x, y=3):
        return x, y
    task = Task(local_test_func, 4)
    assert task.compute() == local_test_func(4)


def test_mpi_bcast_task():
    task = Task(mpi_bcast, 'x')
    assert task.compute() == mpi_bcast('x')


def test_lambda_task():
    task = Task(lambda x: x, 1)
    assert task.compute() == 1


def test_task_func_not_callable_raises_exception():
    with pytest.raises(ValueError):
        Task(1, 'x')


def test_serialize_main_task():
    task = Task(main_test_func, 1, 'a', x='y')
    serialized_task = serialize(task)
    deserialized_task = deserialize(serialized_task)
    assert deserialized_task.compute() == task.compute()


def test_serialize_local_task():
    def local_test_func(x, y=3):
        return x, y
    task = Task(local_test_func, 4)
    serialized_task = serialize(task)
    deserialized_task = deserialize(serialized_task)
    assert deserialized_task.compute() == task.compute()


def test_serialize_mpi_bcast_task():
    task = Task(mpi_bcast, 'x')
    serialized_task = serialize(task)
    deserialized_task = deserialize(serialized_task)
    assert deserialized_task.compute() == task.compute()


def test_serialize_lambda_task():
    task = Task(lambda x: x, 1)
    serialized_task = serialize(task)
    deserialized_task = deserialize(serialized_task)
    assert deserialized_task.compute() == task.compute()


def test_serialize_mpi_bcast_task_to_from_file():
    task = Task(mpi_bcast, 'x')
    filename = 'mpi_bcast_task.out'
    serialize(task, file=filename)
    assert os.path.exists(filename)
    deserialized_task = deserialize(file=filename)
    assert deserialized_task.compute() == task.compute()
    os.remove(filename)
