# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/9/30 19:15
"""



class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def puur(self):
        print("Purr")


class Dog(Cat):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
