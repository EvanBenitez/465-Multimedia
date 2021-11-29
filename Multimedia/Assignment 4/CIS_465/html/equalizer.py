# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:27:15 2021

@author: Evan Benitez
"""

import cv2
import numpy
import gray
import histogram

# for one 8 bit color channel
def intensity_map(image):
    pixel_count = len(image) * len(image[0])
    histo = histogram.histo(image)
    intensity_map = {}
    sum = 0
    for intensity in range(256):
        if histo.get(intensity) != None:
            sum += (histo[intensity] / pixel_count)
        intensity_map[intensity] = round(sum * 255)
    return intensity_map
        
def equalize(image):
    pixel_map = intensity_map(image)
    
    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j] = pixel_map[image[i][j]]
    return image

def equalize_color(image):
     red, green, blue = cv2.split(image)
     red_map = intensity_map(red)
     green_map = intensity_map(green)
     blue_map = intensity_map(blue)
    
     for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j][0] = red_map[image[i][j][0]]
            image[i][j][1] = green_map[image[i][j][1]]
            image[i][j][2] = blue_map[image[i][j][2]]
     return image
        
if __name__ == "__main__":

    #equalize image-1 photo
    original = cv2.imread("images/image.bmp")
    bw = gray.avg_gray(original)
    cv2.imshow("Gray Origianl", bw)
    equalized_gray = equalize(bw)
    cv2.imshow("Equalized Gray", equalized_gray)
    histogram.plot_gray(equalized_gray)
    
    cv2.imshow("original Original", original)
    equalized_color = equalize_color(original)
    cv2.imshow("Altered Original", equalized_color)
    
    #equalizing cat photo
    cat = cv2.imread("images/cat.jpg")
    gray_cat = gray.avg_gray(cat)
    cv2.imshow("Gray Cat", gray_cat)
    egray_cat = equalize(gray_cat)
    cv2.imshow("Equalized Gray Cat", egray_cat)
    
    cv2.imshow("Cat", cat)
    ecat = equalize_color(cat)
    cv2.imshow("Equalized Cat", ecat)
    
    #dark image
    dark = cv2.imread("images/dark.jpg")
    cv2.imshow("Dark", dark)
    edark = equalize_color(dark)
    cv2.imshow("Equalized dark", edark)
    
    #bright image
    bright = cv2.imread("images/bright.jpg")
    cv2.imshow("Bright", bright)
    ebright = equalize_color(bright)
    cv2.imshow("Equalized bright", ebright)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()