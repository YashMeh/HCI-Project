#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:50:07 2018

@author: yash
"""

import numpy as np 
import cv2

img=cv2.imread('tejas.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(25,25,25),15)#The more negative the darker cv uses bgr

cv2.rectangle(img,(150,150),(300,300),(0,255,0),5)

cv2.circle(img,(300,300),25,(0,0,255),-1)

#Drawing the polygon
pts=np.array([[10,20],[30,40],[60,700],[80,90]],np.int32)
cv2.polylines(img,[pts],True,(255,255,0),3)

#Writing on image
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Tejas',(0,130),font,5,(0,255,255),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()