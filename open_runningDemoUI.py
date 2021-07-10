# -*- coding: utf-8 -*-
# corresponding to welcome.py
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from runningDemoUI import UI_runningDemo
import socket
import json

class open_runningDemo(QtWidgets.QWidget, UI_runningDemo): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_runningDemo, self).__init__(parent)
        self.setupUi(self) # import Ui_Form

    # singal slot function
    def RW_File(self):
        print("aaa")
        pass