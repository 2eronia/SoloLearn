# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:15:27 2017

@author: Serino
"""


def add_five(x):
	return x + 5


nums = [11, 22, 33, 44, 55]

result = list(map(add_five, nums))

print(result)

result_2 = list(map(lambda x:x + 5, nums))

print(result_2)

res = list(filter(lambda x:not x % 2 == 0, nums))
res_set = set(res)
print(res)
print(res_set)
