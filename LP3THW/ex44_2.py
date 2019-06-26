# -*- coding: utf-8 -*-
"""
Created by Serino at 08/05/2018
"""


class Other:

	def implicit(self):
		print("OTHER implicit()")

	def override(self):
		print("OTHER override()")

	def altered(self):
		print("OTHER altered()")


class Child:

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD, BEFORE OTHER altered()")
		self.other.altered()
		print("CHILD, AFTER OTHER altered()")


son = Child()

print('=' * 20)
son.implicit()
print('=' * 20)
son.override()
print('=' * 20)
son.altered()
