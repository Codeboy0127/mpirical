import sys

from mpipytest.serialization import serialize_test, deserialize_test


def test_serialize_test_type():
    def test_func(*args, **kwargs):
        return args, kwargs

    serialized_test = serialize_test(test_func, 1, 'a', x=2, y='b')

    if sys.version_info[0] == 2:
        assert isinstance(serialized_test, str)
    elif sys.version_info[0] == 3:
        assert isinstance(serialized_test, bytes)


def test_deserialize_test():
    def test_func(*args, **kwargs):
        return args, kwargs

    args = (1, 'a')
    kwargs = {'x': 2, 'y': 'b'}

    serialized_test = serialize_test(test_func, *args, **kwargs)
    deserialized_test = deserialize_test(serialized_test)

    assert deserialized_test == (args, kwargs)
