from whichcraft import which
from os import environ
from os.path import exists, realpath
from sys import executable, argv
from subprocess import Popen
from mpirical.serialization import serialize, deserialize
from mpirical.exceptions import ExceptionInfo
from tblib import pickling_support
pickling_support.install()

THIS_SCRIPT = realpath(__file__)
MPIRUN = environ['MPIRICAL_MPIRUN'].split() if 'MPIRICAL_MPIRUN' in environ else ['mpirun']
MPIRUN[0] = which(MPIRUN[0])
if not exists(MPIRUN[0]):
    raise RuntimeError('Cannot find mpirun')


def mpirun_cmds(**kwargs):
    cmds = list(MPIRUN)
    for k in kwargs:
        mpiarg = '-{}'.format(str(k).replace('_', '-'))
        cmds.append(mpiarg)
        v = kwargs[k]
        if v is not None:
            cmds.append(str(v))
    cmds.extend([executable, THIS_SCRIPT])
    return cmds


def launch_mpirun_task_file(task_file, result_file, **kwargs):
    cmds = mpirun_cmds(**kwargs) + [task_file, result_file]
    print(cmds)
    p = Popen(cmds)
    p.wait()
    if p.returncode != 0:
        raise RuntimeError('Task failed to run')


def mpirun_task_file(task_file, result_file):
    from mpi4py import MPI
    rank = MPI.COMM_WORLD.Get_rank()
    task = deserialize(file=task_file)
    try:
        result = task.compute()
    except:
        result = ExceptionInfo(rank)
    results = MPI.COMM_WORLD.gather(result)
    if rank == 0:
        serialize(results, file=result_file)


if __name__ == '__main__':
    t_file = argv[1]
    r_file = argv[2]
    mpirun_task_file(t_file, r_file)
