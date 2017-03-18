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
from mainwindow3 import Ui_MainWindow

#On ouvre le fichier de report
report = open("PingCheck_report.txt",'w')


#On cree un thread pour les operations de ping
class pingThread(QThread):
"""
initialisation du thread
:param:hostname: ip entree en argument (str)
:param:timecheck: temps entre en argument (int)
:param:GUI: interface graphique entree en argument (classe Ui_MainWindow de PyQt5)
"""
    def __init__(self,hostname, timecheck,GUI):
        QThread.__init__(self)

        #On initialise les variables locales de la classe
        self.hostname = hostname
        self.timecheck = timecheck
        self.ui = GUI

        #On recupere le temps de l'ouverture du thread
        self.now = int(time.time())

        #On initialise un compteur pour les pings successifs reussis
        self.count = 0

    def __del__(self):
        self.wait()
"""
fonction _ping_check
:param:hostname: ip (str)
:param:timecheck: temps (int)
"""
    def _ping_check(self, hostname, timecheck):

        #On change le texte du resultat avant de faire un ping
        self.text_result = "PingCheck : Checking ..."
        self.ui.lalbel_status.setText(self.text_result)

        #On ping l'ip entree en argument
        #On redirige la sortie de la commande vers une variable ping_var
        #On desactive l'affichage de la console a l'appel de subprocess
        self.ping_var = str(subprocess.Popen("ping %s" %self.hostname, stdout=subprocess.PIPE, creationflags=8).stdout.read())

        #On check si l'ip repond au ping
        if "TTL" in self.ping_var:
            self.text_result = "PingCheck : SUCCESS"

            #On incremente le compteur si c'est le cas
            self.count += 1
        else:
            self.text_result = "PingCheck : FAIL"
            #On reset le compteur sinon
            self.count = 0
            #On log dans le fichier si l'ip ne repond pas
            report.write(time.strftime("%d-%m-%Y | %X", time.localtime()) + '\t PingCheck failed (Hostname : %s)\n'%self.hostname)
            report.flush()

        #On update le texte du resultat
        self.ui.lalbel_status.setText(self.text_result)


        #On log la reponse consecutive de l'ip pendant X sec
        if (int(time.time()) >= (self.now + self.timecheck)) and (self.count != 0):
            report.write(time.strftime("%d-%m-%Y | %X", time.localtime()) + '\t %s secs of SUCCESS '%self.timecheck + '(Hostname : %s)\n'%self.hostname)
            report.flush()
            self.now = int(time.time())

"""
appel de la fonction de ping en boucle
delai de 3 secondes avant de la relancer
"""
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
        self.ui.button_start.clicked.connect(self.start_thread)


"""
fonction check_input
recupere les valeurs des widgets d'input_ip
test sur le host avec le module socket
conversion de l'input time
renvoie une liste de booleens
"""
    def check_input(self):
        #On initialise la liste sur True
        self.check = [True,True]
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

"""
fonction start_thread
si les parametres sont corrects, on lance le thread de ping
"""
    def start_thread(self):
        #Uniquement si les input sont valides
        if self.check_input() == [True,True]:
            #On charge le thread
            self.get_thread = pingThread(self.host,self.period,self.ui)
            #On l'execute
            self.get_thread.start()

            #On active le bouton stop
            self.ui.button_stop.setEnabled(True)

            #On desactive les input tant que le thread tourne
            self.ui.input_ip.setDisabled(True)
            self.ui.input_time.setDisabled(True)

            #On connecte le bouton stop a la fonction de stop
            self.ui.button_stop.clicked.connect(self.end_thread)

            #On desactive le bouton start pour ne pas lancer d'autre thread en meme temps
            self.ui.button_start.setEnabled(False)

"""
fonction end_thread
arrete le thread courant
inverse l'etat actif/inactif des widget
"""
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
    myapp.setWindowTitle("PyPingCheck")
    myapp.setWindowIcon(QIcon("Icone/ping_icon.png"))
    myapp.show()
    sys.exit(exitapp(app))

if __name__ == '__main__':
    main()
