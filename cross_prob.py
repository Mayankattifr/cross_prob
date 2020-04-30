#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:19:11 2020

@author: mayank
"""


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:37:39 2018

@author: mayank
"""

import matplotlib
import matplotlib.pyplot as plt
from astropy.io import ascii
import matplotlib.cm as cm
import pandas as pd
from scipy import stats
import numpy as np
from scipy.interpolate import interp1d
from astropy import units as u

from astropy.coordinates import SkyCoord

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelsize'] = 25
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] =17
plt.rcParams['legend.fontsize'] = 17
plt.rcParams['figure.titlesize'] = 12
plt.rcParams['axes.labelweight']='bold'



plt.rcParams['axes.linewidth'] = 3
plt.rcParams['xtick.major.size'] = 15
plt.rcParams['xtick.minor.size'] = 8
plt.rcParams['ytick.major.size'] = 15
plt.rcParams['ytick.minor.size'] = 5

plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['ytick.minor.visible'] = True
plt.rcParams['ytick.major.size'] = 10


plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#plt.rcParams['xtick.top'] = True
#plt.rcParams['ytick.right'] = True



import random 
RA_exo=np.array(random.sample(range(0,10000),570))/10000.0
DEC_exo=np.array(random.sample(range(0,10000),570))/10000.0
#%%
def check():
    count=0
    count2=0
    RA=np.random.random_sample()
    DEC=np.random.random_sample()
    idx=[]
    source=[]
    sep=[]
    c1 = SkyCoord(RA_exo*u.degree, DEC_exo*u.degree,frame='fk5')
    c2 = SkyCoord(RA*u.degree, DEC*u.degree,frame='fk5')
    d2d = c1.separation(c2)
    catalogmsk = d2d < 0.002*u.deg    
    #print(c1)
    #print(d2d*u.deg   )
    #print("######################")
    idxcatalog = (np.where(catalogmsk)[0])    
    #print(idxcatalog)
    a=idxcatalog
    #len(a)
    if(len(a)>0):
        count2=count2+1 
    return(count2)
a=[]
sep2=[]
count1=0

while(count1<10000):
    a.append(check())
    print(count1)
    count1=count1+1
    
#%%
print(sum(a)*100.0/10000.0)