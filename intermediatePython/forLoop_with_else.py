# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 12/6/2019
"""


def yield_prime_nums(num):
	for i in range(2, num):
		for j in range(2, i // 2):
			if i % j == 0:
				break
		else:
			yield i


print(list(yield_prime_nums(int(input("input a number:")))))
