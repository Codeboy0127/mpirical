import os

import pytest

from mpirical.mpiruntask import launch_mpirun_task_file, mpirun_task_file
from mpirical.serialization import deserialize, serialize
from mpirical.tasks import Task


def main_test_func(x, y=2):
    return x, y


def test_mpirun_task_file_serial():
    task_file = 'serial_main_test_func.task'
    result_file = 'serial_main_test_func.result'

    task = Task(main_test_func, 1)
    serialize(task, file=task_file)
    assert os.path.exists(task_file)

    mpirun_task_file(task_file, result_file)
    assert os.path.exists(result_file)

    results = deserialize(file=result_file)
    assert results == [(1, 2)]

    if os.path.exists(task_file):
        os.remove(task_file)
    if os.path.exists(result_file):
        os.remove(result_file)


@pytest.mark.mpiunstable
def test_mpirun_task_file_parallel():
    task_file = 'parallel_main_test_func.task'
    result_file = 'parallel_main_test_func.result'

    task = Task(main_test_func, 1)
    serialize(task, file=task_file)
    assert os.path.exists(task_file)

    launch_mpirun_task_file(task_file, result_file, np=2)
    assert os.path.exists(result_file)

    results = deserialize(file=result_file)
    assert results == [(1, 2), (1, 2)]

    if os.path.exists(task_file):
        os.remove(task_file)
    if os.path.exists(result_file):
        os.remove(result_file)
