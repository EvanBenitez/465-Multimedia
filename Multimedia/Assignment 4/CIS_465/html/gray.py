# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:40:55 2021

@author: Evan Benitez
"""

import cv2
import numpy

def avg_gray(image):
    gray = numpy.zeros((len(image),len(image[0])))
    
    for i in range(len(image)):
        for j in range(len(image[i])):
            gray[i][j] = image[i][j][0] // 3 + image[i][j][1] // 3 + image[i][j][2] // 3
    return gray.astype(numpy.uint8)
                           
if __name__ == "__main__":
    original = cv2.imread("images/image.bmp")
    cv2.imshow("original", original)
    
    gray = avg_gray(original)
    cv2.imshow("gray", gray)
    
    print(gray)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()