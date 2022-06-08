# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:20:56 2022

@author: musta
"""
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from skimage import io
undo_stack=[]#undo stack
redo_stack=[]#redo stack used circular stack
class FileOp:#File operation class
    def openFile(self):
        self.fname=QFileDialog.getOpenFileName(self,"Open File","c:\\gui\\images","All Files(*);;PNG Files (*.png);;JPG Files(*.jpg)")
        pixmap=QPixmap(self.fname[0])
        self.image=io.imread(self.fname[0])
        pixmap_resized=pixmap.scaled(512,512,QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap_resized)
        self.save_button.setEnabled(True)
        self.actionSave_Output.setEnabled(True)
        self.actionOutput_2.setEnabled(True)
        self.actionSource_2.setEnabled(True)
        self.actionSave_as_Output.setEnabled(True)
        self.actionUndo_Output.setEnabled(True)
        self.actionRedo_Output.setEnabled(True)
        self.export_button.setEnabled(True)
        self.save_as_button.setEnabled(True)
        self.undo_button.setEnabled(True)
        self.redo_button.setEnabled(True)
        self.menuExport_as.setEnabled(True)
        self.rgb2hsv_button.setEnabled(True)
        self.actionRGB_to_GrayScale.setEnabled(True)
        self.clear_button.setEnabled(True)
        self.actionRGB_to_HSV.setEnabled(True)
        self.rgb2gray_button.setEnabled(True)
        self.Multi_otsu_pushButton.setEnabled(True)
        self.actionMulti.setEnabled(True)
        self.Chan_vese_pushButton.setEnabled(True)
        self.actionChan_Vese_Segmentation.setEnabled(True)
        self.Morpho_pushButton.setEnabled(True)
        self.actionMorphological_Snake.setEnabled(True)
        self.Roberts_pushButton.setEnabled(True)
        self.actionRoberts.setEnabled(True)
        self.Sobel_pushButton.setEnabled(True)
        self.Scharr_pushButton.setEnabled(True)
        self.actionScharr.setEnabled(True)
        self.Prewitt_pushButton.setEnabled(True)
        self.actionPrewit.setEnabled(True)
        self.actionSobel.setEnabled(True)
        self.actionSobel.setEnabled(True)
    def clearAll(self):
        self.label.clear()
        self.label2.clear()
        self.image=None
        if self.image==None:
            self.disable()
    def clearSource(self):
        self.label.clear()
        self.image=None
        if self.image==None:
            self.disable()
    def clearOutput(self):
        self.label2.clear()
    def exitFile(self):
        self.close()
    def saveFile(self):
        Fname,_ =QFileDialog.getSaveFileName(self,"Save File","c:\\gui\\images","JPG Files(*.jpg)")
        image=io.imread("output.jpg")
        io.imsave(Fname,image)
    def save_asFile(self):
        Fname,_ =QFileDialog.getSaveFileName(self,"Save File","c:\\gui\\images","All Files(*);;PNG Files (*.png);;JPG Files(*.jpg)")
        image=io.imread("output.jpg")
        plt.show(image)
        plt.savefig(Fname+".pdf",image)
    def undoFile(self):
        redo_stack.append(undo_stack.pop())
        pixmap_resized=undo_stack[-1].scaled(512,512,QtCore.Qt.KeepAspectRatio)
        self.label2.setPixmap(pixmap_resized)
    def redoFile(self):
        pixmap_resized=redo_stack[-1].scaled(512,512,QtCore.Qt.KeepAspectRatio)
        self.label2.setPixmap(pixmap_resized)
        redo_stack.pop()
    def exportFile_out(self):
        Fname,_ =QFileDialog.getSaveFileName(self,"Save File","c:\\gui\\images","All Files(*);;PNG Files (*.png);;JPG Files(*.jpg);;PDF Files(*.pdf)")
        image=io.imread("output.jpg")
        plt.imshow(image)
        plt.savefig(Fname+'.pdf')
    def exportFile_in(self):
        Fname,_ =QFileDialog.getSaveFileName(self,"Save File","c:\\gui\\images","All Files(*);;PNG Files (*.png);;JPG Files(*.jpg);;PDF Files(*.pdf)")
        plt.imshow(self.image)
        plt.savefig(Fname+'.pdf')
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.saveFile()
            event.accept()
        else:
            event.ignore()
    def showOutput(self):
        self.pixmap=QPixmap("output.jpg")
        undo_stack.append(self.pixmap)
        self.image2=self.pixmap
        pixmap_resized=self.pixmap.scaled(512,512,QtCore.Qt.KeepAspectRatio)
        self.label2.setPixmap(pixmap_resized) 
    def disable(self):
        self.save_button.setEnabled(False)
        self.actionSave_Output.setEnabled(False)
        self.actionOutput_2.setEnabled(False)
        self.actionSource_2.setEnabled(False)
        self.actionSave_as_Output.setEnabled(False)
        self.actionUndo_Output.setEnabled(False)
        self.actionRedo_Output.setEnabled(False)
        self.export_button.setEnabled(False)
        self.save_as_button.setEnabled(False)
        self.undo_button.setEnabled(False)
        self.redo_button.setEnabled(False)
        self.menuExport_as.setEnabled(False)
        self.rgb2hsv_button.setEnabled(False)
        self.actionRGB_to_GrayScale.setEnabled(False)
        self.clear_button.setEnabled(False)
        self.actionRGB_to_HSV.setEnabled(False)
        self.rgb2gray_button.setEnabled(False)
        self.Multi_otsu_pushButton.setEnabled(False)
        self.actionMulti.setEnabled(False)
        self.Chan_vese_pushButton.setEnabled(False)
        self.actionChan_Vese_Segmentation.setEnabled(False)
        self.Morpho_pushButton.setEnabled(False)
        self.actionMorphological_Snake.setEnabled(False)
        self.Roberts_pushButton.setEnabled(False)
        self.actionRoberts.setEnabled(False)
        self.Sobel_pushButton.setEnabled(False)
        self.Scharr_pushButton.setEnabled(False)
        self.actionScharr.setEnabled(False)
        self.Prewitt_pushButton.setEnabled(False)
        self.actionPrewit.setEnabled(False)
        self.actionSobel.setEnabled(False)
        self.actionSobel.setEnabled(False)