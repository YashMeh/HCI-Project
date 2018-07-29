#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:29:53 2018

@author: yash
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0) #number denotes the number of camera
fourcc=cv2.VideoWriter_fourcc(*'XVID') #defining codec
out=cv2.VideoWriter('output1.avi',fourcc,20.0,(640,480)) ##writing to output file
while True:
    ret,frame=cap.read() #ret takes the boolean value if you want to break the loop
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'): #on pressing q exit
        break
cap.release() #releases the camera,you cannot use the camera in use
out.release() #saving the video file
cv2.destroyAllWindows()    
    