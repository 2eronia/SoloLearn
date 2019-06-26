# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 20:54:00 2017

@author: Serino
"""

'''
from sys import argv   #import feature

script, filename = argv   #unpacking

txt = open(filename)   #give varieble "txt" a function
   # reading the file we put in commands line 

print "Here's your file %r:" % filename   #just print a MSG
print txt.read()   #print the text source we gave before
'''

print "Type the filename:"   #justj print a MSG
file_again = raw_input("> ")   #put in a file's name

txt_again = open(file_again)   #open function

print txt_again.read()      #read function
print txt_again.close() 