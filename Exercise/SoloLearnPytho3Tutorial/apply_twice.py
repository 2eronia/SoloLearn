# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:23:09 2017

@author: Serino
"""


def apply_twice(func, arg):
    return func(func(arg))


def add_5(x):
    return x + 5


print(add_5(add_5(10)))
print(apply_twice(add_5, 7))


def apply_triple(func, arg):
    return func(func(func(arg)))


print(apply_triple(add_5, 7))
