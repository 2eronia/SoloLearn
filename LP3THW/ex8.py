# -*- coding: utf-8 -*-
"""
Created by Serino at 04/02/2018
"""

formatter = "{}{}{} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))

