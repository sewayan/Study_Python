#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:02:37 2020

@author: sebastianwayan
"""
import matplotlib.pyplot as plt
import pandas as pd


# xs = [1, 2, 3] #Werte auf der x-Achse
# ys = [4, 7, 4] #Werte auf der y-Achse

# plt.plot(xs, ys)


#-----Aufgabe Geburtsstatisken------------
"""
Find out how often the name "Max"
has been given as surname in California between 1950 and 2000 (both years included)
"""

filepath = r"/Users/sebastianwayan/Desktop/Codes/python/Python Test Data/Python_Bootcamp_Materials/Kursmaterialien/data/names.csv"

names = pd.read_csv(filepath) #OG-file with all data

# plot_test = names.plot(kind = 'scatter', x= 'Name', y = 'Year')

df_max = names.loc[(names['Name'] == 'Max') & (names['State'] == 'CA') & (names['Year'] >= 1950) & (names['Year'] <= 2000)]

plot_max = df_max.plot(kind = 'bar', x = 'Year', y = 'Count')

