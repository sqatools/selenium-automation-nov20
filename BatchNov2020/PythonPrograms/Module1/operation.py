"""
1. user one function from one file to another file
import modulename

2. user specific variable or function from another module

from module import <function>  <variable>

from module import *

3. Scope of global variable will be accessible across all the module.
4. We can access local variable out side of module and function

"""

a = 20

def addition():
    b = 30
    c = 40
    d = b + c
    return d