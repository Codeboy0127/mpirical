def mpi_bcast(val):
    from mpi4py import MPI
    x_rank = val if MPI.COMM_WORLD.Get_rank() == 0 else None
    x_all = MPI.COMM_WORLD.bcast(x_rank, root=0)
    return x_all
