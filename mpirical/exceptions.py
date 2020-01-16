from sys import exc_info

from six import reraise


class ExceptionInfo(object):
    """A wrapper class for exceptions and traceback information"""

    def __init__(self, rank):
        self.rank = rank
        self.info = exc_info()

    def reraise(self):
        reraise(*self.info)
