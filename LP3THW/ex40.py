# -*- coding: utf-8 -*-
"""
Created by Serino at 07/01/2018
"""


class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't wan to get sue",
                   "So I'll stop right here"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
