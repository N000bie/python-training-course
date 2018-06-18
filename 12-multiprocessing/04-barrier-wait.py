# -*- encoding: utf-8 -*-
from threading import Thread, get_ident, Barrier
from time import sleep
from random import randrange


class CalThread(Thread):
    def run(self):
        rounds = self._kwargs['rounds']
        barrier = self._kwargs['barrier']
        print('thread %s started' % (get_ident(),))
        for i in range(rounds):
            sleep(randrange(10, 30) / 10)
            print('thread %s run round %s' % (get_ident(), i + 1))
        barrier.wait()
        print('thread %s finished' % (get_ident(),))


if __name__ == '__main__':
    N = 5
    barrier = Barrier(N + 1)
    threads = [CalThread(
        kwargs={'rounds': 5, 'barrier': barrier}
    ) for i in range(N)]
    for t in threads:
        t.start()
    barrier.wait()
    print('parent done')
