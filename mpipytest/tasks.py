class Task(object):
    """A serializable object containing a function and arguments"""

    def __init__(self, func, *args, **kwargs):
        if not callable(func):
            raise ValueError('Task function not callable')
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def compute(self):
        return self.func(*self.args, **self.kwargs)
