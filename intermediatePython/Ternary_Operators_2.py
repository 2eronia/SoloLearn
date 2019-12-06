# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 12/7/2019
"""

'''
>>> True or "Some"
True
>>>
>>> False or "Some"
'Some'
The first statement (True or "Some") will return True and the second statement (False or "Some") will return Some.
'''

output = None
msg = output or "No data returned"
print(msg)
