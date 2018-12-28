import sys
import pytest

from mpipytest.serialization import serialize_test, deserialize_test


@pytest.fixture
def global_func():
    def func(*args, **kwargs):
        return args, kwargs
    return func


@pytest.fixture
def global_func_args():
    return 1, 'a'


@pytest.fixture
def global_func_kwargs():
    return {'x': 2, 'y': 'b'}


@pytest.fixture
def serialize_global_func(global_func, global_func_args, global_func_kwargs):
    return serialize_test(global_func, *global_func_args, **global_func_kwargs)


@pytest.fixture
def deserialize_global_func(serialize_global_func):
    return deserialize_test(serialize_global_func)


def test_serialize_test(serialize_global_func):
    if sys.version_info[0] == 2:
        assert isinstance(serialize_global_func, str)
    elif sys.version_info[0] == 3:
        assert isinstance(serialize_global_func, bytes)


def test_deserialize_test_global(global_func, global_func_args, global_func_kwargs, deserialize_global_func):
    d_func, d_args, d_kwargs = deserialize_global_func

    assert d_func.__name__ == global_func.__name__
    assert d_args == global_func_args
    assert d_kwargs == global_func_kwargs
    assert d_func(*d_args, **d_kwargs) == global_func(*global_func_args, **global_func_kwargs)


def test_deserialize_test_local(global_func_args, global_func_kwargs):
    def local_func(*args, **kwargs):
        return args, kwargs

    serialized_test = serialize_test(local_func, *global_func_args, **global_func_kwargs)
    d_func, d_args, d_kwargs = deserialize_test(serialized_test)

    assert d_func.__name__ == local_func.__name__
    assert d_args == global_func_args
    assert d_kwargs == global_func_kwargs
    assert d_func(*d_args, **d_kwargs) == local_func(*global_func_args, **global_func_kwargs)
