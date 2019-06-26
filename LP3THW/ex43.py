# -*- coding: utf-8 -*-
"""
Created by Serino at 08/03/2018
"""

from random import randint
from sys import exit


class Death(object):
	quips = [
		"You dead. U kinda suck at this."
		"Ur Mom would be proud...if she were smarter."
		"Such a looooser."
		"I have a small puppy that's better at this."
		"You'er worse than ur Dad's jokes."
	]

	@classmethod
	def __init__(self):
		print(Death.quips[randint(0, len(self.quips) - 1)])
		exit(1)


Death()
