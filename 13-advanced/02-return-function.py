# -*- encoding: utf-8 -*-
def increase_by(x):
    def _f(y):
        print('%s + %s = ' % (x, y))
        return x + y
    return _f


add_2 = increase_by(2)

print(add_2(3))
print(add_2(5))

add_4 = increase_by(4)

print(add_4(3))
print(add_4(5))
