import lampe
import time

class Codeschloss:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__offen = False
        self.__falscheVersuche = 0
        self.__korrektePIN = "111"
        self.__eingestelltePIN = "000"

        self.__LampeOben = lampe.Lampe(self.__x, self.__y, 20, "red")
        self.__LampeUnten = lampe.Lampe(self.__x, self.__y+40, 20, "green")

    def gibPosition(self):
        #Vor.: -
        #Erg.: Die X- und Y-Koordinate des Codeschlosses auf dem Bildschirm ist als Tuple geliefert.

        return (self.__x, self.__y)

    def setzePosition(self, x, y):
        #Vor.: -x- und -y- sind als Integer beim Funktionsaufruf übergeben.
        #Erg.: X- und Y-Koordinate des Codeschlosses werden zur übergebene x- und y-Koordinate geändert

        self.__x = x
        self.__y = y
        self.__LampeOben.verschieben(self.__x, self.__y)
        self.__LampeUnten.verschieben(x, y+40)

    def gibAnzahlFehlversuche(self):
        #Vor.: -
        #Eff.: Falls das Schloss geschlossen ist, so blinkt die rote Lampe so oft, wie seit dem letzen Mal Öffnen der Code falsch eingegeben wurde.

        if (self.__offen==False):
            for i in range(self.__falscheVersuche):
                self.__LampeOben.anschalten()
                time.sleep(1)
                self.__LampeOben.ausschalten()

    def oeffnen(self, PIN):
        #Vor.: -PIN- ist als String beim Funktionsaufruf übergeben.
        #Eff.: Falls die PIN korrekt ist, so ist das Schloss unabhängig vom vorherigen Zustand geöffnet, die grüne Lampe
        #      blinkt eine Sekunde und die Anzahl falscher Versuche seit dem letzten Mal Öffnen werden zurückgesetzt.
        #      Falls die PIN jedoch nicht korrekt war, so wird die Anzahl falscher Versuche seit dem letzten Mal Öffnen um 1 erhöht und die rote Lampe blinkt
        #      So oft, wie nun seit dem letzen Mal Öffnen der Code falsch eingegeben wurde.

        if (PIN==self.__korrektePIN):
            self.__offen = True
            self.__LampeUnten.anschalten()
            time.sleep(1)
            self.__LampeOben.anschalten()
            self.__falscheVersuche = 0

        else:
            self.__falscheVersuche+=1
            for i in range(self.__falscheVersuche):
                self.__LampeUnten.anschalten()
                time.sleep(1)
                self.__LampeUnten.ausschalten()

    def schliessen(self):
        #Vor.: -
        #Eff.: Unabhängig vom vorherigen Zustand ist das Schloss nun geschlossen

        self.__offen = False

    def istOffen(self):
        #Vor.: -
        #Erg.: Ist das Schloss offen, so ist True geliefert, andernfalls False.

        return self.__offen

    def neuerPIN(self, PIN):
        #Vor.: -PIN- ist als String beim Funktionsaufruf übergeben.
        #Eff.: Falls das Schloss geschlossen ist, so blinkt die rote Lampe 1 Sekunde. Andernfalls wird ist die PIN nun geändert und die grüne Lampe blinkt 1 Sekunde.

        if (self.__offen==False):
            self.__LampeOben.anschalten()
            time.sleep(1)
            self.__LampeOben.ausschalten()

        else:
            self.__korrektePIN = PIN
            self.__LampeUnten.anschalten()
            time.sleep(1)
            self.__LampeUnten.ausschalten()
