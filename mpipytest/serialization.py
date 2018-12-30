import pickle
import cloudpickle
import dill


def pickle_serialize(obj, *args, **kwargs):
    return pickle.dumps(obj, *args, **kwargs)


def dill_serialize(obj, *args, **kwargs):
    return dill.dumps(obj, *args, **kwargs)


def cloudpickle_serialize(obj, *args, **kwargs):
    return cloudpickle.dumps(obj, *args, **kwargs)


def serialize(obj, *args, **kwargs):
    serializers = kwargs.pop('serializers', [dill, cloudpickle, pickle])
    unsuccessful = True
    last_exception = None
    serialized_obj = None
    while serializers and unsuccessful:
        serializer = serializers.pop(0)
        try:
            serialized_obj = serializer.dumps(obj, *args, **kwargs)
        except Exception as e:
            last_exception = e
        else:
            unsuccessful = False
    if unsuccessful and last_exception is not None:
        raise last_exception
    else:
        return serialized_obj
