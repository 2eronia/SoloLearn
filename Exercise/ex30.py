# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 21:54:01 2017

@author: Serino
"""

people = 30
cars = 30
buses = 30

if cars > people:
    print "We should take the cars."
elif cars <= people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We can't decide."
    
if  people >= buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."