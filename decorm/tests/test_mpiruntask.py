import os

from decorm.tasks import Task
from decorm.serialization import serialize, deserialize
from decorm.mpiruntask import subprocess_mpirun_task_file, mpirun_task_file


def main_test_func(x, y=2):
    return x, y


def test_mpirun_task_file_serial():
    task_file = 'main_test_func.task'
    task = Task(main_test_func, 1)
    serialize(task, file=task_file)

    mpirun_task_file(task_file)
    result_file = task_file + '.result'
    assert os.path.exists(result_file)

    results = deserialize(file=result_file)
    assert results == [(1, 2)]

    if os.path.exists(task_file):
        os.remove(task_file)
    if os.path.exists(result_file):
        os.remove(result_file)


def test_subprocess_mpirun_task_file():
    task_file = 'main_test_func.task'
    task = Task(main_test_func, 1)
    serialize(task, file=task_file)

    subprocess_mpirun_task_file(task_file, np=2)
    result_file = task_file + '.result'
    assert os.path.exists(result_file)

    results = deserialize(file=result_file)
    assert results == [(1, 2), (1, 2)]

    if os.path.exists(task_file):
        os.remove(task_file)
    if os.path.exists(result_file):
        os.remove(result_file)
