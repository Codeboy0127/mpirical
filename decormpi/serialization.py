import pickle
import cloudpickle
import dill

from six import string_types


def _open_file(file=None, write=True):
    file_obj = None
    file_mode = 'wb' if write else 'rb'
    must_close = False
    if file:
        if isinstance(file, string_types):
            file_obj = open(file, file_mode)
            must_close = True
        else:
            file_obj = file
    return file_obj, must_close


def _method_wrapper(obj, module=dill, write=True, file=None, **kwargs):
    file_obj, must_close = _open_file(file, write)

    if write and file:
        method = 'dump'
        args = (obj, file_obj)
    elif write and not file:
        method = 'dumps'
        args = (obj,)
    elif not write and file:
        method = 'load'
        args = (file_obj,)
    else:
        method = 'loads'
        args = (obj,)

    if hasattr(module, method):
        return_val = getattr(module, method)(*args, **kwargs)
    else:
        module_name = module.__name__ if hasattr(module, '__name__') else str(module)
        raise AttributeError('Module {} has no {} method'.format(module_name, method))

    if must_close:
        file_obj.close()

    return return_val


def _try_methods(obj, modules=None, write=True, file=None, **kwargs):
    if modules is None:
        modules = [dill, cloudpickle, pickle]

    unsuccessful = True
    last_exception = None
    new_obj = None
    while modules and unsuccessful:
        module = modules.pop(0)
        try:
            new_obj = _method_wrapper(obj, module=module, write=write, file=file, **kwargs)
        except Exception as e:
            last_exception = e
        else:
            unsuccessful = False
    if unsuccessful and last_exception is not None:
        raise last_exception
    else:
        return new_obj


def serialize(obj, serializers=None, file=None, **kwargs):
    if serializers:
        modules = list(serializers)
    else:
        modules = list(kwargs.pop('modules', [dill, cloudpickle, pickle]))
    return _try_methods(obj, modules=modules, write=True, file=file, **kwargs)


def deserialize(obj=None, deserializers=None, file=None, **kwargs):
    if deserializers:
        modules = list(deserializers)
    else:
        modules = list(kwargs.pop('modules', [dill, cloudpickle, pickle]))
    return _try_methods(obj, modules=modules, write=False, file=file, **kwargs)
