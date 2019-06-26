# -*- coding: utf-8 -*-
"""
Created by Serino at 07/15/2018
"""


# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass


# is-a
class Dog(Animal):

	def __init__(self, name):
		self.name = name  # has-a


# is-a
class Cat(Animal):

	def __init__(self, name):
		self.name = name  # has-a


# is-a
class Person(object):

	def __init__(self, name):
		self.name = name  # has-a
		self.pet = None  # Person has-a pet of some kind


# has-a
class Employee(Person):

	def __init__(self, name, salary):
		super(Employee, self).__init__(name)  # a strange magic
		self.salary = salary  # has-a


# is-a
class Fish(object):
	pass


# is-a
class Salmon(Fish):
	pass


# is-a
class Halibut(Fish):
	pass


# rover is-a dog
rover = Dog("Rover")

# is-a
satan = Cat("Satan")

# is-a
mary = Person("Mary")

# has-a
mary.pet = satan

# has-a
frank = Employee("Frand", 120000)

# is-a
flipper = Fish()

# is-a
crouse = Salmon()

# is-a
harry = Halibut()
