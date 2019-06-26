# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:34:54 2017

@author: Serino
"""

my_name = 'Serino'
my_age = 28
my_height = 1.70 #meter
my_weight = 65 #kilogram
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Letz takl about %s." %my_name
print "He's %d meters tall." %my_height
print "He's %d kilograms heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

#tricky
print "If I add %d, %s and %d I get %s." %(my_age, my_height, my_weight, my_age + my_height + my_weight)

test1 = round (1.756)
print test1

test2 = "1.2"
print my_age + test2 #It will be error.