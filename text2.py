'''
    PyQt5 实现显示和业务逻辑分离, 继承主界面文件的主窗口类
    @Author: Notus(hehe_xiao@qq.com)
    @Create: 2019-02-10
    @Update: 2019-02-10
'''
import sys, os
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from text1 import Ui_MainWindow
from ksjm1 import KSJM
from phb1 import PHB
from gwzj import GWZJ
from cpjm1 import DQZJ
import requests
import http.client
import string
import json
import sys, os
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

##十三水##
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.denglu.clicked.connect(self.dljm)
        self.zuce.clicked.connect(self.zcjm)
    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()
    def dljm(self):
        dialog.exec_()
    def zcjm(self):
        zc.exec_()

##过往战局##
class GWZJ(QWidget,GWZJ):
    def __init__(self, parent=None):
        super(GWZJ, self).__init__(parent)
        self.setupUi(self)
        self.cx.clicked.connect(self.findzjlb)
        self.xxcx.clicked.connect(self.findxq)
    # 根据输入框历史战局详情
    def findxq(self):
        id = self.zjid.text()
        token = text['data']['token']
        headers = {'content-type': "application/json",'x-auth-token': token}
        response = requests.get(url="https://api.shisanshui.rtxux.xyz/history/" +id,
                                      headers=headers)
        text2 = json.loads(response.text)
        #self.label_2.setText('不会做')
        print(text2)

        status = text2['status']
        if status == 3001:
            print('！战局不存在或未结束！')
            return 0
        elif status == 3002:
            print('！玩家不存在！')

        text3 = text2['data']['detail']
        array = text3
        strid = []
        strname = []
        strscore = []
        strcard = []
        for i in array:
            strid.append(i['player_id'])
            strname.append(i['name'])
            strscore.append(i['score'])
            strcard.append(i['card'])

        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(4)
        str2 = ('id', 'name', 'score', 'card')
        self.tableWidget_2.setHorizontalHeaderLabels(str2)
        self.tableWidget_2.setColumnWidth(0, 50)
        self.tableWidget_2.setColumnWidth(1, 150)
        self.tableWidget_2.setColumnWidth(2, 70)
        self.tableWidget_2.setColumnWidth(3, 470)

        for i in range(4):
            newitem1 = QTableWidgetItem("%d" % strid[i])
            newitem2 = QTableWidgetItem(strname[i])
            newitem3 = QTableWidgetItem("%d" % strscore[i])
            newitem4 = QTableWidgetItem("%s" % strcard[i])

            self.tableWidget_2.setItem(i, 0, newitem1)
            self.tableWidget_2.setItem(i, 1, newitem2)
            self.tableWidget_2.setItem(i, 2, newitem3)
            self.tableWidget_2.setItem(i, 3, newitem4)
    def findzjlb(self):
        token = text['data']['token']
        id = text['data']['user_id']
        conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
        headers = {'x-auth-token': token}
        conn.request("GET", "/history?page=0&limit=10&player_id=%d" % id, headers=headers)
        res = conn.getresponse()
        data = res.read()
        print(data)
        listduizhan = json.loads(data.decode("utf-8"))
        listdui = listduizhan['data']
        print(listduizhan)
        print(listdui)
        #self.label.setText('不会')
        strid = []
        strcard = []
        strscore = []

        for i in listdui:
            strid.append(i['id'])
            strcard.append(i['card'])
            strscore.append(i['score'])

        length = len(listdui)
        self.tableWidget.setRowCount(length)
        self.tableWidget.setColumnCount(3)
        str1 = ('id', 'card', 'score')
        self.tableWidget.setColumnWidth(0, 110)
        self.tableWidget.setColumnWidth(1, 445)
        self.tableWidget.setHorizontalHeaderLabels(str1)

        for i in range(length):
            newitem1 = QTableWidgetItem("%d" % strid[i])
            newitem2 = QTableWidgetItem("%s" % strcard[i])
            newitem3 = QTableWidgetItem("%d" % strscore[i])

            self.tableWidget.setItem(i, 0, newitem1)
            self.tableWidget.setItem(i, 1, newitem2)
            self.tableWidget.setItem(i, 2, newitem3)

##排行榜##
class PHB(QWidget,PHB):
    def __init__(self, parent=None):
        super(PHB, self).__init__(parent)
        self.setupUi(self)


    def getphb(self):
        conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
        conn.request("GET", "/rank")
        res = conn.getresponse()
        res2 = requests.get(res.headers['Location'])
        array = json.loads(res2.text)
        print(array)
        self.label_2.setNum(array[0]['player_id'])
        self.label_3.setText(array[0]['name'])
        self.label_4.setNum(array[0]['score'])
        self.label_5.setNum(array[1]['player_id'])
        self.label_7.setText(array[1]['name'])
        self.label_6.setNum(array[1]['score'])
        self.label_10.setNum(array[2]['player_id'])
        self.label_9.setText(array[2]['name'])
        self.label_8.setNum(array[2]['score'])
        self.label_11.setNum(array[3]['player_id'])
        self.label_12.setText(array[3]['name'])
        self.label_13.setNum(array[3]['score'])

##当前战局##
class DQZJ(QWidget,DQZJ):
    def __init__(self, parent=None):
        super(DQZJ, self).__init__(parent)
        self.setupUi(self)
        self.cpan.clicked.connect(self.cp)
    def fapai(self):
         token = text['data']['token']
         conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
         headers = {'content-type': "application/json",'x-auth-token': token}
         conn.request("POST", "/game/open", headers=headers)
         res = conn.getresponse()
         data = res.read()
         global text1
         text1 = json.loads(data.decode("utf-8"))
         id = text1['data']['id']
         card = text1['data']['card']
         global tk
         tk = card
         self.label_2.setText(card)
         global flagcard
         flagcard = 1

    def cp(self):
        pass

##开始界面##
class KSJM(QWidget, KSJM):
    def __init__(self, parent=None):
        super(KSJM, self).__init__(parent)
        self.setupUi(self)
        self.phb.clicked.connect(self.showphb)
        self.wqzj.clicked.connect(self.showgwzj)
        self.dqzj.clicked.connect(self.showdqzj)
    def handle_click(self):
        if not self.isVisible():
            self.show()
    def handle_close(self):
        self.close()

    def showphb(self):
        myphb.show()
        myphb.getphb()


    def showgwzj(self):
        mygwzj.show()
    def showdqzj(self):
        mydqzj.show()
        mydqzj.fapai()
##登录
class logindialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('登录界面')
        self.resize(200, 150)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        ###### 设置界面控件
        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("确定")
        self.verticalLayout.addWidget(self.pushButton_enter)

        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("取消")
        self.verticalLayout.addWidget(self.pushButton_quit)

        ###### 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.pushButton_quit.clicked.connect(self.accept)


    def on_pushButton_enter_clicked(self):
        yhid = self.lineEdit_account.text()
        yhmm = self.lineEdit_password.text()
        if yhid and yhmm:
            data1 = {'username': yhid, 'password': yhmm}
            json1_idmm = json.dumps(data1)
            conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
            payload = json1_idmm
            headers = {'content-type': "application/json"}
            conn.request("POST", "/auth/login", payload, headers)
            res = conn.getresponse()
            data = res.read()
            global text
            text = json.loads(data.decode("utf-8"))
            print(text)
            print(text['status'])
            if text["status"]==0:
                self.accept()
                myksjm.show()
            elif text["status"]==1001:
                print('！用户名已被使用！')
            elif text["status"] == 1002:
                print('！学号已绑定！')
            elif text["status"]==1003:
                print('！教务处认证失败！')
            else:
                print('！w无法登录！')
                return 0

        else:  # id密码没有输入完整无法登录！
            print('！无法登录！')
            self.accept()
            return 0


        '''
        # 账号判断
        if self.lineEdit_account.text() == "":
            return

        # 密码判断
        if self.lineEdit_password.text() == "":
            return
        '''
        # 通过验证，关闭对话框并返回1
##注册##
class zcdialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('注册界面')
        self.resize(200, 150)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        ###### 设置界面控件
        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("确定")
        self.verticalLayout.addWidget(self.pushButton_enter)

        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("取消")
        self.verticalLayout.addWidget(self.pushButton_quit)

        ###### 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.pushButton_quit.clicked.connect(self.accept)

    def on_pushButton_enter_clicked(self):

        yhzh = self.lineEdit_account.text()
        yhmm1 = self.lineEdit_password.text()
        # 点击注册之后直接传json过去
        data2 = {'username': yhzh, 'password': yhmm1}
        json2_zcidmm = json.dumps(data2)
        headers = {'content-type': "application/json"}
        conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
        payload = json2_zcidmm
        conn.request("POST", "/auth/register", payload,headers)
        res = conn.getresponse()
        data = res.read()
        gett = json.loads(data.decode("utf-8"))

        print(gett['status'])
        if gett["status"] == 0:
            print('！注册成功！')
            self.accept()
        elif gett["status"] == 1001:
            print('！用户名已被使用！')
        elif gett["status"] == 1002:
            print('！学号已绑定！')
        elif gett["status"] == 1003:
            print('！教务处认证失败！')
        else:
            print('！注册失败！')
        '''
        # 账号判断
        if self.lineEdit_account.text() == "":
            return

        # 密码判断
        if self.lineEdit_password.text() == "":
            return
        '''
     # 通过验证，关闭对话框并返回1
##主##
if __name__ == "__main__":
 app = QApplication(sys.argv)
 dialog = logindialog()
 zc=zcdialog()
 myWin = MyMainWindow()
 myWin.show()
 myksjm=KSJM()
 myphb=PHB()
 mygwzj=GWZJ()
 mydqzj=DQZJ()
 sys.exit(app.exec_())