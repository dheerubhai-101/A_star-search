# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:19:17 2022

@author: dheeraj
"""

import cv2 as cv
from a_star import a_star_search
import plot_path
from mapping import map_threshold

#read image
image = cv.imread('map.pgm')
img= map_threshold(image)

origin= (370,370)
destination= (639,269)

path= a_star_search(origin,destination,img)


plot_path.plot(image,path)