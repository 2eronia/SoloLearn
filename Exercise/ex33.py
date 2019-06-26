# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 22:35:24 2017

@author: Serino
"""

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num