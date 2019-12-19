import pytest
import mpirical


@pytest.mark.parametrize('n,rank,result', [
    (4, 'all', [0, 1, 2, 3]),
    (4, [1, 3], [1, 3]),
    (4, 0, 0),
])
def test_get_rank(n, rank, result):

    @mpirical.mpirun(return_rank=rank, n=n)
    def get_ranks():
        from mpi4py import MPI
        return MPI.COMM_WORLD.Get_rank()

    assert get_ranks() == result


def test_raise_exception():

    @mpirical.mpirun(n=2)
    def raise_exception():
        from mpi4py import MPI
        if MPI.COMM_WORLD.Get_rank() == 1:
            raise ValueError
        else:
            return None

    with pytest.raises(ValueError):
        raise_exception()


@mpirical.mpirun(np=4)
def test_decorated_test():
    from mpi4py import MPI
    rank = MPI.COMM_WORLD.Get_rank()
    value = MPI.COMM_WORLD.bcast(rank, root=2)
    assert value == 2


@pytest.mark.xfail
@mpirical.mpirun(n=2)
def test_decorated_test_failure():
    def f1():
        raise ValueError('TEST')

    def f2():
        f1()

    def f3():
        f2()

    from mpi4py import MPI
    rank = MPI.COMM_WORLD.Get_rank()
    if rank == 1:
        f3()
