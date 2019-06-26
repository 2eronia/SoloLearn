# -*- coding: utf-8 -*-
"""
Created by Serino at 2017/10/25 21:18
"""
import re

pattern = r"(egg)(spam)*"

if re.match(pattern, "eggspamspamegg"):
    print("Match 1")