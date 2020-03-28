# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:39:40 2019

@author: DE102242
"""

import os
import pandas as pd

folderpath = (r'C:\Users\DE102242\Documents\Tasks\ACTIVE_Pizza&Beer_FISD-Tool\Data')

filesdict = {}

for file in os.listdir(folderpath):
    if file.lower().endswith('.xlsx'):
        filesdict[file.split(".")[0]] = pd.read_excel(os.path.join(folderpath, file), converters = {"MANDT": lambda x: str(x)})
        
print(filesdict['A002'])
