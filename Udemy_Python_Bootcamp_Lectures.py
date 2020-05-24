#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:45:08 2020

@author: sebastianwayan
"""

import random

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

#-----------------
# Control structures (if,else)| Comparison| Loops

# Lecture 23| Control structures

n = 80

if n < 51:
    print("Die Zahl " + str(n) +" ist kleiner als 51")
else:
    print("Die Zahl " + str(n) + " ist größer als 51")

#-----------------

# Lecture 24 | Comparisons
# Operators for comparisons: "<", ">", "==", "<=", ">="

print(6 < 100) # gives back a boolean

n1 = 32423545
n2 = 123

result = n1 * n2

if result > 100000:
    print("Das Ergebnis" + str(n) + " ist größer als 100.000")
else:
    print("Nö, is kleiner")

#-----
# chaining comparisons (booleans)

age = 45

if age >= 30 and age <= 39:
    print("This person is in his/her 30's and " + str(age) + " years old")
else:
    if age < 30:
        print("Roaring twenties")
    else:
        print("Golden Age")

# ---- another Example -----
country = "USA"
age = 20

if (country == "USA" and age >= 21) or (country != "USA" and age >= 18): #beide Seite der Bedingunge getrennt durch "and" müssen "True" sein
    print("Is legally allowed to consume alcohol")
else:
    print("Is not allowed to consume alcohol")

#-------------------
# Lecture 28 | Comparisons and lists

if "student2" in students:
    
    print("Monikkaaaaa")
else:
    print("AAAAYYYEEE")

#-----------------
# Lecture 29| "not" operator

annual_income = 120000
threshold = 100000

if not annual_income >= threshold:
    print("Your income is below the threshold of " + str(threshold) + " bucks per year. You are not financially wealthy")
else:
    print("Your income is above the threshold of " + str(threshold) + " bucks per anno. Congratz, you win at capitalism")

#--------another Example------

names = ["Ezo", "Lena"]

if "Moritz" not in names:
    print("Moritz is nich hier")
else:
    print("Moritz is hier")


if not "Moritz" in names: # Unterschied lediglich in der Berechnung der Query; funktioniert auch. Syntax "unschön"
    print("Moritz is nich hier")
else:
    print("Moritz is hier")
    
#----------------------
# Lecture 32| elif - Operator
currency = "HKD"

def multi_if(currency):
    #multiple conditions and outcomes
    #funktioniert noch nicht wie erwartet
    if currency == "€" or "Euro":
        print("Euro")
    else:
        if currency == "$" or "USD":
            print("US- Dollar")
        else:
            if currency == "¥" or "Yen":
                print("Japanischer Yen")

# multi_if(currency) 
            

if currency == "€":
    print("Euro")
else:
        if currency == "$":
            print("US- Dollar")
        else:
                if currency == "¥":
                    print("Japanischer Yen")

# same example with "elif"
if currency == "$":
    print("US-Dollar")
elif currency == "€":
    print("Euro")
elif currency == "¥":
    print("Yen")
else:
    print ("Currency not in recognized")    
    
#-----------------
# Lecture 33 | while -loop
# "Bereich wird solange wiederhol werden soll, solange eine Bedingung erfüllt ist. Codeblock wird mehfrfach ausgeführt

counter = 0

while counter < 10:
    print(counter)
    print("and another one")
    counter = counter + 1 #w/o counter +1 -> endless looping

#-----------------
# Lecture 34 | for - loop
# for-loops are best used if "range" of the loop is known

for i in range(0,10): # not a "real" list, but object that acts like a list
    print(i)
    print("DJ Khaled")

liste = [5,6,8]

for i in liste:
    print(i)
#-------------------
# Lecture 37| break & continue
for i in range(0,10):
    if i == 3:
        continue #means in this case that i is skipped when == 3, this loop cycle is skipped
    print(i) #prints number range except '3'


for i in range(0,1000):
    if i == 70:
        break #stops loop when i == 70
    print(i) #prints only to '69'

# Example: I want to stop adding when summe of liste > 400
list = [1,4,6,3,7,9,563]

summe = 0

for element in list:
    summe = summe + element # adds numbers 1; 1+4; 5+6; etc.
    if summe > 400:
        break # breaks BEFORE addition would be > than 400
    print(summe)
    
summe = summe + 1

#-------------------
# Exkurs Trump-Twitter-Bot

print(random.randint(0, 400)) #generates random e.g. int in certain range

#lists of tweet "parts"

part1 = ["Putin","Hillary","Obama","Fake News","Mexico", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["no talent", "on the way down", "really poor numbers", "nasty tone", "looking like a fool", "bad hombre"]
part3 = ["got destroyed by my ratings", "rigged election", "had much smaller crowd", "will pay for the wall"]
part4 = ["So Sad", "Apologize", "So true", "Media won't report", "Big Trounble", "Fantastic Job", "Stay tuned"]
part5 = ["#cofeve", "#stablegenius"]

# warp lists of parts into list

best_words = [part1, part2, part3, part4, part5]

print(best_words[4]) #just checking different parts of the list
print(len(part1)) #checking the length of a list to know the range for the random()

# build the tweet generator

sentence = []

for part in best_words:
    r = random.randint(0, len(part) -1)# "select an element between e.g. 0 - 6, (length of list part1 = 7 -> 7-1 = 6 , start counting from zero"
    #print(part[r])
    sentence.append(part[r])
    print(" ".join(sentence) + "!11!!eins!elf")
    
#-------------------








