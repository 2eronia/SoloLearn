# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/10 22:33
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def Square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.Square(6)
print(square.calculate_area())
