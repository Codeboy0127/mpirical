import pickle
import cloudpickle
import dill


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


def deserialize(serialized_obj, *args, **kwargs):
    deserializers = kwargs.pop('deserializers', [dill, cloudpickle, pickle])
    unsuccessful = True
    last_exception = None
    deserialized_obj = None
    while deserializers and unsuccessful:
        deserializer = deserializers.pop(0)
        try:
            deserialized_obj = deserializer.loads(serialized_obj, *args, **kwargs)
        except Exception as e:
            last_exception = e
        else:
            unsuccessful = False
    if unsuccessful and last_exception is not None:
        raise last_exception
    else:
        return deserialized_obj
