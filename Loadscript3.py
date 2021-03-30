#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
## Import packages ###########
##############################

import pandas as pd
import numpy as np
import glob
import re
from skimage.io import imread
from skimage.filters import threshold_otsu as to
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

##############################
## Functions #################
##############################

def load_ids(txts):
    '''
    Loads every txt files in one folder and returns a data frame of the ids.
    '''
    files_txt = glob.glob(txts)
    files_txt.sort()
    df_txt = pd.DataFrame(columns=('fileRoot', 'position', 'plantnumber'))
    for file in files_txt:
        print(file)  # just to see which file is processed
        fileRoot = re.sub(".*/", "", file[:-4]) # get filenames

        txtdf = pd.read_csv(file, sep="\s+", header=None)

        df_txt.loc[len(df_txt)] = [fileRoot, 'topleft', txtdf.loc[0, 0]]
        df_txt.loc[len(df_txt)] = [fileRoot, 'topcenter', txtdf.loc[0, 1]]
        df_txt.loc[len(df_txt)] = [fileRoot, 'topright', txtdf.loc[0, 2]]
        df_txt.loc[len(df_txt)] = [fileRoot, 'bottomleft', txtdf.loc[1, 0]]
        df_txt.loc[len(df_txt)] = [fileRoot, 'bottomcenter', txtdf.loc[1, 1]]
        df_txt.loc[len(df_txt)] = [fileRoot, 'bottomright', txtdf.loc[1, 2]]
    return(df_txt)

def load_imgs(tifs):
    '''
    Loads every image files in one folder, slices them, and returns a data frame of the area.
    '''
    files_img = glob.glob(tifs)
    files_img.sort()
    df_img = pd.DataFrame(columns=('fileRoot', 'position', 'area','imageArray'))
    for file in files_img:
        print(file)
        fileRoot = re.sub(".*/", "", file[:-4])

        imgdf = imread(file, key=1)

        df_img.loc[len(df_img)] = [fileRoot, 'topleft', np.sum(imgdf[0:240, 0:213] > to(imgdf[0:240, 0:213])),imgdf[0:240, 0:213]]
        df_img.loc[len(df_img)] = [fileRoot, 'topcenter', np.sum(imgdf[0:240, 213:426] > to(imgdf[0:240, 213:426])),imgdf[0:240, 213:426]]
        df_img.loc[len(df_img)] = [fileRoot, 'topright', np.sum(imgdf[0:240, 426:640] > to(imgdf[0:240, 426:640])),imgdf[0:240, 426:640]]
        df_img.loc[len(df_img)] = [fileRoot, 'bottomleft', np.sum(imgdf[240:480, 0:213] > to(imgdf[240:480, 0:213])),imgdf[240:480, 0:213]]
        df_img.loc[len(df_img)] = [fileRoot, 'bottomcenter', np.sum(imgdf[240:480, 213:426] > to(imgdf[240:480, 213:426])),imgdf[240:480, 213:426]]
        df_img.loc[len(df_img)] = [fileRoot, 'bottomright', np.sum(imgdf[240:480, 426:640] > to(imgdf[240:480, 426:640])),imgdf[240:480, 426:640]]
    return(df_img)

def plot_plant(plantnum):
    '''
    Plots the area against time(points) of a certain plant(number). Takes only 
    an integer (plant number/id).
    '''
    plant_df = total_df[total_df.plantnumber == plantnum]
    plant_df = plant_df.reset_index()
    del plant_df['plantnumber']
    del plant_df['index']
    
    def expon (x,a,k):
        form = a*np.exp(k*x)
        return(form)
    
    x = np.array(plant_df['fileRoot'])
    x=x.astype(int)
    x = x-180800
    y = np.array(plant_df['area'])
    y=y.astype(int)
    popt, pcov = curve_fit(expon, x, y, p0=(4, 0.1))
    global k
    k=popt[1]
    lab = str('Plant #{0}').format(plantnum)
    plt.plot(x, y, 'b.', label=lab)
    y_x = expon(x,*popt)
    plt.plot(x, y_x, 'r-', label='fit, k = %.2f a = %.2f' %(popt[1],popt[0]))
    plt.xlabel('Date')
    plt.ylabel('Area')
    plt.title(lab)
    plt.legend()
    plt.show()
        

##############################
## Loading Procedure #########
##############################

## 1. Run the functions for all folders
txt = ('/home/howsetya/workspace/Bioimage/Dennis_GrowthRate/*/*.txt') # H's path
img = ('/home/howsetya/workspace/Bioimage/Dennis_GrowthRate/*/*.tif') # H's path
txt = ('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/*/*.txt') # D's path
img = ('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/*/*.tif') # D's path

ids = load_ids(txt)
ars = load_imgs(img)

## 2. Merge ids and ars in one big data frame (?)
total_df = ids
total_df = total_df[total_df.fileRoot!='180806_FL-4'] # remove these entry rows
total_df = total_df.reset_index() # reset indexes
del total_df['index']
total_df['area'] = ars['area'] # merge
total_df['imageArray'] = ars['imageArray'] # merge
del total_df['position'] # total_df.drop('position',inplace=True, axis=1) 

## 3. cleanup data frame (fileRoot to just dates and make them int)
x = 0
for names in total_df['fileRoot']:
    name = re.sub(".*/", "", names[:6])
    total_df.loc[x,'fileRoot'] = int(re.sub(".*/", "", name))
    x = x+1
del(names,name,x)

##############################
## Plotting ##################
##############################

## 1. Plot plants number 1-60. Change as necessary.
df_sum=pd.DataFrame(columns=('plantnumber','growth constant(k)'))
for i in  range(1,61):
    plot_plant(i)
    df_sum.loc[len(df_sum)]=(i,k)
    
### Ideas for geeting delta area
# total_df[total_df.plantnumber == 2]["area"][1] -> get the first area of plant 2
# total_df[total_df.plantnumber == 2]["area"][389] -> get the last area of plant 2

#--> With this approach but the original index back. 
#For every plant we have 7 datapoints
#Calculate every 7th area - area 7 steps back  

# =============================================================================
# Summary table
# =============================================================================




##############################
## Questions #################
##############################

## 1. Is threshold otsu ok? why threshold otsu? another method?
## 2. What is the biological question (in detail)? How to answer?
## 3. Some fit fails. Should check the slicing in detail/the area calculation. 