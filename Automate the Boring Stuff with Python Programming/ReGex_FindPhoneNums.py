# -*- coding: utf-8 -*-
"""
Created by Serino at 10/15/2018
"""

import re

message = 'call me 123-1234-1234 or 122-1233-1233'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.findall(message)
print(f'the phone Nums in message is {matchObject}')

