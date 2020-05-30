#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:50:11 2020

@author: sebastianwayan
"""

"""
Functions as method to structure code

"""

def multi_print(): # Definiton of function
    print("Hallo Welt")
    print("Hallo Welt, nochmal")

def multi_print2(name):
    print(name)
    print(name)


# multi_print() # execution of function

# multi_print2("Kaiser") #Parameter is given when executing and used by defined function

#---------
#function with multiple parameters

# i = 0

def multi_print3(name, count):
    """ 
    multiple Parameter are given to the function
    """
    for i in range(0, count):
        print(name)
        # i = i+1 # counter is not necessary here

def trigger_funct(): #function that triggers other pre-defined functions
    multi_print3("Hana", 6)
    multi_print2("RIP")

# multi_print3("Bertha", 3)

# trigger_funct()

#------------------

def maximum(a, b): 
    """return" = returns value, but is needed to be assigend to a variable
    and e.g. used further, printed etc."""
    if a > b:
        return b
    else:
        return a


result = maximum(1234, 65485432)
print(result)
#-------------------------
# Function "variable.function"
# there are function that are specifically executable on/with functions

list = [1, 2, 4]

list.append(4)

print(list)

text = ("Hallo,Welt")

text.split(",")

print(text)
#-------------------------












