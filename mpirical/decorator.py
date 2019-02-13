from os import remove
from os.path import exists
from mpirical.tasks import Task
from mpirical.serialization import serialize, deserialize
from mpirical.mpiruntask import launch_mpirun_task_file
from mpirical.exceptions import ExceptionInfo


class mpirun(object):
    """A decorator to execute functions in their own MPI environment"""

    def __init__(self, return_rank='all', **kwargs):
        """
        Run a function in an MPI environment

        The ``mpirun`` decorator will run the function with the installed
        ``mpirun`` executable that is part of the MPI installation used by
        ``mpi4py``.

        Parameters
        ----------
        return_rank : ``int`` or ``[int]`` or ``'all'``
            Indicates the ranks from which the return values will be gathered
            across the MPI environment.  If ``'all'`` is specified, then all of
            the return values from all MPI ranks will be returned in a list.
            If a list of integers is given, then only those MPI ranks will
            return values (in the order specified).  If only 1 integer is
            given, then the return value from that rank will be returned (not
            in a list).
        kwargs : dict
            Dictionary that stores the arguments (without their initiall ``-``)
            to be given to the ``mpirun`` command.  Any value other than
            ``None`` will be converted to a string and passed as part of the
            ``mpirun`` argument.  For example, the keyword ``np`` with the
            value ``4`` (i.e., ``kwargs = {'np': 4}``) would result in
            ``mpirun`` being called with the arguments ``-np 4``.
        """
        self.return_rank = return_rank
        self.kwargs = kwargs

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            task_file = '{}.task'.format(func.__name__)
            result_file = '{}.result'.format(task_file)

            task = Task(func, *args, **kwargs)
            serialize(task, file=task_file)
            launch_mpirun_task_file(task_file, result_file, **self.kwargs)
            results = deserialize(file=result_file)

            self._remove_file(task_file)
            self._remove_file(result_file)

            exception = self._get_first_exception(results)
            if exception:
                exception.reraise()
            else:
                return self._collect_results(results)
        return wrapped_func

    @staticmethod
    def _remove_file(filename):
        if exists(filename):
            remove(filename)

    @staticmethod
    def _get_first_exception(results):
        exception = None
        for r in results:
            if isinstance(r, ExceptionInfo):
                exception = r
                break
        return exception

    def _collect_results(self, results):
        if self.return_rank == 'all':
            return results
        elif isinstance(self.return_rank, (tuple, list)):
            return [results[i] for i in self.return_rank]
        elif isinstance(self.return_rank, int):
            return results[self.return_rank]
