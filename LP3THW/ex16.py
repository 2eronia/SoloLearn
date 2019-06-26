# -*- coding: utf-8 -*-
"""
Created by Serino at 04/16/2018
"""

line1 = "this is line1"
line2 = "this is line2"
line3 = "this is line3"

fileName = input("filename>>")
target = open(fileName ,"w+")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

target.close()
