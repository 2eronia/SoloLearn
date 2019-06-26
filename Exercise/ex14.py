# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 22:53:56 2017

@author: Serino
"""

from sys import argv

script, user_name = argv
prompt = "> "

print "Hi, %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s." % user_name
likes = raw_input(prompt)

print "Where do you live %s." % user_name
lives = raw_input(prompt)

print "What kinda computer do you have?"
computer = raw_input(prompt)

print '''
Alright, so you said %r about liking me.
You live in %r.
And you have a %r computer. Nice.
''' % (likes, lives, computer)