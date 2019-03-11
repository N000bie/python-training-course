import functools

from toolz import thread_last, curry, pipe

print(list(map(lambda x: x + 10, [1, 2, 3])))  # => [11, 12, 13]
print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))  # => [6, 7]
print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))  # => 15

x = functools.reduce(
    lambda x, y: x + y,
    map(lambda x: x + 10,
        filter(lambda x: x > 5, [3, 4, 5, 6, 7])
        )
)  # => 33
print('combine all operations together:', x)

x = thread_last(
    [3, 4, 5, 6, 7],
    (filter, lambda x: x > 5),
    (map, lambda x: x + 10),
    (functools.reduce, lambda x, y: x + y)
)
print('use toolz:', x)

from operator import add, lt
from toolz.curried import filter, map, reduce
add = curry(add)
lt = curry(lt)

x = pipe(
    [3, 4, 5, 6, 7],
    filter(lt(5)),
    map(add(10)),
    reduce(add)
)
print('another toolz style:', x)
