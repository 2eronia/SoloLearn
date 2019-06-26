# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 00:55:23 2017

@author: Serino
"""

stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print stuff

print '-'*20
stuff['city'] = 'San Francisco'
print stuff

print '-'*20
stuff['city2'] = 'San Francisco2'
stuff['city1'] = 'San Francisco1'
stuff['city3'] = 'San Francisco3'
stuff['city0'] = 'San Francisco0'

#del stuff[*] #error
print stuff
print '-'*20
print stuff.items()

print '-'*20
for i, j in stuff.items():
    print j

print '-'*20
test = stuff.get('name')
print test


if not test:
    print "none at all"