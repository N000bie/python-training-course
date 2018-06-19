# -*- encoding: utf-8 -*-
from functools import wraps


def log_it(f):
    @wraps(f)
    def _wrapper(*args, **kwargs):
        print('enter function %s, args: %s, kwargs %s ' % (f.__name__, args, kwargs))
        ans = f(*args, **kwargs)
        print('leave function %s, return: %s' % (f.__name__, ans))
        return ans
    return _wrapper


@log_it
def add(a, b):
    return a + b


print(add(1, 2))
