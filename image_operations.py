#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 19:25:56 2018

@author: yash
"""

import numpy as np
import cv2

#Usually people perform analysis on grayscale image 
#then export the result on coloured image
img=cv2.imread('tejas.jpg',cv2.IMREAD_COLOR)

###Referencing a particular pixel
px=img[55,55]
print(px)
###Changing the value of pixel
img[55,55]=[255,255,255]
px=img[55,55]
print(px)

##ROI=region of image
roi=img[100:150,100:150]
print(roi)
##Changing the region
img[100:150,100:150]=[255,255,255]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##Copying a region and pasting it
face=img[37:111,107:194]
img[0:74,0:87]=face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
