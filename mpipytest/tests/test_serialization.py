import pytest
import pickle
import dill
import cloudpickle

from serialization import serialize, deserialize
from tests.utils import mpi_bcast, serialized_mpi_bcast


@pytest.mark.parametrize('serializers', ([dill], [pickle], [cloudpickle]))
def test_serialize_mpi_bcast(serializers):
    serialized_bcast = serialize(mpi_bcast, serializers=serializers)
    assert isinstance(serialized_bcast, (str, bytes))


@pytest.mark.parametrize('deserializers', ([dill], [pickle], [cloudpickle]))
def test_deserialize_mpi_bcast(deserializers, serialized_mpi_bcast):
    deserialized_mpi_bcast = deserialize(serialized_mpi_bcast, deserializers=deserializers)
    assert deserialized_mpi_bcast('x') == 'x'
