# -*- coding: utf-8 -*-
# corresponding to welcome.py
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from welcomeUI import UI_Welcome
from open_nodeRegisterUI import open_nodeRegister
from open_runningDemoUI import open_runningDemo
import socket
import json

class open_index(QtWidgets.QWidget, UI_Welcome): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_index, self).__init__(parent)
        self.setupUi(self) # import Ui_Form

        # 实例化子窗体
        self.open_nodeRegister = open_nodeRegister()
        self.open_runningDemo = open_runningDemo()

    # # signal channel for connection
    def open_nodeRegister_page(self):
        self.open_nodeRegister.show()

    def open_runningDemo_page(self):
        self.open_runningDemo.show()

app = QtWidgets.QApplication(sys.argv)
window = open_index()
window.show()
app.exec_()