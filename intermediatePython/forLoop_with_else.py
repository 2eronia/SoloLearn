# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 12/6/2019
"""

import pysnooper
import time


# @pysnooper.snoop()
def yield_prime_nums(num):
	for i in range(2, num + 1):
		for j in range(2, i // 2):
			if i % j == 0:
				break
		else:
			yield i


input_num = int(input("input a number:\n"))
t0 = time.time()
prime_nums_output = print(list(yield_prime_nums(input_num)))

t1 = time.time()
print('Time required:', t1 - t0)
