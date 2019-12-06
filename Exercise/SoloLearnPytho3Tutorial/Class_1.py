# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/9/30 17:17
"""


class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def bark(self):
        print("Woof!")


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(rover.color)
rover.bark()
