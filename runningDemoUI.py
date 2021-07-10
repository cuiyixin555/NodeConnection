from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class UI_runningDemo(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 330)

        # setup welcome.png
        self.label=QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(23, 10, 820, 70))
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 0, 0);\n"
                                 "     border-width: 0px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/demo_title.png")))
        # self.label.setScaledContents(True)

        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(23, 100, 820, 200))
        self.table.setColumnCount(4)  # 设置列数
        self.table.setRowCount(6)  # 设置行数
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setStyleSheet(
            '''QTableWidget{background:#A9A9A9;color:#FFFFFF}'''
        )

        column_name = [
            'IP',
            'Name',
            'Domain',
            'Waiting Node List',
        ]
        self.table.setHorizontalHeaderLabels(column_name)  # 设置列名称

        self.retranslateUi(Form)

        # 将控件加载到Form中
        QtCore.QMetaObject.connectSlotsByName(Form)

    def update_item_data(self, data):
        """更新内容"""
        self.setItem(0, 0, QTableWidgetItem(data))  # 设置表格内容(行， 列) 文字


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QIcon("./asserts/image/register_icon.png"))
        Form.setWindowTitle(_translate("Form", "Master-Slave Running Demo"))