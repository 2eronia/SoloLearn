# -*- coding: utf-8 -*-
"""
Created by Serino at 06/24/2018
"""

elements = []


# for i in range(6):
# 	elements.append(i)
#
# print(elements)


def add_element(i):
	if i > 5:
		return
	else:
		elements.append(i)
		print(elements.pop(0))
		return add_element(i + 1)


add_element(0)

for i in elements:
	print(i, end = "")

print(elements)
