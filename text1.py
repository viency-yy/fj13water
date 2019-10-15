# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 643)
        MainWindow.setStyleSheet("MainWindow.setStyleSheet(“background-image:url(:/newPrefix/python/fjsss/福建十三水1.jpg)”)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fjsss = QtWidgets.QLabel(self.centralwidget)
        self.fjsss.setGeometry(QtCore.QRect(0, 0, 831, 591))
        self.fjsss.setText("")
        self.fjsss.setTextFormat(QtCore.Qt.AutoText)
        self.fjsss.setPixmap(QtGui.QPixmap(r"C:\Users\Your Dad\Desktop/python/fjsss/福建十三水1.jpg"))
        self.fjsss.setObjectName("fjsss")
        self.zuce = QtWidgets.QPushButton(self.centralwidget)
        self.zuce.setGeometry(QtCore.QRect(510, 460, 261, 71))
        self.zuce.setMouseTracking(False)
        self.zuce.setText("")
        self.zuce.setFlat(True)
        self.zuce.setObjectName("zuce")
        self.denglu = QtWidgets.QPushButton(self.centralwidget)
        self.denglu.setGeometry(QtCore.QRect(90, 450, 261, 71))
        self.denglu.setMouseTracking(False)
        self.denglu.setText("")
        self.denglu.setFlat(True)
        self.denglu.setObjectName("denglu")
        self.dengluk = QtWidgets.QLabel(self.centralwidget)
        self.dengluk.setGeometry(QtCore.QRect(0, 0, 831, 591))
        self.dengluk.setText("")
        self.dengluk.setPixmap(QtGui.QPixmap(":/newPrefix/python/fjsss/登录s.jpg"))
        self.dengluk.setObjectName("dengluk")
        self.yhm = QtWidgets.QLineEdit(self.centralwidget)
        self.yhm.setGeometry(QtCore.QRect(390, 380, 161, 25))
        self.yhm.setObjectName("yhm")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 420, 161, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.qr = QtWidgets.QPushButton(self.centralwidget)
        self.qr.setGeometry(QtCore.QRect(390, 450, 71, 23))
        self.qr.setText("")
        self.qr.setFlat(True)
        self.qr.setObjectName("qr")
        self.yhm.raise_()
        self.lineEdit.raise_()
        self.qr.raise_()
        self.dengluk.raise_()
        self.fjsss.raise_()
        self.zuce.raise_()
        self.denglu.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
'''
        self.retranslateUi(MainWindow)
        self.denglu.clicked.connect(self.dengluk.raise)
        self.denglu.clicked.connect(self.yhm.raise)
        self.denglu.clicked.connect(self.lineEdit.raise)
        self.denglu.clicked.connect(self.dengluk.raise)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
'''
def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#import try_rc
