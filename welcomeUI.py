from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon

class UI_Welcome(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 520)

        # setup welcome.png
        self.label=QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(23, 10, 570, 380))
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 0, 0);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/welcome.png")))

        # setup pushButton for choose variety of datasets
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton_1 = QtWidgets.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(23, 410, 570, 40))
        self.pushButton_1.setGeometry(QtCore.QRect(23, 460, 570, 40))

        self.pushButton.setObjectName("pushButton")
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton.setStyleSheet(
            '''QPushButton{background:#000000;border-radius:5px;color:#FFF0F5}QPushButton:hover{background:#808080;}''')
        self.pushButton_1.setStyleSheet(
            '''QPushButton{background:#000000;border-radius:5px;COLOR:#FFF0F5}QPushButton:hover{background:#808080;}''')
        self.pushButton.setFont(QtGui.QFont('HGDY_CNKI', 10))
        self.pushButton_1.setFont(QtGui.QFont('HGDY_CNKI', 10))

        self.label.setText("")
        self.label.setObjectName("label")
        self.retranslateUi(Form)

        self.pushButton.clicked.connect(Form.open_nodeRegister_page)
        self.pushButton_1.clicked.connect(Form.open_runningDemo_page)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Master-Slave Connection"))
        Form.setWindowIcon(QIcon("./asserts/image/register_icon.png"))
        self.pushButton.setText(_translate("Form", "Slave Node Register"))
        self.pushButton_1.setText(_translate("Form", "Master-Slave Running Demo"))