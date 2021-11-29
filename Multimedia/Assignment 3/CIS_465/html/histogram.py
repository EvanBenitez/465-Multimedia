# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:06:08 2021

@author: Evan Benitez
"""
import cv2
import numpy
import gray
import matplotlib.pyplot as plt


def histo(image):
    gram = {}
    
    for row in image:
        for col in row:
             key = col
             gram[key] = gram.get(key, 0) + 1
    return gram

def histo_thee_channel(image):
    red, green, blue = cv2.split(image)
    return histo(red), histo(green), histo(blue)

def plot_color(red, green, blue):
    plt.hist(red.flatten(), bins = [i for i in range(256)], color = 'red')
    plt.hist(green.flatten(), bins = [i for i in range(256)], color = 'green')
    plt.hist(blue.flatten(), bins = [i for i in range(256)], color = 'blue')
    plt.xlabel('Intensity')
    plt.ylabel('Count')
    plt.title('Intensity histogram')
    plt.show()
             
def plot_gray(gray_scale):
    plt.hist(gray_scale.flatten(), bins = [i for i in range(256)], color = 'gray')
    plt.xlabel('Intensity')
    plt.ylabel('Count')
    plt.title('Intensity histogram')
    plt.show()


if __name__ == "__main__":
    original = cv2.imread("images/image.bmp")
    red, blue, green = cv2.split(original)
    hist_red, hist_green, hist_blue = histo_thee_channel(original)
    
    gray = gray.avg_gray(original)
    hist_gray = histo(gray)
    
    print('Red channel')
    print(sorted(hist_red.items()))
    print('Green channel')
    print(sorted(hist_green.items()))
    print('Blue channel')
    print(sorted(hist_blue.items()))
    print('Gray scale')
    print(sorted(hist_gray.items()))
    
    plot_gray(gray)
    plot_color(red, green, blue)


    
   

    
    