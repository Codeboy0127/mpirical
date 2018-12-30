import pytest
import pickle
import dill
import cloudpickle

from serialization import serialize


def mpi_bcast(val):
    from mpi4py import MPI

    x_rank = val if MPI.COMM_WORLD.Get_rank() == 0 else None
    x_all = MPI.COMM_WORLD.bcast(x_rank, root=0)

    return x_all


@pytest.mark.parametrize('serializers', ([dill], [pickle], [cloudpickle]))
def test_serialize_mpi_bcast_cloudpickle(serializers):
    serialize(mpi_bcast, serializers=serializers)
