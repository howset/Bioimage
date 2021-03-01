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

from skimage.io import imread,imshow,imsave
import tifffile
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.morphology import remove_small_objects,label


# =============================================================================
# Try with tifffile
# https://openbase.com/python/tifffile/documentation
# =============================================================================


# use key=2 or key =5 for our data


img1=imread("/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/180801",key=1) 
imshow(img1)

#open corresponding txt file
img1txt=open("/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/bioimage/Dennis_GrowthRate/180801/180801_FL-1.txt", 'r')
content = img1txt.read()
print (content)


img2=imread("/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/Dennis_GrowthRate/180802/180802_6.tif",key=2)
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

np.sum(l==1)
sizes = []
for i in range(1,nb+1):
    sizes.append(np.sum(l==i))

sizes_i = sizes



img5=imread("/home/dennis/Schreibtisch/Uni_Potsdam/Bioimage/practical/Dennis_GrowthRate/180801/180801_FL-1.tif",key=5) 
imshow(img5)


# =============================================================================
# grid separation: 
# tkinter: https://www.pythontutorial.net/tkinter/tkinter-grid/
# matplotlib.pyplot.grid: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
# =============================================================================




# =============================================================================
# calculate the size of a plant 
# example calculation of plant 1 in Image 1 (maybe)
# =============================================================================

# homogenous illumination of an imaged area: 10x13 cm
# Dimemsnsion of the image
img1.shape[1] 
#-> X axis: 640px = 13cm

img1.shape[0]
#-> Y axis: 480px = 10 cm

img1.shape
# 480 px * 640px = 307200 px²
# 10cm *13 cm = 130 cm² 
# --> 130cm² = 307200 px²

# Calculate size of plant 1
np.sum(l==1) # 288 pixel of plant 1
size of plant 1 = (130*288)/307200 = 0,12 cm² = 12 mm² 

#==============================================================================







#==============================================================================
# Ideas
# =============================================================================
#plant1

#for x in 1:len(list)


#for i in 1:2
#    var = sprintf(img+i)    
#    gray = rgb2gray(var)
#    bw = gray > threshold_otsu(gray)
#    l = label(bw)
#    np.unique(l)
#    nb=len(np.unique(l))-1
#    p.sum(l==0)
#    sizes = []
#    for i in range(1,nb+1):
#        sizes.append(np.sum(l==i))
   
#sizes_i = sizes
