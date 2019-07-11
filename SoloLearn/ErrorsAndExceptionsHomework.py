# -*- coding: utf-8 -*-
"""
Created by serin at 7/11/2019
"""

'''
import pysnooper


def ask_for_int():
	while True:
		try:
			n = int(input('Please input a num: '))
		except:
			print('Try again')
			continue
		else:
			print(f'Your num squared is {n**2}')
			break
'''



def ask_for_int():
	try:
		n = int(input('Please input a num: '))
	except:
		print('Try again')
		ask_for_int()
	else:
		print(f'Your num squared is {n**2}')


ask_for_int()
