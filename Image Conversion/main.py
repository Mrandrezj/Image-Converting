# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:13:21 2022

@author: musta
"""

from PyQt5.QtWidgets import QApplication
import sys
from UI import UI
#Driver code
if __name__=='__main__':
    app=QApplication(sys.argv)
    UIWindow=UI()
    app.exec_()