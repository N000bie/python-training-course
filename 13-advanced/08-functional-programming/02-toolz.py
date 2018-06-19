# -*- encoding: utf-8 -*-
import toolz


print_list = lambda x: print(list(x))

l = list(range(25))


# 1. use toolz.curry instead functools.partial
@toolz.curry
def not_multiple_of(x, y):
    return y % x != 0


print_list(filter(not_multiple_of(3), l))
print_list(filter(not_multiple_of(7), l))
print('-' * 20, '\n')


# 2. use toolz.remove
print_list(toolz.remove(toolz.complement(not_multiple_of(3)), l))
print_list(toolz.remove(toolz.complement(not_multiple_of(7)), l))
