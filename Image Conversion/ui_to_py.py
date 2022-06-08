# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:18:05 2022

@author: musta
"""

from PyQt5 import uic

with open('interfaceUI.py','w',encoding="utf-8") as fout:
          uic.compileUi('interface.ui', fout)