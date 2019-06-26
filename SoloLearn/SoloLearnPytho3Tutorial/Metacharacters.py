# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/25 20:40
"""
import re

pattern1 = r"gr.y"
pattern2 = r"^gr.y$"
pattern3 = r"[aeiou][bcd]"
pattern4 = r'[^a-z]'

# Any letter out of "aeiou", then any out of "bdd"
# [1-5][0-9] match Any two-digit number from 10 to 59

# re.match re.search

if re.search(pattern1, "stinggggray"):
    print("Match 1")

if re.search(pattern2, "gray"):
    print("Match 2")

if re.search(pattern3, "QWERT"):
    print("Match 3")

if re.search(pattern3, "qwert"):
    print("Match 4")

if re.search(pattern3, "qwertabcd"):
    print("Match 5")

if re.search(pattern4, "abcdefg"):
    print("Match 6")

if re.search(pattern4, "1234abcdQWERT"):
    print("Match 7")
