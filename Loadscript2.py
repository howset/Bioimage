#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:04:54 2021

@author: dennis
"""

import pandas as pd
import numpy as np
import glob
import re
from skimage.io import imread, imshow
from skimage.filters import threshold_otsu as to

## Process txt-files

files_txt = glob.glob('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/*/*.txt')
files_txt = glob.glob('/home/howsetya/workspace/Bioimage/Dennis_GrowthRate/*/*.txt')
files_txt.sort()
df_txt = pd.DataFrame(columns=('fileRoot','position','plantnumber'))

#dict={}
    
for file in files_txt:
    print(file) # just to see which file is processed
    fileRoot=re.sub(".*/","",file[:-4])

    txtdf = pd.read_csv(file,sep="\s+",header=None) 
    
    df_txt.loc[len(df_txt)] = [fileRoot, 'topleft', txtdf.loc[0,0]]
    df_txt.loc[len(df_txt)] = [fileRoot, 'topcenter', txtdf.loc[0,1]]
    df_txt.loc[len(df_txt)] = [fileRoot, 'topright', txtdf.loc[0,2]]
    df_txt.loc[len(df_txt)] = [fileRoot, 'bottomleft', txtdf.loc[1,0]]
    df_txt.loc[len(df_txt)] = [fileRoot, 'bottomcenter', txtdf.loc[1,1]]
    df_txt.loc[len(df_txt)] = [fileRoot, 'bottomright', txtdf.loc[1,2]]
    
#df_txt.sort_values(by=['fileRoot'])
    
   # dict[fileRoot,'topleft'] = txtdf.loc[0,0]
   # dict[fileRoot, 'topcenter'] = txtdf.loc[0,1]
   # dict[fileRoot, 'topright'] = txtdf.loc[0,2]
   # dict[fileRoot, 'bottomleft'] = txtdf.loc[1,0]
   # dict[fileRoot, 'bottomcenter'] = txtdf.loc[1,1]
   # dict[fileRoot, 'bottomright'] = txtdf.loc[1,2]


## Process Images

files_img = glob.glob ('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/*/*.tif')
files_img = glob.glob('/home/howsetya/workspace/Bioimage/Dennis_GrowthRate/*/*.tif')
files_img.sort()                      
df_img = pd.DataFrame(columns=('fileRoot','position','area'))
for file in files_img:
    print(file)
    fileRoot=re.sub(".*/","",file[:-4])
    
    imgdf = imread(file,key=1) 
    
    df_img.loc[len(df_img)] = [fileRoot, 'topleft', np.sum(imgdf[0:240,0:213] > to(imgdf[0:240,0:213]))]
    df_img.loc[len(df_img)] = [fileRoot, 'topcenter', np.sum(imgdf[0:240,213:426] > to(imgdf[0:240,213:426]))]
    df_img.loc[len(df_img)] = [fileRoot, 'topright', np.sum(imgdf[0:240,426:640] > to(imgdf[0:240,426:640]))]
    df_img.loc[len(df_img)] = [fileRoot, 'bottomleft', np.sum(imgdf[240:480,0:213] > to(imgdf[240:480,0:213]))]
    df_img.loc[len(df_img)] = [fileRoot, 'bottomcenter',np.sum(imgdf[240:480,213:426] > to(imgdf[240:480,213:426]))]
    df_img.loc[len(df_img)] = [fileRoot, 'bottomright', np.sum(imgdf[240:480,426:640] > to(imgdf[240:480,426:640]))]


## Merge df_txt and df_img
df_txt['Area']=df_img['area'] 
df_merged=df_txt


# =============================================================================
# Matplotlib
# https://publish.illinois.edu/olaogunbayo/2015/09/29/exponential-functions-ordinary-differential-equations-simulations-2/
# https://www.epythonguru.com/2020/09/python-exponential-growth-model.html
# =============================================================================

# Also was du bekommst ist die Fläche der Pflanzen über Zeit. Da die Pflanze exponentiell wächst, 
# fitten wir die Datenpunkte auf die first order exponential growth equation y(t) = e^(kt). 
# Dabei ist t der Zeitpunkt und k die Wachstumskonstante. 
# Die Wachstumskonstante ist quasi das Wachstum pro Zeiteinheit (hier nehmen wir Tage). 
# --> so which value has k in our case ?? Maybe 7 because we have data points from 7 days?


from scipy.integrate import odeint
from matplotlib import pyplot as plt







