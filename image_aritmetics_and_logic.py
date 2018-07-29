#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 22:31:35 2018

@author: yash
"""

import numpy as np
import cv2

img1=cv2.imread('img1.png',cv2.IMREAD_COLOR)
img2=cv2.imread('logo.png',cv2.IMREAD_COLOR)

#Adding images
add=img1+img2
#This method-like addition adds the two pixels therefore the pic becomes 
#lighter
add=cv2.add(img1,img2)
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Weighted addition of images
#Blending images
weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow('add',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
I want to put OpenCV logo above an image. If I add two images, it will 
change color. If I blend it, I get an transparent effect.
 But I want it to be opaque. If it was a rectangular region,
 I could use ROI as we did in last chapter. But OpenCV logo is
 a not a rectangular shape. So you can do it with bitwise
 operations as below:
    '''
import numpy as np
import cv2

img1=cv2.imread('img1.png',cv2.IMREAD_COLOR)
img2=cv2.imread('logo.png',cv2.IMREAD_COLOR)
rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('mask',mask)
cv2.imshow('notmask',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()  
    