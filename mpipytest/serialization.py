import pickle
import dill


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
