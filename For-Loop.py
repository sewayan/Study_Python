#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:24:55 2019

@author: sebastianwayan
"""

#x = 3
#r = x - 2
#
#if r >= 1:
#    print ("Heya")
#    
#else:
#    print("Neya")
#    
#
#
#print("Penis")
#
#
#x = [1,2,3,4,5,6,7]
#
##print(x)
#
#for i in x:
#    print(i)
#   
#print('----------')
#
#for i in x:
#    if i > 2:
#        print(i)

import os

fileslist = os.listdir(r'/Users/sebastianwayan/Desktop/Bootcamp_Study Material')

print(fileslist)

print('-------------')

pdf_list = [f for f in fileslist if f[-3:]== 'pdf']

print (pdf_list)

