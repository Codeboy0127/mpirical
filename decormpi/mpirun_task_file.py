import mpi4py

from os.path import realpath, dirname, join, exists
from sys import executable, argv
from subprocess import Popen
from decormpi.serialization import serialize, deserialize

THIS_SCRIPT = realpath(__file__)
MPIRUN = join(dirname(mpi4py.get_config()['mpicc']), 'mpirun')
if not exists(MPIRUN):
    raise RuntimeError('Cannot find mpirun')


def subprocess_mpirun_task_file(task_file, result_file=None, nprocs=1):
    if result_file is None:
        result_file = '{}.result'.format(task_file)
    p = Popen([MPIRUN, '-np', str(nprocs), executable, THIS_SCRIPT, task_file, result_file])
    p.wait()
    if p.returncode != 0:
        raise RuntimeError('Task failed to run')


def mpirun_task_file(task_file, result_file=None):
    if result_file is None:
        result_file = '{}.result'.format(task_file)
    from mpi4py import MPI
    task = deserialize(file=task_file)
    result = task.compute()
    results = MPI.COMM_WORLD.gather(result)
    if MPI.COMM_WORLD.Get_rank() == 0:
        serialize(results, file=result_file)


if __name__ == '__main__':
    t_file = argv[1]
    r_file = argv[2] if len(argv) > 2 else None
    mpirun_task_file(t_file, result_file=r_file)
