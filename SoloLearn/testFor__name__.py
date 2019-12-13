# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 7/9/2019
"""
import __name__N__main__

# import would also execute

'''
If the source file is executed as the main program, 
the interpreter sets the __name__ variable to have a value “__main__”. 
 
If this file is being imported from another module, 
__name__ will be set to the module’s name.

__name__ is a built-in variable which evaluates to the name of the current module. 
'''

print(f"File2 __name__ = {__name__}")

if __name__ == "__main__":
    print("File2 is being run directly")
else:
    print("File2 is being imported")
