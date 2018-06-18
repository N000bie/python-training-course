# -*- encoding: utf-8 -*-
from threading import Thread, get_ident
from time import sleep
from random import randrange


class CalThread(Thread):
    def run(self):
        rounds = self._kwargs['rounds']
        print('thread %s started' % (get_ident(), ))
        for i in range(rounds):
            sleep(randrange(10, 30) / 10)
            print('thread %s run round %s' % (get_ident(), i + 1))
        print('thread %s finished' % (get_ident(),))


if __name__ == '__main__':
    threads = [CalThread(kwargs={'rounds': 5}) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('all threads done')
