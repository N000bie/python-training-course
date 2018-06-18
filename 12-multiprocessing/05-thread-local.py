# -*- encoding: utf-8 -*-
import threading
from time import sleep


class A:
    var = 0


a = A()


def fun1():
    print('thread 1 sets a.var to 1')
    a.var = 1
    print('in thread 1, a.var =', a.var)


def fun2():
    print('thread 2 sets a.var to 2')
    a.var = 2
    sleep(0.5)
    print('in thread 2, a.var =', a.var)


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t2.start()
t1.start()

sleep(0.6)
print('in main thread, a.var =', a.var)

print('-' * 20)


class B:
    var = threading.local()
    var.value = 0


b = B()


def fun3():
    print('thread 3 sets b.var.value to 3')
    b.var.value = 3
    print('in thread 3, b.var.value =', b.var.value)


def fun4():
    print('thread 4 sets b.var.value to 4')
    b.var.value = 4
    sleep(0.5)
    print('in thread 4, b.var.value =', b.var.value)


t3 = threading.Thread(target=fun3)
t4 = threading.Thread(target=fun4)
t4.start()
t3.start()
sleep(0.6)
print('in main thread, b.var.value =', b.var.value)
