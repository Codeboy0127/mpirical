import cloudpickle
from six import string_types


def serialize(obj, file=None, **kwargs):
    if file is None:
        return cloudpickle.dumps(obj, **kwargs)
    elif isinstance(file, string_types):
        with open(file, 'wb') as f:
            cloudpickle.dump(obj, f)
    else:
        cloudpickle.dump(obj, file)


def deserialize(obj=None, file=None, **kwargs):
    if file is None:
        return cloudpickle.loads(obj)
    elif isinstance(file, string_types):
        with open(file, 'rb') as f:
            return cloudpickle.load(f)
    else:
        return cloudpickle.load(file)
