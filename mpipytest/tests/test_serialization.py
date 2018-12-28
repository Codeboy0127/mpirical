import sys
import pytest
import pickle

from mpipytest.serialization import serialize_test, deserialize_test, SerializableTest


@pytest.fixture
def func_fixture():
    def func(*args, **kwargs):
        return args, kwargs
    return func


@pytest.fixture
def args_fixture():
    return 1, 'a'


@pytest.fixture
def kwargs_fixture():
    return {'x': 2, 'y': 'b'}


@pytest.fixture
def serializable_fixture(func_fixture, args_fixture, kwargs_fixture):
    return SerializableTest(func_fixture, *args_fixture, **kwargs_fixture)


@pytest.fixture
def serialized_test(func_fixture, args_fixture, kwargs_fixture):
    return serialize_test(func_fixture, *args_fixture, **kwargs_fixture)


@pytest.fixture
def deserialized_test(serialized_test):
    return deserialize_test(serialized_test)


def test_serialize_test(serialized_test):
    if sys.version_info[0] == 2:
        assert isinstance(serialized_test, str)
    elif sys.version_info[0] == 3:
        assert isinstance(serialized_test, bytes)


def test_deserialize_test(func_fixture, args_fixture, kwargs_fixture, deserialized_test):
    d_func, d_args, d_kwargs = deserialized_test

    assert d_func.__name__ == func_fixture.__name__
    assert d_args == args_fixture
    assert d_kwargs == kwargs_fixture
    assert d_func(*d_args, **d_kwargs) == func_fixture(*args_fixture, **kwargs_fixture)


def test_serialize_serializable_test(serializable_fixture):
    serialized_test = serializable_fixture.serialize()
    if sys.version_info[0] == 2:
        assert isinstance(serialized_test, str)
    elif sys.version_info[0] == 3:
        assert isinstance(serialized_test, bytes)


def test_deserialize_serializable_test(func_fixture, args_fixture, kwargs_fixture, serializable_fixture):
    d_test = SerializableTest.deserialize(serializable_fixture.serialize())

    assert d_test.func.__name__ == func_fixture.__name__
    assert d_test.args == args_fixture
    assert d_test.kwargs == kwargs_fixture
    assert d_test.run() == func_fixture(*args_fixture, **kwargs_fixture)


def test_deserialize_nontest():
    s_obj = pickle.dumps((1, 'a', {'b': 3}))
    nontest = SerializableTest.deserialize(s_obj)
