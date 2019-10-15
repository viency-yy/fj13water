# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gwzj.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class GWZJ(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(828, 581)
        self.gwzj = QtWidgets.QLabel(widget)
        self.gwzj.setGeometry(QtCore.QRect(1, -6, 851, 601))
        self.gwzj.setText("")
        self.gwzj.setPixmap(QtGui.QPixmap(r"C:\Users\Your Dad\Desktop/python/fjsss/过往战局1s.jpg"))
        self.gwzj.setObjectName("gwzj")
        self.yhid = QtWidgets.QLineEdit(widget)
        self.yhid.setGeometry(QtCore.QRect(120, 80, 151, 31))
        self.yhid.setObjectName("yhid")
        self.cx = QtWidgets.QPushButton(widget)
        self.cx.setGeometry(QtCore.QRect(290, 80, 93, 28))
        self.cx.setObjectName("cx")
        self.xxcx = QtWidgets.QPushButton(widget)
        self.xxcx.setGeometry(QtCore.QRect(290, 270, 93, 28))
        self.xxcx.setObjectName("xxcx")
        self.zjid = QtWidgets.QLineEdit(widget)
        self.zjid.setGeometry(QtCore.QRect(120, 270, 151, 31))
        self.zjid.setObjectName("zjid")
        self.tableWidget = QtWidgets.QTableWidget(widget)
        self.tableWidget.setGeometry(QtCore.QRect(120, 120, 271, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(widget)
        self.tableWidget_2.setGeometry(QtCore.QRect(120, 310, 271, 211))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.cx.setText(_translate("widget", "查询"))
        self.xxcx.setText(_translate("widget", "详细查询"))
#import dzjl1_rc
