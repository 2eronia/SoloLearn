# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:36:24 2017

@author: Serino
"""

nums = set()
for i in range(9):
    nums.add(i)

'''
while len(nums) > 0:
    #print(len(nums))
    print(nums)
    nums.pop()

'''

for num,num2 in enumerate(nums):
    print(num, num2)
