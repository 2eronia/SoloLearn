# -*- coding: utf-8 -*-

'''
def factorial(x):
    if x == 1:
        return 1
    else:
        return  x * factorial(x - 1)

print(factorial(6))
'''


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)


num = int(input(">>>"))
print(is_odd(num))
print(is_even(num))


def f():
    print("Hello")
