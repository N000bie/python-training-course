# -*- encoding: utf-8 -*-
from datetime import datetime, timedelta


def sleep(n):
    enter = datetime.utcnow()
    to = enter + timedelta(seconds=n)
    while datetime.utcnow() < to:
        yield


def create():
    for _ in sleep(3.0):
        yield
    print(datetime.utcnow(), "(1) create file")


def write():
    for _ in sleep(1.0):
        yield
    print(datetime.utcnow(), "(2) write into file")


def close():
    print(datetime.utcnow(), "(3) close file")
    yield


def scheduler(*tasks):
    while tasks:
        current, rest = tasks[0], tasks[1:]
        try:
            next(current)
        except StopIteration:
            print('task %s ends' % (current, ))
            tasks = rest
        else:
            tasks = rest + (current, )


def main():
    print(datetime.utcnow(), 'task begin')
    for _ in create():
        yield _
    for _ in write():
        yield _
    for _ in close():
        yield _


# scheduler(create(), write(), close())
scheduler(main())
