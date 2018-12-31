import decormpi


def test_get_rank():

    @decormpi.mpirun(nprocs=4)
    def get_ranks():
        from mpi4py import MPI
        return MPI.COMM_WORLD.Get_rank()

    assert get_ranks() == [0, 1, 2, 3]
