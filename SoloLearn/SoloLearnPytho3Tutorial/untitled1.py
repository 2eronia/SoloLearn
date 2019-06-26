# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 23:28:35 2017

@author: Serino
"""
import random

p1 = random.randrange(1, 7)
p2 = random.randrange(1, 7)
p3 = random.randrange(1, 7)

print(p1, p2, p3)

'''
def trapezoid_area(base_up, base_down, height = 3):
    print(1 / 2 * (base_up + base_down) * height)


trapezoid_area(3, 2)
'''

'''
for i in range(1, 5):
    for j in range(1, 5):
        print('{} X {} = {}'.format(i, j, i * j))
'''


def add_string(a, b):
    return a + b


test = add_string("hello", "world")
print(test)

x = "zdd"
print(f"Howdy {x}")
