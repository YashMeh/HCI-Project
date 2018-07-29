#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 11:56:35 2018

@author: yash
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('tejas.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR=1  'image-name' then 0
#IMREAD_UNCHANGED=-1
#IMREAD_GRAYSCALE=0
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Saving the image
#cv2.imwrite('tejas_gray.jpg',img)























