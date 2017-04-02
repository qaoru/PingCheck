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
from mainwindow4 import Ui_MainWindow


#On cree un thread pour les operations de ping
class pingThread(QThread):


    def __init__(self,hostname, timecheck,GUI, report):
        QThread.__init__(self)

        #On initialise les variables locales de la classe
        self.hostname = hostname
        self.timecheck = timecheck
        self.ui = GUI
        self.report = open(report + "/PyPingCheck_report.txt",'a')

        #On recupere le temps de l'ouverture du thread comme temps du dernier succes
        self.successtime= int(time.time())

        #On initialise une variable d'erreur de ping
        self.pingerror = False

    def __del__(self):
        self.wait()

    def _ping_check(self, hostname, timecheck):

        #On change le texte du resultat avant de faire un ping
        self.text_result = "PingCheck : Checking ..."
        self.ui.label_status.setText(self.text_result)
        self.ui.label_status.setStyleSheet("color: rgba(0,0,0,1);")
        #On ping l'ip entree en argument
        #On redirige la sortie de la commande vers une variable ping_var
        #On desactive l'affichage de la console a l'appel de subprocess
        self.ping_var = str(subprocess.Popen("ping %s" %self.hostname, stdout=subprocess.PIPE, creationflags=8).stdout.read())

        #On check si l'ip repond au ping
        if "TTL" in self.ping_var:
            self.text_result = "PingCheck : SUCCESS"

            #Si la variable d'erreur est vraie, on reset le temps du dernier succes
            if self.pingerror == True:
                self.successtime = int(time.time())

                #On remet la variable d'erreur sur faux
                self.pingerror = False


        else:
            self.text_result = "PingCheck : FAIL"
            #On met la variable d'erreur a l'etat vrai
            self.pingerror = True

            #On log dans le fichier si l'ip ne repond pas
            self.report.write(time.strftime("%d-%m-%Y | %X", time.localtime()) + '\t PingCheck failed (Hostname : %s)\n'%self.hostname)
            self.report.flush()

        #On update le texte du resultat
        self.ui.label_status.setText(self.text_result)
        self.ui.label_status.setStyleSheet("color: rgba(255,0,0,1);")


        #On log la reponse consecutive de l'ip pendant X sec
        if (int(time.time()) >= (self.successtime + self.timecheck)):
            self.report.write(time.strftime("%d-%m-%Y | %X", time.localtime()) + '\t %s secs of SUCCESS '%self.timecheck + '(Hostname : %s)\n'%self.hostname)
            self.report.flush()
            self.successtime = int(time.time())

    def run(self):
        while True:
            self._ping_check(self.hostname, self.timecheck)
            self.sleep(3)

#Application
class ShipHolderApplication(QMainWindow):

    #On initialise l'interface graphique et le bouton start
    def __init__(self):
        super (self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.input_file.setText("Report directory")
        self.ui.button_start.clicked.connect(self.start_thread)
        self.ui.button_file.clicked.connect(self.get_file)


    def get_file(self):
        self.report_file_path = QFileDialog.getExistingDirectory(self)
        self.ui.input_file.setText(self.report_file_path)

    def check_input(self):
        #On initialise la liste sur True
        self.check = [True,True,True]

        #On recupere le chemin du rapport
        self.report = str(self.ui.input_file.text())
        if os.path.isdir(self.report) != True:
            self.ui.input_file.setText("Error : Please select a directory")
            self.check[2] = False

        #On recupere la valeur d'input de l'host
        self.host = str(self.ui.input_ip.text())

        #On teste si l'ip est valide
        if valid_ip(self.host) != True:
            #On affiche un message d'erreur si elle ne l'est pas
            self.ui.label_iperror.setText("Wrong IP format")
            #On met l'element de la liste sur False
            self.check[0] = False
        else:
            self.ui.label_iperror.setText("")

        #On recupere la valeur d'input time
        self.period = str(self.ui.input_time.text())
        #On essaye de convertir la chaine en entier
        try:
            int(self.period)
        except:
            #On affiche un message d'erreur si besoin
            self.ui.label_timerror.setText("Wrong time format")
            #On met la liste a jour
            self.check[1] = False
        else:
            self.ui.label_timerror.setText("")
            #Si c'est possible, on convertit la chaine en entier
            self.period = int(self.period)
        #On retourne la liste
        return self.check


    def start_thread(self):
        #Uniquement si les input sont valides
        if self.check_input() == [True,True,True]:

            #On charge le thread
            self.get_thread = pingThread(self.host,self.period,self.ui, self.report)
            #On l'execute
            self.get_thread.start()

            #On active le bouton stop
            self.ui.button_stop.setEnabled(True)

            #On desactive les input tant que le thread tourne
            self.ui.input_ip.setDisabled(True)
            self.ui.input_time.setDisabled(True)
            self.ui.input_file.setDisabled(True)

            #On desactive le bouton de recherche
            self.ui.button_file.setEnabled(False)

            #On connecte le bouton stop a la fonction de stop
            self.ui.button_stop.clicked.connect(self.end_thread)

            #On desactive le bouton start pour ne pas lancer d'autre thread en meme temps
            self.ui.button_start.setEnabled(False)


    def end_thread(self):
        self.get_thread.terminate()
        self.ui.button_start.setEnabled(True)
        self.button_file.setEnabled(True)
        self.ui.input_ip.setDisabled(False)
        self.ui.input_time.setDisabled(False)
        self.ui.input_file.setDisabled(False)
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
    myapp.setWindowTitle("PyPingCheck")
    myapp.setWindowIcon(QIcon("Icone/ping_icon.png"))
    myapp.show()
    sys.exit(exitapp(app))

if __name__ == '__main__':
    main()
