# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:19:49 2021

@author: Crow
"""

import cv2
import numpy
import time

# color parameters
red_param = (0,250)
green_param = (0,155)
blue_param = (0,255)

# returns if pixel is within the parameters
def check_params(pixel):
    if red_param[0] < pixel[0] <= red_param[1]:
        if green_param[0] < pixel[1] <= green_param[1]:
            if blue_param[0] < pixel[2] <= blue_param[1]:
                return True
    return False

def grey(pixel):
    return pixel[0] // 3 + pixel[1] // 3 + pixel[2] // 3


img = cv2.imread("Pic.jpg")

cv2.imshow("original", img)

print(time.localtime())
# for i in range(len(img)):
#     for j in range(len(img[i])):
#         if not check_params(img[i][j]):
#            img[i][j] = grey(img[i][j])
            
# cv2.imshow("altered", img)

#print( [2,0,4] < [2,1,3] )
cv2.waitKey(0)
cv2.destroyAllWindows()