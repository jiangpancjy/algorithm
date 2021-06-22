from utils.constants import MethodType


def check_pos(method_type=MethodType.INDEX):
    def wrapper(func):
        def decorator(instance, pos, *args, **kwargs):
            if not isinstance(pos, int):
                raise TypeError('linked list index must be an integer')
            if method_type == MethodType.INDEX:
                if pos >= len(instance) or abs(pos) > len(instance):
                    raise IndexError('linked list index out of range')
            if method_type == MethodType.INSERT:
                if pos > len(instance) or abs(pos) > len(instance) + 1:
                    raise IndexError('linked list index out of range')
            res = func(instance, pos, *args, **kwargs)
            return res
        return decorator
    return wrapper
