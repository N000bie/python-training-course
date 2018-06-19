import functools

print(list(map(lambda x: x + 10, [1, 2, 3])))  # => [11, 12, 13]
print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))  # => [6, 7]
print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))  # => 15

x = functools.reduce(
    lambda x, y: x + y,
    map(lambda x: x + 10,
        filter(lambda x: x > 5, [3, 4, 5, 6, 7])
        )
)       # => 33
print(x)
