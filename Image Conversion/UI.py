# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:06:31 2022

@author: musta
"""
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import uic
from Conversion import Conv
from Segmentation import Segment
from EdgeDetect import Edge
from FileOperations import FileOp
class UI(QMainWindow,Conv,Segment,Edge,FileOp):#Multi-inheritance
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("interface.ui",self)
        self.open_button=self.findChild(QPushButton,"open_pushButton")
        self.open_button.clicked.connect(self.openFile)
        self.actionOpen_Source.triggered.connect(self.openFile)
        
        self.clear_button=self.findChild(QPushButton,"clear_pushButton")
        self.clear_button.clicked.connect(self.clearAll)            
        self.actionSource_2.triggered.connect(self.clearSource)
        self.actionOutput_2.triggered.connect(self.clearOutput)

        self.Exit_button=self.findChild(QPushButton,"Exit_pushButton")
        self.Exit_button.clicked.connect(self.exitFile)     
        self.actionExit.triggered.connect(self.exitFile) 
        
        self.save_button=self.findChild(QPushButton,"save_pushButton")
        self.save_button.clicked.connect(self.saveFile) 
        self.actionSave_Output.triggered.connect(self.saveFile)
        
        self.save_as_button=self.findChild(QPushButton,"save_as_pushButton")
        self.save_as_button.clicked.connect(self.save_asFile) 
        self.actionSave_as_Output.triggered.connect(self.save_asFile)
        
        self.undo_button=self.findChild(QPushButton,"undo_pushButton")
        self.undo_button.clicked.connect(self.undoFile) 
        self.actionUndo_Output.triggered.connect(self.undoFile)
        self.actionOutput_2.setEnabled(False)
        self.actionSource_2.setEnabled(False)
        self.redo_button=self.findChild(QPushButton,"redo_pushButton")
        self.redo_button.clicked.connect(self.redoFile) 
        self.actionRedo_Output.triggered.connect(self.redoFile)
        
        self.export_button=self.findChild(QPushButton,"export_as_pushButton")
        self.export_button.clicked.connect(self.exportFile_out) 
        self.actionOutput.triggered.connect(self.exportFile_out)
        self.actionSource.triggered.connect(self.exportFile_in)
        
        self.label=self.findChild(QLabel,"label")  
        self.label2=self.findChild(QLabel,"label_2")
        
        self.rgb2hsv_button=self.findChild(QPushButton,"RGB_HSV_pushButton")
        self.rgb2hsv_button.clicked.connect(self.rgbtohsv)
        self.actionRGB_to_HSV.triggered.connect(self.rgbtohsv)
        
        self.rgb2gray_button=self.findChild(QPushButton,"RGB_GRAY_pushButton")
        self.rgb2gray_button.clicked.connect(self.rgbtogray)
        self.actionRGB_to_GrayScale.triggered.connect(self.rgbtogray)
                
        self.Multi_otsu_pushButton=self.findChild(QPushButton,"Multi_otsu_pushButton")
        self.Multi_otsu_pushButton.clicked.connect(self.multi_otsu)
        self.actionMulti.triggered.connect(self.multi_otsu)
        
        self.Chan_vese_pushButton=self.findChild(QPushButton,"Chan_vese_pushButton")
        self.Chan_vese_pushButton.clicked.connect(self.chanvese)
        self.actionChan_Vese_Segmentation.triggered.connect(self.chanvese)
        
        self.Morpho_pushButton=self.findChild(QPushButton,"Morpho_pushButton")
        self.Morpho_pushButton.clicked.connect(self.morphological)
        self.actionMorphological_Snake.triggered.connect(self.morphological)
        
        self.Roberts_pushButton=self.findChild(QPushButton,"Roberts_pushButton")
        self.Roberts_pushButton.clicked.connect(self.roberts)
        self.actionRoberts.triggered.connect(self.roberts)
        
        self.Sobel_pushButton=self.findChild(QPushButton,"Sobel_pushButton")
        self.Sobel_pushButton.clicked.connect(self.sobel)
        self.actionSobel.triggered.connect(self.sobel)
        
        self.Scharr_pushButton=self.findChild(QPushButton,"Scharr_pushButton")
        self.Scharr_pushButton.clicked.connect(self.scharr)
        self.actionScharr.triggered.connect(self.scharr)
        
        self.Prewitt_pushButton=self.findChild(QPushButton,"Prewitt_pushButton")
        self.Prewitt_pushButton.clicked.connect(self.prewitt)
        self.actionPrewit.triggered.connect(self.prewitt)
        
        self.show()