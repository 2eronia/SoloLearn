# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 12/21/2019
"""

from sympy import sieve
import time

t0 = time.time()
primes = list(sieve.primerange(1, 10001))
print(primes)
t1 = time.time()
print('Time required:', t1 - t0)