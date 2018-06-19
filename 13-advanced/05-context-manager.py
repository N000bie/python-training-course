# -*- encoding: utf-8 -*-
from contextlib import contextmanager


@contextmanager
def bookmark(f):
    pos = f.tell()
    try:
        yield f
    finally:
        f.seek(pos)


with open('01-rot13.py') as f:
    posx = f.tell()
    try:
        with bookmark(f) as bf:
            print(bf.read(10))
            raise Exception()
    except:
        pass
    finally:
        posy = f.tell()
        print(posx, posy)
        assert posx == posy

