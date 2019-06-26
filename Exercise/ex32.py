# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 20:45:12 2017

@author: Serino
"""

the_count = [1,2,3,4,5]
fruits = ["apples","oranges","pears","apricots"]
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print "This is count %d" % number
    
for fruit in fruits:
    print "A fruit of type: %s" % fruit
    
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# it is a empty list
elements = []

#use the range function tu do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the 'elements' list." %i
    # append is  a funcion that lists understand
    elements.append(i)
    
#now we can print them out too
for i in elements:
    print "Element was : %d" %i
    
test = range(0, 6)
print test
