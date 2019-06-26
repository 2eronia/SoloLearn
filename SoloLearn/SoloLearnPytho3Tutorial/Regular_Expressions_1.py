# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/19 23:14
"""
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

print(re.findall(pattern, "eggspamsausagespam"))
