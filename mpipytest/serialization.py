import pickle
import dill
import logging

logger = logging.getLogger(__name__)


def serialize_test(func, *args, **kwargs):
    unsuccessful = True
    serializers = [pickle, dill]
    serialized_test = None
    while unsuccessful and serializers:
        serializer = serializers.pop(0)
        try:
            serialized_test = serializer.dumps((func, args, kwargs))
        except AttributeError:
            pass
        else:
            unsuccessful = False
    if unsuccessful:
        raise AttributeError(('failed to serialize test {} with arguments {} and '
                              'keyword arguments {}').format(func, args, kwargs))
    return serialized_test


def deserialize_test(serialized_test):
    unsuccessful = True
    deserializers = [pickle, dill]
    func, args, kwargs = None, None, None
    while unsuccessful and deserializers:
        deserializer = deserializers.pop(0)
        try:
            func, args, kwargs = deserializer.loads(serialized_test)
        except AttributeError:
            pass
        else:
            unsuccessful = False
    if unsuccessful:
        raise AttributeError('failed to deserialize test {}'.format(serialized_test))
    return func, args, kwargs


class Test(object):
    """A class that contains a function and its arguments"""

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        return self.func(*self.args, **self.kwargs)

    def __repr__(self):
        return '<{}: func={} args={} kwargs={}>'.format(self.__class__.__name__, self.func, self.args, self.kwargs)


class SerializableTest(Test):
    """A Test that can serialize itself"""

    def serialize(self):
        unsuccessful = True
        serializers = [pickle, dill]
        serialized_test = None
        while unsuccessful and serializers:
            serializer = serializers.pop(0)
            try:
                serialized_test = serializer.dumps(self)
            except AttributeError:
                pass
            else:
                unsuccessful = False
        if unsuccessful:
            raise AttributeError('failed to serialize Test {!r}'.format(self))
        return serialized_test

    @staticmethod
    def deserialize(serialized_test):
        unsuccessful = True
        deserializers = [pickle, dill]
        deserialized_test = None
        while unsuccessful and deserializers:
            deserializer = deserializers.pop(0)
            try:
                deserialized_test = deserializer.loads(serialized_test)
            except AttributeError:
                pass
            else:
                unsuccessful = False
        if unsuccessful:
            raise AttributeError('failed to deserialize {}'.format(serialized_test))
        if not isinstance(deserialized_test, Test):
            logger.warning('deserialized object is not a Test')
        return deserialized_test
