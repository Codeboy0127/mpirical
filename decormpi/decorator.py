import os

from decormpi.tasks import Task
from decormpi.serialization import serialize, deserialize
from decormpi.mpirun_task_file import subprocess_mpirun_task_file


class mpirun(object):
    """A decorator to execute functions in their own MPI environment"""

    def __init__(self, nprocs=1, timeout=20):
        """
        Run a function in an MPI environment

        Parameters
        ----------
        nprocs : int
            The number of processors to use in the mpirun call
        """
        self.nprocs = nprocs
        self.timeout = timeout

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            task = Task(func, *args, **kwargs)
            task_file = '{}.task'.format(func.__name__)
            serialize(task, file=task_file)

            subprocess_mpirun_task_file(task_file, nprocs=self.nprocs, timeout=self.timeout)

            result_file = '{}.result'.format(task_file)
            result = deserialize(file=result_file)

            os.remove(task_file)
            if os.path.exists(result_file):
                os.remove(result_file)

            return result
        return wrapped_func
