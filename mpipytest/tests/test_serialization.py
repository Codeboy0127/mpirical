import sys
import pytest
import pickle
import dill
import cloudpickle

from mpipytest.serialization import serialize, deserialize
from tests.utils import mpi_bcast


def test_serialize_mpi_bcast_default():
    serialized_mpi_bcast = serialize(mpi_bcast)
    if sys.version_info[0] == 2:
        assert isinstance(serialized_mpi_bcast, str)
    elif sys.version_info[0] == 3:
        assert isinstance(serialized_mpi_bcast, bytes)


@pytest.mark.parametrize('serializers', ([dill], [pickle], [cloudpickle]))
def test_serialize_mpi_bcast(serializers):
    serialized_mpi_bcast = serialize(mpi_bcast, serializers=serializers)
    if sys.version_info[0] == 2:
        assert isinstance(serialized_mpi_bcast, str)
    elif sys.version_info[0] == 3:
        assert isinstance(serialized_mpi_bcast, bytes)


def test_deserialize_mpi_bcast_default():
    serialized_mpi_bcast = serialize(mpi_bcast)
    deserialized_mpi_bcast = deserialize(serialized_mpi_bcast)
    assert deserialized_mpi_bcast('x') == mpi_bcast('x')


@pytest.mark.parametrize('deserializers', ([dill], [pickle], [cloudpickle]))
def test_deserialize_mpi_bcast(deserializers):
    serialized_mpi_bcast = serialize(mpi_bcast, serializers=deserializers)
    deserialized_mpi_bcast = deserialize(serialized_mpi_bcast, deserializers=deserializers)
    assert deserialized_mpi_bcast('x') == mpi_bcast('x')
