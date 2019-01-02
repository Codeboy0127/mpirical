import os

from decorm.tasks import Task
from decorm.serialization import serialize, deserialize
from decorm.mpiruntask import subprocess_mpirun_task_file


class mpirun(object):
    """A decorator to execute functions in their own MPI environment"""

    def __init__(self, **kwargs):
        """
        Run a function in an MPI environment

        The ``mpirun`` decorator will run the function with the installed ``mpirun``
        executable that is part of the MPI installation used by ``mpi4py``.

        Parameters
        ----------
        kwargs : dict
            Dictionary that stores the arguments (without their initiall ``-``) to
            be given to the ``mpirun`` command.  Any value other than ``None`` will
            be converted to a string and passed as part of the ``mpirun`` argument.
            For example, the keyword ``np`` with the value ``4`` (i.e.,
            ``kwargs = {'np': 4}``) would result in ``mpirun`` being called with the
            arguments ``-np 4``.
        """
        self.kwargs = kwargs

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            task = Task(func, *args, **kwargs)
            task_file = '{}.task'.format(func.__name__)
            serialize(task, file=task_file)

            subprocess_mpirun_task_file(task_file, **self.kwargs)

            result_file = '{}.result'.format(task_file)
            results = deserialize(file=result_file)

            if os.path.exists(task_file):
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
