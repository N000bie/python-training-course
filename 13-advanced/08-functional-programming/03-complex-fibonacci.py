import itertools


def fibonacci():
    p, p_1 = 1, 1
    yield p_1

    while True:
        yield p
        p, p_1 = p + p_1, p


def positive_integers():
    i = 1
    while True:
        yield i
        i += 1


def take_n(iterable, n):
    for i in iterable:
        if n <= 0:
            break
        yield i
        n -= 1


def take_odd(iterable):
    for i in iterable:
        if i % 2 == 1:
            yield i


def take_even(iterable):
    for i in iterable:
        if i % 2 == 0:
            yield i


def take_even_pos(iterable):
    for idx, i in enumerate(iterable):
        if idx % 2 == 0:
            yield i


def take_between(iterable, low, high):
    for i in iterable:
        if i < low:
            continue
        elif i > high:
            break
        yield i


def drop_until(iterable, low):
    for i in iterable:
        if i < low:
            continue
        yield i


def take_until(iterable, high):
    for i in iterable:
        if i > high:
            break
        yield i


def take_between_v2(iterable, low, high):
    for i in take_until(drop_until(iterable, low), high):
        yield i


for i in take_between_v2(take_even(fibonacci()), 100, 1000):
    print(i)


print(
    list(
        itertools.takewhile(
            lambda i: i <= 1000,
            itertools.dropwhile(
                lambda i: i < 100, filter(lambda i: i % 2 == 0, fibonacci())
            ),
        )
    )
)
