# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/19 22:48
"""

'''
names = ['Bob', 'Alice', 'Joshua']
for index, value in enumerate(names):
    print(f'{index}:{value}')
'''


def my_func(**kwargs):
    print(kwargs)


my_func(a = 3, b = 4, d = "f")

for i in range(10):
    print(i)
