# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/5 0:30
"""


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __mod__(self, other):
        for i in range(len(other.cont) + 1):
            print(i)
            print(other.cont[:i])
            print(other.cont[i:])


spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam % eggs
