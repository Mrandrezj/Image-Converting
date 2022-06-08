# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:14:28 2022

@author: musta
"""
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np
from skimage import img_as_ubyte, exposure
from skimage.filters import threshold_multiotsu
from skimage.segmentation import chan_vese
from skimage.segmentation import morphological_chan_vese
class Segment:#Segmentation class with 3 functions
    def multi_otsu(self):
        gray_img = rgb2gray(self.image)
        thresholds = threshold_multiotsu(gray_img)
        regions= np.digitize(gray_img, bins=thresholds)
        output=img_as_ubyte(exposure.rescale_intensity(regions))
        plt.imsave("output.jpg",output)
        self.showOutput()
    def chanvese(self):
        gray=rgb2gray(self.image)
        cv = chan_vese(gray,mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
               max_iter=200, dt=0.5, init_level_set="checkerboard",
               extended_output=False)
        plt.imsave("output.jpg",cv,cmap="gray")
        self.showOutput()
    def morphological(self):
        gray_img = rgb2gray(self.image)
        ls = morphological_chan_vese(gray_img, iterations=35, smoothing=3)
        #plt.contour(ls,[0.5], colors='r')
        plt.imsave("output.jpg",ls,cmap="gray")
        self.showOutput()