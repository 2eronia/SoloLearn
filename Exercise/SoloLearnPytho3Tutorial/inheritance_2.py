# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 23:23:52 2017

@author: Serino
"""


class A:
    def method(self):
        print(1)


class B(A):
    def method(self):
        print(2)


B().method()
