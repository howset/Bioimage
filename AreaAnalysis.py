# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================
# important notes
# =============================================================================
# Height of growing pots: 6 cm
#fixed working distance 18.5 cm
# homogenous illumination of an imaged area: 10x13 cm
# The CCD Camera IMAG-K6 (Allied Vision Technologies) features a 2/3" chip with 1392 x 1040 pixel. The data are digitized
# within the camera and transferred via ethernet interface

#ImagingWin image: 640x480 pixel

#The CCD Camera IMAG-K7 (Allied Vision Technologies) can be used, which features a 1/2" chip with 640 x 480 pixel resolution. 
#The data are digitized within the camera and transferred via Ethernet interface (GigE-Vision ® ) to the PC.

from skimage.io import imread,imshow,imsave,imshape
import tifffile
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.morphology import remove_small_objects,label


# =============================================================================
# Try with tifffile
# https://openbase.com/python/tifffile/documentation
# =============================================================================


# use key=2 or key =5 for our data


img1=imread("/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/Dennis_GrowthRate/180801/180801_FL-1.tif",key=2) 
imshow(img1)

img2=imread("/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/Dennis_GrowthRate/180802/180802_6.tif",key=1)
imshow(img2)

plant1=[img1,img2]
plant2[img1,img2]

gray = rgb2gray(img1)
imshow(gray)
bw = gray > threshold_otsu(gray)
imshow(bw)

    
from skimage.morphology import label
l=label(bw)

import numpy as np
np.unique(l)
nb=len(np.unique(l))-1

np.sum(l==0)
sizes = []
for i in range(1,nb+1):
    sizes.append(np.sum(l==i))

sizes_1 = sizes



img5=imread("/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/Dennis_GrowthRate/180801/180801_FL-1.tif",key=5) 
imshow(img5)


# =============================================================================
# grid separation: with tkinter
# https://www.pythontutorial.net/tkinter/tkinter-grid/
# =============================================================================















# =============================================================================
# Ideas
# =============================================================================
#plant1
for x in 1:len(list)
        






for i in 1:2
    var = sprintf(img+i)    
    gray = rgb2gray(var)
    bw = gray > threshold_otsu(gray)
    l = label(bw)
    np.unique(l)
    nb=len(np.unique(l))-1
    p.sum(l==0)
    sizes = []
    for i in range(1,nb+1):
        sizes.append(np.sum(l==i))

    
sizes_i = sizes
