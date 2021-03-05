#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:17:11 2021

@author: howsetya
"""

### Set work directory. Change directory accordingly

import os
os.chdir('/home/howsetya/workspace/Bioimage/')

### Load image into filelist. Change directory accordingly

import glob
flist = glob.glob('Dennis_GrowthRate/180801/*.tif')
flist.sort() # sort the list

### Get only filename 

def splitname (filelist):
    '''Splits path and filename. Takes a list as input, outputs only the image
    names without the path.'''
    namelist=[]
    for n in range(len(filelist)):
        x1 = filelist[n]
        x2 = x1.split('/')
        namelist.append(x2[2])
    return(namelist)

imgnames = splitname(flist)

### Load the image

from skimage.io import imread

def loadimage (imagenames,filelist):
    '''Loads images. Takes the image names and file list as input, outputs a 
    list of images.'''
    imlist=[]
    for n in range(len(imagenames)):
        imlist.append(imread(filelist[n],key=1))
    return(imlist)

imglist = loadimage(imgnames,flist)

### Show images on the list. Change index accordingly 
### Not necessary, just to visualize things

#from skimage.io import imshow
#imshow(imglist[0])

### Make a dictionary to connect image with the respective filename

def makedict (imagelist,imagenames):
    '''Make a dictionary with the images as values and the names as keys.'''
    imgdict = {}
    for n in range(len(imagelist)):
        imgdict.update({imagenames[n]:imagelist[n]})
    return(imgdict)

file_image = makedict(imglist,imgnames)

### Grid slicing (make 6 boxes out of an image)
# file_image.keys() #get all keys
# list(file_image.keys())[0] #get the first key
# list(file_image.values())[0] #get the first value

def gridslice (imagedict):
    flo = []
    for n in range(len(imagedict)):
        x = list(file_image.keys())[n]
        flowers = file_image[x]
        flo[1] = flowers[0:240,0:213]
        flo[2] = flowers[0:240,213:426]
        flo[3] = flowers[0:240,426:640]
        flo[4] = flowers[240:480,0:213]
        flo[5] = flowers[240:480,213:426]
        flo[6] = flowers[240:480,426:640]
        
        
        
        
        