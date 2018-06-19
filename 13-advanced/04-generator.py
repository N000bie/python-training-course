# -*- encoding: utf-8 -*-
def double_numbers(end):
    for i in range(end):
        print("produce a number")
        yield i + i


d = double_numbers(3)
print(d)
print(list(d))
