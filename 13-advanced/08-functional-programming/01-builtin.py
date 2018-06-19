# -*- encoding: utf-8 -*-
from functools import partial

print_list = lambda x: print(list(x))

l = list(range(25))

# 1. plain filter

print_list(filter(lambda x: x % 3 != 0, l))
print_list(filter(lambda x: x % 7 != 0, l))
print('-' * 20, '\n')


# 2. reusable function generation
def not_multiple_of(x):
    def _f(y):
        return y % x != 0
    return _f


print_list(filter(not_multiple_of(3), l))
print_list(filter(not_multiple_of(7), l))
print('-' * 20, '\n')


# 3. use python partial
def not_multiple_of(x, y):
    return y % x != 0


not_3x = partial(not_multiple_of, 3)
not_7x = partial(not_multiple_of, 7)
print_list(filter(not_3x, l))
print_list(filter(not_7x, l))
print('-' * 20, '\n')
