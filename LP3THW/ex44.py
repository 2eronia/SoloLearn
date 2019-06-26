# -*- coding: utf-8 -*-
"""
Created by Serino at 08/05/2018
"""


class Parent:

	def implicit(self):
		print("PARENT implicit()")

	def override(self):
		print("PARENT override()")

	def altered(self):
		print("PARENT altered()")


class Child(Parent):

	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print("=" * 20)
dad.override()
son.override()

print("=" * 20)
dad.altered()
print("-" * 20)
son.altered()
