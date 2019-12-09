# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 12/9/2019
"""

s = 'Global Variable'


def check_for_locals():
	b = 'Local Variable'
	print(locals())


print('\n-------***-------\n')
check_for_locals()
print('\n-------***-------\n')
print(globals())
print('\n-------***-------\n')
print(globals().keys())
print('\n-------***-------\n')
print(globals().values())
print('\n-------***-------\n')
print(globals()['s'])