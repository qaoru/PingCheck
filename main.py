#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import time
import socket
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow2 import Ui_MainWindow

def testfun():
    print("hello world")

report = open("PingCheck_report.txt",'w')
class pingThread(QThread):
    def __init__(self,hostname, timecheck,GUI):
        QThread.__init__(self)
        self.hostname = hostname
        self.timecheck = timecheck
        self.ui = GUI
        self.now = int(time.time())
        self.count = 0

    def __del__(self):
        self.wait()

    def _ping_check(self, hostname, timecheck):
        self.text_result = "Checking ..."
        self.ui.lalbel_status.setText(self.text_result)
        self.ping_var = str(subprocess.Popen("ping %s" %self.hostname, stdout=subprocess.PIPE, creationflags=8).stdout.read())


        if "TTL" in self.ping_var:
            self.text_result = "PingCheck : SUCCESS"
            self.count += 1
        else:
            self.text_result = "PingCheck : FAIL"
            self.count = 0
            report.write(time.strftime("%d-%m-%Y | %X", time.localtime()) + '\t PingCheck failed (Hostname : %s)\n'%self.hostname)
            report.flush()

        self.ui.lalbel_status.setText(self.text_result)

        if (int(time.time()) >= (self.now + self.timecheck)) and (self.count != 0):
            report.write(time.strftime("%d-%m-%Y | %X", time.localtime()) + '\t %s secs of SUCCESS '%self.timecheck + '(Hostname : %s)\n'%self.hostname)
            report.flush()
            self.now = int(time.time())


    def run(self):
        while True:
            self._ping_check(self.hostname, self.timecheck)
            self.sleep(3)

class ShipHolderApplication(QMainWindow):
    def __init__(self):
        super (self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_start.clicked.connect(self.start_thread)


    def start_thread(self):
        self.host = str(self.ui.input_ip.text())
        self.period = int(self.ui.input_time.text())
        self.get_thread = pingThread(self.host,self.period,self.ui)
        self.get_thread.start()
        self.ui.button_stop.setEnabled(True)
        self.ui.input_ip.setDisabled(True)
        self.ui.input_time.setDisabled(True)
        self.ui.button_stop.clicked.connect(self.end_thread)
        self.ui.button_start.setEnabled(False)

    def end_thread(self):
        self.get_thread.terminate()
        self.ui.button_start.setEnabled(True)
        self.ui.input_ip.setDisabled(False)
        self.ui.input_time.setDisabled(False)
        self.ui.button_stop.setEnabled(False)




def valid_ip(address):
    try:
        socket.inet_aton(address)
        return True
    except:
        return False


def exitapp(app):
    app.exec_()

def main():
    app = QApplication(sys.argv)
    myapp = ShipHolderApplication()
    myapp.show()
    sys.exit(exitapp(app))

if __name__ == '__main__':
    main()
