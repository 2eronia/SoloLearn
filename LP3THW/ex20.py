# -*- coding: utf-8 -*-
"""
Created by Serino at 06/09/2018
"""


def print_all(f):
	print(f.read())


def rewind(f):
	f.seek(0)


def print_a_line(line_count, f):
	print(line_count, f.readline(), end = "")  # You can add 'end = "" ' to avoid adding double \n


current_file = open(input("File Name ? >>"))

print("1st, letz print the whole fiile:\n")

print_all(current_file)

print("Now letz rewind, kinda like a tape.")

rewind(current_file)

print("Letz pring three lines:")

current_line = 1
print_a_line(current_line, current_file, )

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
