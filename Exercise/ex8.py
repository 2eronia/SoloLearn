# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:50:59 2017

@author: Serino
"""

formatter0 = "%s %s %s %s"

print formatter0 % (1, 2, 3, 4)
print formatter0 % ("one", "tow" ,"three", "four") #What if I put in Chinese
print formatter0 % (True, False, False, True)
print formatter0 % (formatter0, formatter0, formatter0, formatter0)
print formatter0 % (
        "I had this thing.",
        "That you could type up right.",
        "BUt it didn't sing.",
        "So I said goodnight."
        )

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "tow" ,"three", "four") #What if I put in Chinese
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "BUt it didn't sing.",
        "So I said goodnight."
        )