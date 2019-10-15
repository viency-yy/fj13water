# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ksjm1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class KSJM(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(817, 592)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"C:\Users\Your Dad\Desktop/python/fjsss/开始界面s.jpg"))
        self.label.setObjectName("label")
        self.phb = QtWidgets.QPushButton(Form)
        self.phb.setGeometry(QtCore.QRect(470, 190, 181, 121))
        self.phb.setText("")
        self.phb.setFlat(True)
        self.phb.setObjectName("phb")
        self.dqzj = QtWidgets.QPushButton(Form)
        self.dqzj.setGeometry(QtCore.QRect(310, 350, 191, 121))
        self.dqzj.setText("")
        self.dqzj.setFlat(True)
        self.dqzj.setObjectName("dqzj")
        self.wqzj = QtWidgets.QPushButton(Form)
        self.wqzj.setGeometry(QtCore.QRect(600, 350, 191, 121))
        self.wqzj.setText("")
        self.wqzj.setFlat(True)
        self.wqzj.setObjectName("wqzj")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "福建十三水"))
#import ksjm_rc
