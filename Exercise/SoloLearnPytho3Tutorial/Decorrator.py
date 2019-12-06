# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:32:36 2017

@author: Serino
"""


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


def print_text():
    print("Hello world!")


decorated = decor(print_text)
decorated()
