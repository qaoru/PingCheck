# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label_ip = QtWidgets.QLabel(self.centralWidget)
        self.label_ip.setGeometry(QtCore.QRect(20, 70, 31, 16))
        self.label_ip.setStyleSheet("font-weight: bold;")
        self.label_ip.setObjectName("label_ip")
        self.label_time = QtWidgets.QLabel(self.centralWidget)
        self.label_time.setGeometry(QtCore.QRect(20, 120, 101, 16))
        self.label_time.setObjectName("label_time")
        self.input_ip = QtWidgets.QLineEdit(self.centralWidget)
        self.input_ip.setGeometry(QtCore.QRect(60, 70, 113, 20))
        self.input_ip.setObjectName("input_ip")
        self.input_time = QtWidgets.QLineEdit(self.centralWidget)
        self.input_time.setGeometry(QtCore.QRect(130, 120, 61, 20))
        self.input_time.setText("")
        self.input_time.setObjectName("input_time")
        self.button_start = QtWidgets.QPushButton(self.centralWidget)
        self.button_start.setGeometry(QtCore.QRect(180, 220, 75, 23))
        self.button_start.setObjectName("button_start")
        self.button_stop = QtWidgets.QPushButton(self.centralWidget)
        self.button_stop.setGeometry(QtCore.QRect(290, 220, 75, 23))
        self.button_stop.setObjectName("button_stop")
        self.label_title = QtWidgets.QLabel(self.centralWidget)
        self.label_title.setGeometry(QtCore.QRect(280, 10, 101, 20))
        self.label_title.setObjectName("label_title")
        self.lalbel_status = QtWidgets.QLabel(self.centralWidget)
        self.lalbel_status.setGeometry(QtCore.QRect(20, 180, 131, 21))
        self.lalbel_status.setStyleSheet("border: 2px ridge black;")
        self.lalbel_status.setObjectName("lalbel_status")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_ip.setText(_translate("MainWindow", "IPv4 :"))
        self.label_time.setText(_translate("MainWindow", "Checking time (sec) :"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_stop.setText(_translate("MainWindow", "Quit"))
        self.label_title.setText(_translate("MainWindow", "PyPingCheck v2.0"))
        self.lalbel_status.setText(_translate("MainWindow", "STATUS :"))

