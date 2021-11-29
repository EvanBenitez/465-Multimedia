# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 22:53:57 2021

@author: Evan Benitez
"""

import cv2
import copy
import math

def binary(image, thresh):
    img = copy.deepcopy(image)
    
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] < thresh:
                img[i][j] = 0
            else:
                img[i][j] = 255
    cv2.imshow("binary Image " + str(thresh), img)
    
def trinary(image):
    img = copy.deepcopy(image)
    
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] < 70:
                img[i][j] = 0
            elif img[i][j] > 170:
                img[i][j] = 255
    cv2.imshow("trinary Image", img)
    
def log(image):
    img = copy.deepcopy(image)
    C = 255 / math.log(1 + 255)
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j] = C * math.log(1 + img[i][j])
    cv2.imshow("Logarithmic Image", img)
    
def gamma(image, G):
    img = copy.deepcopy(image)
    C = 255 / math.pow(255, G)
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j] = C * math.pow(img[i][j], G)
    cv2.imshow("Gamma Image " + str(G), img)


original = cv2.imread("images/cat.jpg", 0)
cv2.imshow("original", original)

binary(original, 70)
binary(original, 170)

trinary(original)

log(original)

gamma(original, 5) # high gamma
gamma(original, 1) # neutral gamma
gamma(original, 0.2) # low gamma

cv2.waitKey(0)

cv2.destroyAllWindows()