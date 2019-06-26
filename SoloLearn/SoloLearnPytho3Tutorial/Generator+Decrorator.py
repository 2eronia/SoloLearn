# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:44:50 2017

@author: Serino
"""


def decor(func):
    def wrap():
        print("=" * 20)
        func()
        print("=" * 20)

    return wrap


def countdown(x):
    while x > 0:
        yield x
        x -= 1


num = int(input(">>>"))


#@decor
def print_list():
    print(list(countdown(num)))


print_result = decor(print_list)
print_result()