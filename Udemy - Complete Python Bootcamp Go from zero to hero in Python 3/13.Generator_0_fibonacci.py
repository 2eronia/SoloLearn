# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 12/28/2019
"""


def gen_fibon(n):
	a = 1
	b = 1
	for i in range(n):
		yield a
		a, b = b, a + b
