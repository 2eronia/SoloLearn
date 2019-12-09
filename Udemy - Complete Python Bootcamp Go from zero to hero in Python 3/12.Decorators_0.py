# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 12/7/2019
"""


def a_decrorator(original_func):
	def wrap_func():
		print('Some extra code before the original func')
		original_func()
		print('Some extra code after the original func')

	return wrap_func


@a_decrorator
def func_needs_decorator():
	print('I want to be decorated')


# decrotated_func = a_decrorator(func_needs_decorator)
# decrotated_func()

func_needs_decorator()
