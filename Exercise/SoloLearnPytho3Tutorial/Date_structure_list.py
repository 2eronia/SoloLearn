# -*- coding: utf-8 -*-
"""
Created by Serino at 12/24/2017
"""

import time

a = []
t0 = time.clock()
for i in range(0, 20000):
    a.append(i)
print(time.clock() - t0, "s")

t0 = time.clock()
b = [i for i in range(0, 20000)]
print(time.clock() - t0, "s")

g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
print(g)

