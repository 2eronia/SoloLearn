# -*- coding: utf-8 -*-
"""
Created by Serino on 2017/9/22
"""


for i in range(10):
	if i > 5:
		print(i)
		break
	else:
		print("7")

print("this is another loop")

for i in range(10):
	if i > 5:
		print(i)
		break
else:
	print("7")

print("this is another loop")

try:
	print(1)
	print(1 + "1" == 2)
	print(2)
except TypeError:
	print(3)
else:
	print(4)
