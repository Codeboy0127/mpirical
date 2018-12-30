import pytest
import pickle
import dill
import cloudpickle

from serialization import pickle_serialize, dill_serialize, cloudpickle_serialize, serialize


def mpi_bcast(val):
    from mpi4py import MPI

    x_rank = val if MPI.COMM_WORLD.Get_rank() == 0 else None
    x_all = MPI.COMM_WORLD.bcast(x_rank, root=0)

    return x_all


def test_serialize_mpi_bcast_pickle():
    pickle_serialize(mpi_bcast)


def test_serialize_mpi_bcast_dill():
    dill_serialize(mpi_bcast)


def test_serialize_mpi_bcast_cloudpickle():
    cloudpickle_serialize(mpi_bcast)


@pytest.mark.parametrize('serializers', ([dill], [pickle], [cloudpickle]))
def test_serialize_mpi_bcast_cloudpickle(serializers):
    serialize(mpi_bcast, serializers=serializers)
