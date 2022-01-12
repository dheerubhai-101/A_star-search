# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:01:21 2022

@author: dheeraj
"""

import cv2 as cv
#import numpy as np

# changing colour of pixels in the path

def plot(image,path):
    for i in path:
        y,x = i
        image[y,x,0]=0
        image[y,x,1]=255
        image[y,x,2]=0
        
    cv.imshow('map',image)
    cv.waitKey(0)
    cv.destroyAllWindows()