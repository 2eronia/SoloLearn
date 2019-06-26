# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/8 20:41
"""
import random


class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(0, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont) * 2)


vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
