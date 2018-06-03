"""

Author: Samrat Banerjee
Date: 01-06-2018
Description: Names, Variables, Code, Functions

"""

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2=args
    print("arg1: %r,arg2: %r"%(arg1,arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print("arg1: %r,arg2: %r"%(arg1,arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: %r"%arg1)

# this takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Samrat","Banerjee")
print_two_again("Sammy","Whammy")
print_one("Sam")
print_none()
