# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:43:13 2018

@author: ChenHu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 08:45:05 2018

@author: ChenHu
"""

#import math
import pandas as pd
import numpy as np

dust=pd.read_csv('Tradamm.csv', sep=';')

# calculate the sum of column index 1
total_mass=dust.iloc[:,1].sum()

# column 2 is the mass fraction in [%] of particle size range
dust.iloc[:,2]=dust.iloc[:,1]*100/total_mass

meshSize=np.arange(0,7,1)

# column 6 is the accumulated mass fraction of particle size range
dust.iloc[:,3]=np.cumsum(dust.iloc[:,2])

# check in which region the DXX is located and then make the interpolation
D10=np.interp(10,[dust.iloc[0,3], dust.iloc[1,3]], [63, 75])
D25=np.interp(25,[dust.iloc[1,3], dust.iloc[2,3]], [75,125])
D50=np.interp(50,[dust.iloc[3,3], dust.iloc[4,3]], [180,250])
D75=np.interp(75,[dust.iloc[4,3], dust.iloc[5,3]], [250, 355])
D90=np.interp(90,[dust.iloc[5,3], dust.iloc[6,3]], [355,500])
