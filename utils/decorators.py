from utils.constants import MethodType


def check_pos(method_type=MethodType.INDEX):
    def wrapper(func):
        def decorator(instance, pos):
            if not isinstance(pos, int):
                raise TypeError('Index must be an integer')
            if method_type == MethodType.INDEX:
                if pos >= len(instance):
                    raise IndexError('Index out of range')
            if method_type == MethodType.INSERT:
                if pos > len(instance):
                    raise IndexError('Index out of range')
            if pos < 0:
                raise IndexError('Index must be positive')
            res = func(instance, pos)
            return res
        return decorator
    return wrapper
