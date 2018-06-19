# -*- encoding: utf-8 -*-
import itertools
import operator


def is_incr(a):
    a1 = a[:-1]
    a2 = a[1:]
    cmp = list(map(lambda x: x[0] < x[1], zip(a1, a2)))
    print(cmp)
    return all(cmp)


print(is_incr([1, 2, 3]))
print(is_incr([1, 1, 2]))
print(is_incr([3, 2, 1]))


def is_incr_ex(a):
    return all(itertools.starmap(operator.lt, zip(a[:-1], a[1:])))


print(is_incr_ex([1, 2, 3]))
print(is_incr_ex([1, 1, 2]))
print(is_incr_ex([3, 2, 1]))
