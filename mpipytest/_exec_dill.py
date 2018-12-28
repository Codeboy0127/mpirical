import sys

from ._dill import exec_test_dill

if __name__ == '__main__':
    filename = sys.argv[1]
    exec_test_dill(filename)
