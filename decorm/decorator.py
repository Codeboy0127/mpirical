import os

from decorm.tasks import Task
from decorm.serialization import serialize, deserialize
from decorm.mpiruntask import subprocess_mpirun_task_file


class mpirun(object):
    """A decorator to execute functions in their own MPI environment"""

    def __init__(self, nprocs=1):
        """
        Run a function in an MPI environment

        The `mpirun` decorator will run the function with the installed `mpirun`
        executable that is part of the MPI installation used by `mpi4py`.

        Parameters
        ----------
        nprocs : int
            The number of processors to use in the mpirun call
        """
        self.nprocs = nprocs

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            task = Task(func, *args, **kwargs)
            task_file = '{}.task'.format(func.__name__)
            serialize(task, file=task_file)

            subprocess_mpirun_task_file(task_file, nprocs=self.nprocs)

            result_file = '{}.result'.format(task_file)
            results = deserialize(file=result_file)

            os.remove(task_file)
            if os.path.exists(result_file):
                os.remove(result_file)

            if any(isinstance(r, Exception) for r in results):
                exception = None
                for r in results:
                    if isinstance(r, Exception):
                        exception = r
                        break
                raise exception
            else:
                return results
        return wrapped_func
