import socket
from threading import Thread, Event

import mainclasses
import colors
import datastructures
from helper import *

class käsekästchenserver:
    def __init__(self, port, AnzahlSpalten, AnzahlZeilen):
        self.current_Spielbrett = mainclasses.Spielbrett(AnzahlSpalten, AnzahlZeilen, 20)
        self.current_Spieler1 = mainclasses.Spieler(1, colors.lime_green)
        self.current_Spieler2 = mainclasses.Spieler(2, colors.dark_red)
        self.current_Spieler1_hostname = None
        self.current_Spieler2_hostname = None
        self.am_Zug = self.current_Spieler1

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ("localhost", port)
        self.mainthread = Thread(target=self.handleRequests, args=())
        self.running = None

    def start(self):
        self.mainthread.start()
        self.running = True

    def stop(self):
        self.running = False
        self.mainthread.join()

    def handleRequests(self):
        self.sock.bind(self.address)
        self.sock.listen()
        self.sock.settimeout(0.2)
        print("Lokalen Server erfolgreich gestartet auf Port ", self.address[1])

        while self.running:

            try:
                connection, client_address = self.sock.accept()
                print(client_address)

                if self.current_Spieler1_hostname==None or self.current_Spieler2_hostname==None: #wenn hostnamen noch nicht bekannt sind

                    if client_address[0]=="127.0.0.1":
                        self.current_Spieler1_hostname = client_address[0]
                        #self.sendToConnection(connection, "1")
                    else:
                        self.current_Spieler2_hostname = client_address[0]
                        #self.sendToConnection(connection, "1")

                else:   #wenn hostnamen von beiden Spieleclients jedoch bekannt sind

                    data = connection.recv()
                    print("received: ", data)
                    request_parts = data.decode("utf-8").split(" ")
                    operation = request_parts[0]
                    args = request_parts[1].split(",")

                    if operation=="add_connection":
                        indices_ersterPunkt = (args[0], args[1])
                        indices_zweiterPunkt = (args[2], args[3])
                        indizes_paar_angeklickter_punkte = [indices_ersterPunkt, indices_zweiterPunkt]

                        if client_address[0]==self.current_Spieler1_hostname: #wenn anfrage von spieler 1 (Hostgerät) kommt
                            if self.am_Zug.ID==1: #wenn spieler 1 auch dran ist dann füge verbindung hinzu
                                self.VerbindungSpielbrettHinzufügen(self, indizes_paar_angeklickter_punkte, self.am_Zug)
                                self.sendToConnection(connection, "2")
                                print("Verbindung von Spieler 1 hinzugefügt")

                            else:                 #wenn spieler 1 jedoch nicht dran sein sollte, dann füge keine Verbindung hinzu
                                self.sendToConnection(connection, "1")


                        elif client_address[0]==self.current_Spieler2_hostname: #wenn anfrage von spieler 2 (externes Gerät) kommt
                            if self.am_Zug.ID==2: #wenn spieler 2 auch dran ist dann füge verbindung hinzu
                                self.VerbindungSpielbrettHinzufügen(self, indizes_paar_angeklickter_punkte, self.am_Zug)
                                self.sendToConnection(connection, "2")
                                print("Verbindung von Spieler 2 hinzugefügt")


                            else:                 #wenn spieler 2 jedoch nicht dran sein sollte, dann füge keine Verbindung hinzu
                                self.sendToConnection(connection, "1")

                        else:   #wenn anfage von keinem der beiden spieleclients kommt
                            self.sendToConnection(connection, "0")

                        connection.close()

                    elif operation=="update_gamestate":
                        pass


            except socket.timeout:
                pass

            except:
                break

        print("socket closing")
        self.sock.close()

        def sendToConnection(self, conn, string):
            conn.sendall(string.encode())

        def VerbindungSpielbrettHinzufügen(self, indizes_paar_angeklickter_punkte, am_Zug):
            if (horizontaldervertikalbenachbart(indizes_paar_angeklickter_punkte)):
                if not(self.current_Spielbrett.angeklicktePunkteExistierenSchonAlsVerbindung(indizes_paar_angeklickter_punkte)):
                    kordsangeklicktezweipunkte = self.current_Spielbrett.KordsAngeklicktePunkteReturnieren(indizes_paar_angeklickter_punkte)
                    gewonnenepunkte = self.current_Spielbrett.VerbindungHinzufuegen(self.indizes_paar_angeklickter_punkte, kordsangeklicktezweipunkte, am_Zug.ID, am_Zug.verbindungsfarbe)

class käsekästchenclient:

    def __init__(self, view, server_address):
        self.view = view
        self.server_address = server_address
        self.mainthread = None
        self.running = None

        self.mainthread = Thread(target=self.pingeserveran, args=())
        self.mainthread.start()
        self.running = True

    def pingeserveran(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.server_address)
            print("sucecssfully pinged server")
            sock.close()

        self.updateGameattribute()

    def updateGameattribute(self):
        pass

    def sendeVerbindung(self, indizes_paar_angeklickter_punkte):


        indices_ersterPunkt = indizes_paar_angeklickter_punkte[0]
        indices_zweiterPunkt = indizes_paar_angeklickter_punkte[1]

        a1 = indices_ersterPunkt[0]
        a2 = indices_ersterPunkt[1]
        b1 = indices_zweiterPunkt[0]
        b2 = indices_zweiterPunkt[1]

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.server_address)
            data ="add_connection " + str(a1) + "," + str(a2) + str(b1) + "," + str(b2)
            sock.sendall(data.encode())
            status = sock.recv(16)
            print(status)
            sock.close()
