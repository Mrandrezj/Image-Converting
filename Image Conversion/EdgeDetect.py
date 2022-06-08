# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:18:39 2022

@author: musta
"""
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import roberts, sobel, scharr, prewitt
class Edge:#Edge Detection with 4 functions
    def roberts(self):
        gray_img = rgb2gray(self.image)
        edge_roberts = roberts(gray_img)
        plt.imsave("output.jpg",edge_roberts,cmap="gray")
        self.showOutput()
    def sobel(self):
        gray_img = rgb2gray(self.image)
        edge_sobel = sobel(gray_img)
        plt.imsave("output.jpg",edge_sobel,cmap="gray")
        self.showOutput()
    def scharr(self):
        gray_img = rgb2gray(self.image)
        edge_scharr = scharr(gray_img)
        plt.imsave("output.jpg",edge_scharr,cmap="gray")
        self.showOutput()
    def prewitt(self):
        gray_img = rgb2gray(self.image)
        edge_prewitt = prewitt(gray_img)
        plt.imsave("output.jpg",edge_prewitt,cmap="gray")
        self.showOutput()