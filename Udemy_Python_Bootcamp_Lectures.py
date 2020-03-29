#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:45:08 2020

@author: sebastianwayan
"""

# Part: 2 | Lecture: 8 "Strings"

name = "Sebo"
age = "21"

integer1 = 123.4
integer2 = 12


print ("Mein Name ist " + name + " und ich bin " + age + " Jahre alt")

print ("Die beste Zahl heut ist " + str(integer1)) # Workaround: transform integer to string

print((integer1 + integer2) * 12)

#----------------

# Lecture 10 "Lists"

corgi_names = ["Potatz", "Charles Barkley", "Bootz", "LowRy"]

corgi_names.append("Mr.Wiggles")

print(corgi_names)

print(corgi_names[:2]) # slicing position 0 -2 

print(len(corgi_names)) # getting info about a list

print("The best names for a corgi on this day are" + corgi_names[4] + " & " + corgi_names[0] + ". #" +str(100) + "%")

#----------------
