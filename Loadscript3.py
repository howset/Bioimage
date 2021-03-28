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
    df_img = pd.DataFrame(columns=('fileRoot', 'position', 'area'))
    for file in files_img:
        print(file)
        fileRoot = re.sub(".*/", "", file[:-4])

        imgdf = imread(file, key=1)

        df_img.loc[len(df_img)] = [fileRoot, 'topleft', np.sum(imgdf[0:240, 0:213] > to(imgdf[0:240, 0:213]))]
        df_img.loc[len(df_img)] = [fileRoot, 'topcenter', np.sum(imgdf[0:240, 213:426] > to(imgdf[0:240, 213:426]))]
        df_img.loc[len(df_img)] = [fileRoot, 'topright', np.sum(imgdf[0:240, 426:640] > to(imgdf[0:240, 426:640]))]
        df_img.loc[len(df_img)] = [fileRoot, 'bottomleft', np.sum(imgdf[240:480, 0:213] > to(imgdf[240:480, 0:213]))]
        df_img.loc[len(df_img)] = [fileRoot, 'bottomcenter', np.sum(imgdf[240:480, 213:426] > to(imgdf[240:480, 213:426]))]
        df_img.loc[len(df_img)] = [fileRoot, 'bottomright', np.sum(imgdf[240:480, 426:640] > to(imgdf[240:480, 426:640]))]
    return(df_img)


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

## 2. Merge ids and ars

total_df = ids
total_df = total_df[total_df.fileRoot!='180806_FL-4'] # remove these entry rows
total_df = total_df.reset_index() # reset indexes
del total_df['index']
total_df['area'] = ars['area'] # merge
del total_df['position'] # total_df.drop('position',inplace=True, axis=1) 

##############################
## Plotting ##################
##############################

