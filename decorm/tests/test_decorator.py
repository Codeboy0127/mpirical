import pytest
import decorm


def test_get_rank():

    @decorm.mpirun(nprocs=4)
    def get_ranks():
        from mpi4py import MPI
        return MPI.COMM_WORLD.Get_rank()

    assert get_ranks() == [0, 1, 2, 3]


def test_raise_exception():

    @decorm.mpirun(nprocs=2)
    def raise_exception():
        from mpi4py import MPI
        if MPI.COMM_WORLD.Get_rank() == 1:
            raise RuntimeError
        else:
            return None

    with pytest.raises(RuntimeError):
        raise_exception()
