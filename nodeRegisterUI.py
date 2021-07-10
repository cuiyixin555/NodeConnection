# Welcome Page to choose variety of DataSets
# Motion_Blur Dataset for Deblur Processing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget,QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton

class UI_nodeRegister(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 220)

        # 全局布局：水平
        self.wlayout=QHBoxLayout(Form)

        # 局部布局：垂直，表单
        self.vlayout=QVBoxLayout()
        self.formlayout=QFormLayout()

        # left: setup login.png
        self.label=QtWidgets.QLabel()
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 0, 0);\n"
                                 "     border-width: 0px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/register_icon.png")))

        # 为左边布局添加控件
        self.vlayout.addWidget(self.label)
        self.vwg = QWidget()
        self.vwg.setLayout(self.vlayout)
        self.wlayout.addWidget(self.vwg)

        # right: setup input text
        self.label_1=QtWidgets.QLabel()
        self.label_1.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 0, 0);\n"
                                 "     border-width: 0px;\n"
                                 "     border-style: solid;\n"
                                 "}")

        self.label_1.setPixmap((QtGui.QPixmap("./asserts/image/register_title.png")))

        self.pDestIP = QLineEdit()
        self.pUserName = QLineEdit()

        self.pDestIP.setPlaceholderText("Dest IP")
        self.pUserName.setPlaceholderText("User Name")
        self.pDestIP.setStyleSheet(
            '''QLineEdit{background:#000000;color:#FFFFFF}'''
        )
        self.pUserName.setStyleSheet(
            '''QLineEdit{background:#000000;color:#FFFFFF}'''
        )

        # 设置演示效果
        self.pDestIP.setEchoMode(QLineEdit.Normal)
        self.pUserName.setEchoMode(QLineEdit.Normal)
        self.pDestIP.setFixedSize(400, 32)
        self.pUserName.setFixedSize(400, 32)

        self.pushButton = QPushButton(Form)

        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedSize(400, 35)

        self.pushButton.setStyleSheet(
            '''QPushButton{background:#000000;border-radius:5px;color:#FFF0F5}QPushButton:hover{background:#808080;}''')
        self.pushButton.setFont(QtGui.QFont('HGDY_CNKI', 10))

        self.label.setText("")
        self.label.setObjectName("label")
        self.label_1.setText("")
        self.label.setObjectName("label_1")

        self.formlayout.addWidget(self.label_1)
        self.formlayout.addWidget(self.pDestIP)
        self.formlayout.addWidget(self.pUserName)
        self.formlayout.addWidget(self.pushButton)
        self.fwg = QWidget()
        self.fwg.setLayout(self.formlayout)
        self.wlayout.addWidget(self.fwg)
        self.setLayout(self.wlayout)

        self.pushButton.clicked.connect(Form.RW_File)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QIcon("./asserts/image/register_icon.png"))
        Form.setWindowTitle(_translate("Form", "Slave Node Register"))
        self.pushButton.setText(_translate("Form", "Register"))