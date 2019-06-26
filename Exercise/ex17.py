# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 17:43:08 2017

@author: Serino
"""

from sys import argv
from os.path import exists

script, from_file, to_file =argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()
#use "r" mode could make these two line into one?

print "The input file is %d bytes long" % len(indata)
print "Ready, hit ENTER to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, it's done."

out_file.close()
in_file.close()
