# -*- coding: utf-8 -*-
"""
Created by Serino at 05/27/2018
"""


def print_two(*args):
	arg1, arg2 = args
	print(f"arg1:{arg1}, arg2:{arg2}")


def pring_two_again(arg1, arg2):
	print(f"arg1:{arg1}, arg2:{arg2}")


def print_none():
	print("I got nothing'.")


print_two("Dr.", "Serino")
pring_two_again("Mrs", "Luxxanna")
print_none()
