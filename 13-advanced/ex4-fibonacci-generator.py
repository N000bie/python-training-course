import itertools


def fib():
    p1, p2 = 1, 0
    while True:
        yield p1
        p1, p2 = p1 + p2, p1


print('take first 10 elements:')
print(list(itertools.islice(fib(), 10)))

print('take first 10 even elements:')
print(list(itertools.islice(filter(lambda x: x % 2 == 0, fib()), 10)))

print('take elements less than 40:')
print(list(itertools.takewhile(lambda x: x < 40, fib())))

print('take elements > 20 and < 70:')
print(list(itertools.takewhile(
    lambda x: x < 70,
    itertools.dropwhile(
        lambda x: x <= 20,
        fib()
    )
)))
