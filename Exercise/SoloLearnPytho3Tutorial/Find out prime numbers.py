# -*- coding: utf-8 -*-
"""
Created on Ded 11 22:21:23 2017

@author: Serino
"""
import math

import pysnooper

'''
def is_prime(x):
	if x > 1:
		n = x // 2  # floor division
		for i in range(2, n + 1):
			if x % i == 0:  # mod x by i from 2 to n
				return False
		return True
	else:
		return False  # make sure x is greater than 1
'''


@pysnooper.snoop()
def is_prime(x):
	if x % 2 == 0 and x > 2:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True


'''
def count_prime(num):
	prime = [2]
	x = 3
	if num < 2:
		return False
	while x <= num:
		for y in [z for z in prime if z <= int(math.sqrt(num)) + 1]:
			# if y <= int(math.sqrt(num)) + 1:
			if x % y == 0:
				x += 2
				break
		else:
			prime.append(x)
			x += 2
	return prime


print(count_prime(int(input("Input a Num:"))))

'''

num = int(input("input a num greater than 1 >>> "))

# print("Your input number is " + str(num))
print("The prime numbers under your input are:")


def yield_prime_nums(x):  # use 'yield' function to list prime nums
	for i in range(x + 1):
		if is_prime(i):  # if a num is prime, write it in a [list]
			yield i


print(list(yield_prime_nums(num)))
