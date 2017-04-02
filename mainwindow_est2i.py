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
        MainWindow.resize(500, 360)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label_ip = QtWidgets.QLabel(self.centralWidget)
        self.label_ip.setGeometry(QtCore.QRect(20, 70, 35, 20))
        self.label_ip.setStyleSheet("font-weight: bold;")
        self.label_ip.setObjectName("label_ip")
        self.label_time = QtWidgets.QLabel(self.centralWidget)
        self.label_time.setGeometry(QtCore.QRect(20, 120, 100, 20))
        self.label_time.setObjectName("label_time")
        self.input_ip = QtWidgets.QLineEdit(self.centralWidget)
        self.input_ip.setGeometry(QtCore.QRect(65, 70, 110, 20))
        self.input_ip.setObjectName("input_ip")
        self.input_time = QtWidgets.QLineEdit(self.centralWidget)
        self.input_time.setGeometry(QtCore.QRect(130, 120, 45, 20))
        self.input_time.setObjectName("input_time")
        self.button_start = QtWidgets.QPushButton(self.centralWidget)
        self.button_start.setGeometry(QtCore.QRect(320, 300, 75, 23))
        self.button_start.setObjectName("button_start")
        self.button_stop = QtWidgets.QPushButton(self.centralWidget)
        self.button_stop.setGeometry(QtCore.QRect(410, 300, 75, 23))
        self.button_stop.setObjectName("button_stop")
        self.label_title = QtWidgets.QLabel(self.centralWidget)
        self.label_title.setGeometry(QtCore.QRect(0, 10, 160, 30))
        self.label_title.setStyleSheet("font: 75 italic 13pt \"Comic Sans MS\";\n"
"\n"
"padding-left: 10px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 170, 255, 255), stop:1 rgba(255, 255, 255, 0));")
        self.label_title.setObjectName("label_title")
        self.label_status = QtWidgets.QLabel(self.centralWidget)
        self.label_status.setGeometry(QtCore.QRect(20, 180, 155, 20))
        self.label_status.setStyleSheet("border: 1px ridge black;\n"
"padding-left: 3px;")
        self.label_status.setObjectName("label_status")
        self.label_iperror = QtWidgets.QLabel(self.centralWidget)
        self.label_iperror.setGeometry(QtCore.QRect(65, 95, 100, 20))
        self.label_iperror.setText("")
        self.label_iperror.setObjectName("label_iperror")
        self.label_timerror = QtWidgets.QLabel(self.centralWidget)
        self.label_timerror.setGeometry(QtCore.QRect(65, 145, 100, 20))
        self.label_timerror.setText("")
        self.label_timerror.setObjectName("label_timerror")
        self.label_file = QtWidgets.QLabel(self.centralWidget)
        self.label_file.setGeometry(QtCore.QRect(20, 230, 91, 20))
        self.label_file.setStyleSheet("text-decoration: underline;")
        self.label_file.setObjectName("label_file")
        self.input_file = QtWidgets.QLineEdit(self.centralWidget)
        self.input_file.setGeometry(QtCore.QRect(20, 260, 180, 20))
        self.input_file.setObjectName("input_file")
        self.button_file = QtWidgets.QPushButton(self.centralWidget)
        self.button_file.setGeometry(QtCore.QRect(210, 260, 75, 20))
        self.button_file.setObjectName("button_file")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 251, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Est2i.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(240, 160, 251, 61))
        self.label_2.setStyleSheet("padding-left: 3px;")
        self.label_2.setObjectName("label_2")
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
        self.input_time.setText(_translate("MainWindow", "600"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_stop.setText(_translate("MainWindow", "Stop"))
        self.label_title.setText(_translate("MainWindow", "PyPingCheck v2.2"))
        self.label_status.setText(_translate("MainWindow", "STATUS :"))
        self.label_file.setText(_translate("MainWindow", "Report location :"))
        self.button_file.setText(_translate("MainWindow", "Browse ..."))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Est2i<br/>67 rue du Général Leclerc<br/>67202 Wolfisheim</span></p></body></html>"))

