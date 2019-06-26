# -*- coding: utf-8 -*-
"""
Created by Serino at 06/30/2018
"""

from collections import OrderedDict

# create a mapping of state to abbreviation
states = {
	'Oregon'    : 'OR',
	'Florida'   : 'FL',
	'California': 'CA',
	'New York'  : 'NY',
	'Nevada'    : 'NV',
	'Michigan'  : 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
	'NV': 'Las Vegas'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 15, 1)
print("NY States has:", cities['NY'])
print('OR State has:', cities['OR'])

# print some states
print('-' * 15, 2)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# do it by using states then cities dict
print('-' * 15, 3)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# print every state abbreviation
print('-' * 15, 4)
print(list(states.items()))
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated as {abbrev}")

# print every city in state
print('-' * 15, 5)
print(list(cities.items()))
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 15, 6)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated as {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-' * 15, 7)

# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does No Exist')
print(f"The city for the state 'TX' is: {city}")

print('-' * 15, 8)
print(states)
order_dict_test = OrderedDict(sorted(states.items(), key = lambda t: len(t[0])))
print(order_dict_test)
