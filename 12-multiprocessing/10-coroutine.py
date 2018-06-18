# -*- encoding: utf-8 -*-
import asyncio


@asyncio.coroutine
def create():
    yield from asyncio.sleep(3.0)
    print("(1) create file")


@asyncio.coroutine
def write():
    yield from asyncio.sleep(1.0)
    print("(2) write into file")


@asyncio.coroutine
def close():
    print("(3) close file")


@asyncio.coroutine
def test():
    yield from create()
    yield from write()
    yield from close()
    yield from asyncio.sleep(2.0)
    loop.stop()


loop = asyncio.get_event_loop()
asyncio.ensure_future(test())
loop.run_forever()
loop.close()
