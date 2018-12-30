import pytest
import pickle
import dill
import cloudpickle

from serialization import serialize, deserialize


def mpi_bcast(val):
    from mpi4py import MPI
    x_rank = val if MPI.COMM_WORLD.Get_rank() == 0 else None
    x_all = MPI.COMM_WORLD.bcast(x_rank, root=0)
    return x_all


@pytest.fixture
def serialized_mpi_bcast():
    return serialize(mpi_bcast)


@pytest.mark.parametrize('serializers', ([dill], [pickle], [cloudpickle]))
def test_serialize_mpi_bcast(serializers):
    serialize(mpi_bcast, serializers=serializers)


@pytest.mark.parametrize('deserializers', ([dill], [pickle], [cloudpickle]))
def test_deserialize_mpi_bcast(deserializers, serialized_mpi_bcast):
    deserialized_mpi_bcast = deserialize(serialized_mpi_bcast, deserializers=deserializers)
    assert deserialized_mpi_bcast('x') == 'x'
