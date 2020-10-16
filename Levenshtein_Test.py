#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:02:17 2020

@author: sebastianwayan
"""
import pandas as pd
import Levenshtein as lev
from itertools import product

# making test dict

data1 = {'Company Name': ['Bose', 'AMG', 'Penispumper', 'John Reed', 'Redland Seafood']}
data2 = {'Company Name': ['Bose', 'AMG', 'Penispumer', 'Join Red', 'Redland Saefood']}

# making df's

df1 = pd.DataFrame(data1, columns = ['Company Name'])
df2 = pd.DataFrame(data2, columns = ['Company Name'])

"""
Levenshtein Distance

1st step: combine the df that you want to compare
2nd step: compare with lev
"""

compare_df = pd.DataFrame(product(df1['Company Name'], df2 ['Company Name']), columns = ["Company 1", "Company 2"])

compare_df["LevScore"] = compare_df.apply(lambda x: lev.distance(x[0],x[1]), axis=1)