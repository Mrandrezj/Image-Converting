# Image-Converting
An interface which makes image convertion
from PyQt5 import uic

with open('interfaceUI.py','w',encoding="utf-8") as fout:
          uic.compileUi('interface.ui', fout)
