# -*- encoding: utf-8 -*-
import asyncio


async def create():
    await asyncio.sleep(3.0)
    print("(1) create file")


async def write():
    await asyncio.sleep(1.0)
    print("(2) write into file")


async def close():
    print("(3) close file")


async def test():
    await create()
    await write()
    await close()
    await asyncio.sleep(2.0)
    loop.stop()


loop = asyncio.get_event_loop()
asyncio.ensure_future(test())
loop.run_forever()
loop.close()
