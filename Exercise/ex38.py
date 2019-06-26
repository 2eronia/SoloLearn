# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:45:16 2017

@author: Serino
"""
'''
test =[]
for i in range(0,9):
    test.append(i)

print test

test2 = test.pop(3)
print test2
test2 = test.pop(5)
print test2
test2 = test.pop()
print test2
test2 = test.pop()
print test2
test2 = test.pop()
print test2
test2 = test.pop()
print test2
test2 = test.pop()
print test2
print test
'''

ten_number = "One Two Three Four Five"
stuff_test = ten_number.split(' ',1)
stuff = ten_number.split() #at here, it's same as .split(' ')

print stuff_test
print stuff
print stuff[-3:-1]
print stuff[2:4]
print stuff[1:4]

print len(stuff)

more_stuff = ['5', '6', '7', '8', '9', '10']

while len(stuff) < 10:
    next_one = more_stuff.pop() #u can also use stuff[x] x+=1 method instead
    print "Adding:", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print stuff
print stuff[-1]
print ' '.join(stuff)
'''
print "wait"
print ' '.join(stuff)
join_stuff = stuff.join(' ', stuff) #error
print join_stuff
'''
print "wait"
print stuff
print '#'.join(stuff[2:5])
print stuff[2:6]

'''
print stuff[-1]
print stuff.pop()
print stuff[-1]
print stuff.pop()
print stuff[-1]
'''
'''
class Thing(object):
    def test(hi):
        print "hi"
a = Thing()
a.Thing("guy")
'''