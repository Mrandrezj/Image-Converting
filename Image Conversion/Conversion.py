# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:38:54 2022

@author: musta
"""

import matplotlib.pyplot as plt
from skimage.color import rgb2hsv, rgb2gray
class Conv: #Conversion class with 2 functions
    def rgbtohsv(self):
        rgb_img = rgb2hsv(self.image)
        plt.imsave("output.jpg",rgb_img,cmap="gray")
        self.showOutput()
    def rgbtogray(self):
        gray_img = rgb2gray(self.image)
        plt.imsave("output.jpg",gray_img,cmap="gray")
        self.showOutput()