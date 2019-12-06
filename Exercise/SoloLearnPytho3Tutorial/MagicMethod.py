# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/4 22:32
"""


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5, 7)
second = Vector2D(6, 9)
result_1 = first + first
result_2 = second + second
result_3 = first + second

print(result_1.x, result_1.y)
print(result_2.x, result_2.y)
print(result_3.x, result_3.y)
print(result_1.x)
print(result_1.y)
