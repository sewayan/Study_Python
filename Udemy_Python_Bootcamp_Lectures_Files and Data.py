#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:27:48 2020

@author: sebastianwayan
"""

#---------------

"""
How to work with files

"""

# write a text file

file = open("writes_testfile.txt", "w") # w == write-mode

hs_students = ["Harald", "Banu", "Sarah", "Biene", "Alex"]

for student in hs_students:
    file.write(student + "\n") # datei wird default in den selben Ordner geschrieben in dem die py-file liegt
    
file.close()

#---------------------
# open a file (and automatically close)

with open("writes_testfile.txt", "r") as text:
    for line in text:
        print(line)
# Datei ist hier wieder geschlossen


 