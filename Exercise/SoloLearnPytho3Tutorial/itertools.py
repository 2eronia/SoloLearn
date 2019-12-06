# -*- coding: utf-8 -*-
"""
Created by Serino on 2017/9/22
"""
from itertools import count, accumulate, takewhile, product, permutations

nums = set()

for i in count(3):
    nums.add(i)
    if i >= 11:
        print(nums)
        break

nums_2 = list(accumulate(range(8)))
nums_3 = list(takewhile(lambda x: x <= 5, nums_2))

# TODO
letters = ("A", "B", "X")
letters = ("A", "B", "X")
print(list(product(letters, nums_2, nums_3)))
print(list(permutations(letters)))
