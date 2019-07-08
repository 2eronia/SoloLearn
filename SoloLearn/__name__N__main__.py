# -*- coding: utf-8 -*-
"""
Created by serin at 7/9/2019
"""

# __name__ = "__main__"

def print_name():
	print(f"File1 __name__ = {__name__}")

	if __name__ == "__main__":
		print("File1 is being run directly")
	else:
		print("File1 is being imported")


print(f"File1 __name__ = {__name__}")

print("before __name__ guard")
if __name__ == "__main__":
	print_name()
print("after __name__ guard")

'''
def functionA():
	print("a1")
	from __name__N__main__ import functionB
	print("a2")
	functionB()
	print("a3")

def functionB():
	print("b")

print("t1")
if __name__ == "__main__":
	print("m1")
	functionA()
	print("m2")
print("t2")
'''
