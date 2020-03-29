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

print("The best names for a corgi on this day are " + corgi_names[4] + " & " + corgi_names[0] + ". #" +str(100) + "%")

# Lecture 12 | "Lists" pop() - function
# removes LAST element in a list

corgi_names.append("shitface")
print(corgi_names)

pop_corgi = corgi_names.pop()
print(corgi_names)
print(pop_corgi) # NOTE: the element that has been popped <can be written into a variable for further use

#----------------

# Lecture 15| data type conversion/ type casting

# Situation: Source of valuse can not be altered, values are read as string

a = "35"
b = "45"
c = "5.3"
d = "75.2"
e = 41

#we want to sum numbers
print(a + b) # just concats two strings

print(int(a) + int(b)) # strings are type casted into integer, can be summed up

print(float(c) + float(d)) # Kommazahl = floating point number

sentence = ("Ich schreibe einen random Satz zum Thema typecast mit den Werten " + str(int(a) * float(d)) + str(e)) #Calculation inside brackets with "int" and "float", casted as sring to be able to concat
print(sentence)

# type casting for lists

students = ["student1", "student2", "student3", "student4"]

students_as_string = (", ".join(students)) #casts from datatype "list" to "string" by joining a seperator
print(students_as_string)

#casting from "string" to list by split() at seperator
# then count elements in list (e.g. after scrapping data/ information from web)
i = students_as_string
students_casted_list = i.split(", ")

print(students_casted_list)
print(len(students_casted_list))