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
    def func(*arguments, **keywords):
        return arguments, keywords

    args = (1, 'a')
    kwargs = {'x': 2, 'y': 'b'}

    serialized_test = serialize_test(func, *args, **kwargs)
    d_func, d_args, d_kwargs = deserialize_test(serialized_test)

    assert d_func.__name__ == func.__name__
    assert d_args == args
    assert d_kwargs == kwargs
