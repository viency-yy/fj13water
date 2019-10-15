# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpjm1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class DQZJ(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(828, 588)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1, -6, 831, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"C:\Users\Your Dad\Desktop/python/fjsss/出牌界面s.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 520, 541, 51))
        self.label_2.setStyleSheet("font: 9pt \"Adobe 黑体 Std R\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.cpan = QtWidgets.QPushButton(Form)
        self.cpan.setGeometry(QtCore.QRect(700, 520, 71, 51))
        self.cpan.setObjectName("cpan")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cpan.setText(_translate("Form", "出牌"))
#import dqzj_rc
