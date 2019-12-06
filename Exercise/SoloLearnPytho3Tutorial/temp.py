# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

filename = input("Enter a filename:")

with open(filename) as f:
    text = f.read()


def count_char(text, char):
    count = 0
    for i in text:
        if i == char:
            count += 1
    return count


print(count_char(text, "r"))
