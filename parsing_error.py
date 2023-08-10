#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:28:29 2023

@author: gator
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

#%% Imports
import numpy as np
import pandas as pd

#%% Parameters
# file_name = './GOOG Key Ratios.txt'
file_name = './monthly_in_situ_co2_mlo.csv'
#%% Read csv with pandas
df = pd.read_csv(file_name, skiprows = np.arange(57))

#%% Checke the file
with open(file_name) as f:
    lines = f.readlines()
    
for i_line, line in enumerate(lines[:57]):
    print('Line {0:03d}: {1:03d}'.format(i_line, len(line.split(','))))
    print(line)
