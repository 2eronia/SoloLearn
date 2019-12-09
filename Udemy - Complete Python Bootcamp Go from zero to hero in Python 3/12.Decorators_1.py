# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 12/9/2019
"""


def hello(name):
	print('The hello() function has been executed')

	def greet():
		return '\tthis is the greet() inside func hello'

	def welcome():
		return '\tthis is welcom() inside func hello'

	print("I'm gonna return a func")

	if name == 'Vii':
		return greet
	else:
		return welcome


my_new_func = hello('V')
print(my_new_func)
