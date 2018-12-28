import subprocess
import os
import sys

from ._dill import write_test_dill


class mpitest(object):
    """Decorator to run a function in an MPI subprocess"""

    def __init__(self, nprocs: int = 1):
        self.nprocs = nprocs

    def __call__(self, test):
        def wrapped_test(*args, **kwargs):
            test_dill = write_test_dill(test, *args, **kwargs)

            mpi_cmds = ['mpirun',
                        '--tag-output',
                        '-np', str(self.nprocs),
                        sys.executable,
                        '-m', 'mpi_pytest._exec_dill',
                        test_dill]

            p = subprocess.Popen(mpi_cmds,
                                 env=os.environ,
                                 stderr=subprocess.PIPE)

            (stdout, stderr) = p.communicate()

            os.remove(test_dill)

            if p.returncode != 0:
                print(stderr.decode('utf-8'), file=sys.stderr)
                assert False

        return wrapped_test
