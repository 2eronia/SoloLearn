# -*- coding: utf-8 -*-
"""
Created by Serino at 06/09/2018
"""


def add(a, b):
	print(f"ADDING {a}+{b}")
	return a + b


def subtract(a, b):
	print(f"SUBTRACTING {a}-{b}")
	return a - b


def multiply(a, b):
	print(f"MULTIPLYING {a}*{b}")
	return a * b


def divide(a, b):
	print(f"DIVIDING {a}/{b}")
	return a / b


print("Letz do some math\n")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"\nAge:{age}\nHeight:{height}\nWeight:{weight}\nIQ:{iq}\n")

puzzle = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print(f"\n{puzzle}")
