# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/10 22:09
"""


class Spam:
    __egg=8
    def print_egg(self):
        print(self.__egg)

s=Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)