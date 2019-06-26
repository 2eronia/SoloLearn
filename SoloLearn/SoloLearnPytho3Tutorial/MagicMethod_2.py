# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/4 23:20
"""


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __mod__(self, other):
        #u can use other Magic Method, it has no functionality within.
        line = "+" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("spam")
hello = SpecialString("Hello World!")

print(spam % hello)
