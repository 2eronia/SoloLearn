# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/10 21:48
"""


class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3, 4, 5])
print(queue)
queue.push(-1)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
