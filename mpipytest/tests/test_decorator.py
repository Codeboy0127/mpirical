from mpipytest import mpitest

import pytest


def func(*args, **kwargs):
    if 'error' in kwargs and kwargs['error']:
        raise AttributeError()
    return 'SUCCESS'


def test_func():
    retval = func()
    assert retval == 'SUCCESS'


@mpitest()
def test_func_raises_error():
    with pytest.raises(AttributeError):
        func(error=True)


@mpitest()
def test_func_with_no_argument_decorator():
    retval = func()
    assert retval == 'SUCCESS'


@mpitest(nprocs=4)
def test_func_with_decorator():
    retval = func()
    assert retval == 'SUCCESS'

@mpitest(nprocs=2)
def test_false():
    assert False
