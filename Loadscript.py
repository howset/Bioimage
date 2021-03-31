#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:17:11 2021

@author: howard & dennis

!!! This script is now obsolete! See gcCalc.py !!!

The plan here is to run this whole script once for one directory. This is 
obviously not the best approach. But more refinement can be done as time 
permits (and energy too).

The script will load the images and then slice the images (according to the 
6 boxes-grid). And then save it somehow in a usable format.

Then probably the binarization (turn them to black-white) and area calculation 
can be done in another script.

Still to do:
    1. grid slicing - done!
    2. how to connect sliced flower images to the txt data - done
    3. Connect the flower images with their corresponding number to the pixel size

"""
# test git
### Set work directory. Change directory accordingly.

import os
os.chdir('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/180801')
os.chdir('/home/howset/workspace/Bioimage/') ## comment this out 

###############################################################################
### Deal with images ##########################################################
###############################################################################

### Load image into filelist. Change directory accordingly.

import glob
fList = glob.glob('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/180801/*.tif')
fList = glob.glob('Dennis_GrowthRate/180801/*.tif') ## comment this out
fList.sort() # sort the list, not really necessary

### Get only filename.

def splitname (filelist):
    '''Splits path and filename. Takes a list as input, outputs only the image
    names without the path.'''
    namelist=[]
    for n in range(len(filelist)):
        x1 = filelist[n]
        x1 = str(x1)
        x1 = x1.split(sep='/')
        x1 = str(x1[-1])
        print(x1,type(x1))
        x1 = x1.split(sep='.')
        namelist.append(x1[0])
    return(namelist)

imgNames = splitname(fList)

### Load the image.

from skimage.io import imread,imshow

def loadimage (imagenames,filelist):
    '''Loads images. Takes the image names and file list as input, outputs a 
    list of images.'''
    imlist=[]
    for n in range(len(imagenames)):
        imlist.append(imread(filelist[n],key=1))
    return(imlist)

imgList = loadimage(imgNames,fList)

### Show images on the list. Change index accordingly .
### Not necessary, just to visualize things.

#from skimage.io import imshow
#imshow(imgList[0])

### Make a dictionary to connect image with the respective filename.

def makedict (imagelist,imagenames):
    '''Make a dictionary with the images as values and the names as keys.'''
    imgdict = {}
    for n in range(len(imagelist)):
        imgdict.update({imagenames[n]:imagelist[n]})
    return(imgdict)

fileImage = makedict(imgList,imgNames)

#imshow(fileImage['180801_FL-1']) # just testing

### Grid slicing (make 6 boxes out of an image).
# fileImage.keys() #get all keys
# list(fileImage.keys())[0] #get the first key
# list(fileImage.values())[0] #get the first value

def gridslice (specificimage):
    '''slice one image into six flowers'''
    flo = {}
    #x = list(file_image.keys())[n]
    #flowers = file_image[x]
    flowers = fileImage[specificimage]
    flo['A-topleft'] = flowers[0:240,0:213] 
    flo['B-topmid'] = flowers[0:240,213:426] 
    flo['C-topright'] = flowers[0:240,426:640]
    flo['D-botleft'] = flowers[240:480,0:213]
    flo['E-botmid'] = flowers[240:480,213:426]
    flo['F-botright'] = flowers[240:480,426:640]
    return(flo)
    
#test = gridslice('180801_FL-1')
#imshow(test['A-topleft'])

### Use the function gridslice to loop over the dictionary.
### Yields in a dictionary containing the filenames, position of cut images (id), and the cut images.

fName={}
for n in range(len(fileImage)):
    fName['{0}'.format(list(fileImage.keys())[n])] = gridslice(list(fileImage.keys())[n])
    
###############################################################################
### Deal with csv #############################################################
###############################################################################

### Import csv data / Import txt data

import pandas as pd

####-- with .csv table----###
floLoc_df = pd.read_csv ('Dennis_GrowthRate/180801/180801.csv', sep=';',header = None)
floLoc_df.loc[0] # by row
floLoc_df[0] # by column

### Clean up the df and convert to dict

placeHolder = splitname(list(floLoc_df[0]))
floLoc_df[0] = placeHolder
floLoc = floLoc_df.set_index(0).T.to_dict('list')

#### --with .txt files---(recommended by Christian)###

#flo_180801_1 = pd.read_csv('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/180801/180801_FL-1.txt', sep="  ",header=None)
#flo1 = flodf.loc[0,0]


#--Load .txt into filelist

ftxt = glob.glob('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/180801/*.txt')
ftxt = glob.glob('Dennis_GrowthRate/180801/*.txt')
ftxt.sort()

# Get only filenames with splitname function

txtNames = splitname(ftxt)
# ftxt = splitname(ftxt) # just to avoid having too many variables

## load the txt-files

def loadtxt(txtnames,filelist):
    '''Loads txt. Takes the txt names and file list as input, outputs a 
    list of txt.'''
    txtlist=[]
    for files in glob.glob('*.txt'):
        txtlist.append(files)
    return(txtlist)

txtList=loadtxt(txtNames,ftxt)
   

# Step 3: Build up DataFrame:


#-------version 2------------

def frametxt(ftxt):
    df = []
    for file in ftxt:
        frame=pd.read_csv(file,sep="\s+",header=None) 
        df.append(frame)area
    return(df)

txt_df=frametxt(ftxt)

#------------------------
    
### Make a dictionary to connect txt with the respective filename.

def maketxtdict (txtlist,txtnames):
    '''Make a dictionary with the images as values and the names as keys.'''
    txtdict = {}
    for n in range(len(txtlist)):
        txtdict.update({txtnames[n] : txtlist[n]})
    return(txtdict)

txtdict = makedict(txt_df,txtNames)

### Grid slicing (make 6 boxes out of an txt file).
# fileImage.keys() #get all keys
# list(fileImage.keys())[0] #get the first key
# list(fileImage.values())[0] #get the first value

def gridslicetxt (specifictxt):
    '''slice one txt into six grids'''
    grid = {}
    #x = list(file_image.keys())[n]
    #flowers = file_image[x]
    flower_number = txtdict[specifictxt]
    grid['A-topleft'] = flower_number.loc[0,0] 
    grid['B-topmid'] = flower_number.loc[0,1] 
    grid['C-topright'] = flower_number.loc[0,2]
    grid['D-botleft'] = flower_number.loc[1,0]
    grid['E-botmid'] = flower_number.loc[1,1]
    grid['F-botright'] = flower_number.loc[1,2]
    return(grid)

#test=gridslicetxt('180801_FL-1')
#test['F-botright']

gridtxt={}
for n in range(len(txtdict)):
    gridtxt['{0}'.format(list(txtdict.keys())[n])] = gridslicetxt(list(txtdict.keys())[n])

###############################################################################
### Connect images and txt ####################################################
###############################################################################

### Loop over fName and rename the position key (id) of every image with values from 
### (how?)



# =============================================================================
# Version: Christian
# Using Pandas data frame to collect df_img
# =============================================================================

import pandas as pd
import numpy as np
import glob
import re
from skimage.io import imread, imshow

## Process txt-files

files_txt = glob.glob('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/180801/*.txt')
files_txt.sort()
df_txt = pd.DataFrame(columns=('fileRoot','position','plantnumber'))

dict={}
    
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
    
    dict[fileRoot,'topleft'] = txtdf.loc[0,0]
    dict[fileRoot, 'topcenter'] = txtdf.loc[0,1]
    dict[fileRoot, 'topright'] = txtdf.loc[0,2]
    dict[fileRoot, 'bottomleft'] = txtdf.loc[1,0]
    dict[fileRoot, 'bottomcenter'] = txtdf.loc[1,1]
    dict[fileRoot, 'bottomright'] = txtdf.loc[1,2]


## Process Images



files_img = glob.glob ('/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/180801/*.tif')
files_img.sort()                      
df_img = pd.DataFrame(columns=('fileRoot','position','Individual_Plant'))
for file in files_img:
    print(file)
    fileRoot=re.sub(".*/","",file[:-4])
    
    imgdf = imread(file,key=1) 
    
    df_img.loc[len(df_img)] = [fileRoot, 'topleft', imgdf[0:240,0:213]]
    df_img.loc[len(df_img)] = [fileRoot, 'topcenter', imgdf[0:240,213:426]]
    df_img.loc[len(df_img)] = [fileRoot, 'topright', imgdf[0:240,426:640]]
    df_img.loc[len(df_img)] = [fileRoot, 'bottomleft', imgdf[240:480,0:213]]
    df_img.loc[len(df_img)] = [fileRoot, 'bottomcenter', imgdf[240:480,213:426]]
    df_img.loc[len(df_img)] = [fileRoot, 'bottomright', imgdf[240:480,426:640]]
    
#df_img.sort_values(by=['fileRoot'])    

     ### Read image, segmenatation,

    
    
    

 
