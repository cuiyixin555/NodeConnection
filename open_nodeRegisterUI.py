# -*- coding: utf-8 -*-
# corresponding to welcome.py
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from nodeRegisterUI import UI_nodeRegister
import socket
import json

class open_nodeRegister(QtWidgets.QWidget, UI_nodeRegister): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_nodeRegister, self).__init__(parent)
        self.setupUi(self) # import Ui_Form

    # singal slot function
    def RW_File(self):
        # client message
        ip = self.pDestIP.text().strip()
        username = self.pUserName.text().strip()
        dataString = ip + '@' + username + '\n'
        # print('dataString', dataString)

        with open("./configuration/config.txt", 'a+') as f:
            f.write(dataString)
            f.close()

        # link server
        ADDRESS = ('127.0.0.1', 8888)
        client = socket.socket()
        client.connect(ADDRESS)

        # receive server message for welcome
        fromServerMsg = client.recv(1024).decode(encoding='utf8') # connect server successfully
        if fromServerMsg != None:
            client.sendall(dataString.encode('utf-8'))

        # jsonstr = json.dumps(jd)
        # print('send: ' + jsonstr)
        # client.sendall(jsonstr.encode('utf8'))
        # client ip message and data message

# app = QtWidgets.QApplication(sys.argv)
# window = open_nodeRegister()
# window.show()
# app.exec_()