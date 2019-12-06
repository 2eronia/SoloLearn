# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/23 22:49
"""
import re

pattern = r"pam"

match = re.search(pattern, "12345eggspamsausagespamspameggs")

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
