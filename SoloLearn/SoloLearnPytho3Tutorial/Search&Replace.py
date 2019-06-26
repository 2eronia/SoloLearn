# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/23 23:10
"""
import re

Hello = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Serino", Hello)

print(newstr)
