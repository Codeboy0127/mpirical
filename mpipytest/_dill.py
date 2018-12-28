import os
import sys
import dill
import tempfile


def write_test_dill(func, *args, **kwargs):
    fd, fn = tempfile.mkstemp()
    os.close(fd)
    with open(fn, 'wb') as f:
        dill.dump((func, args, kwargs), f)
    return fn


def exec_test_dill(fn):
    with open(fn, 'rb') as f:
        test, args, kwargs = dill.load(f)
    try:
        test(*args, **kwargs)
    except Exception as e:
        print(e, file=sys.stderr)
