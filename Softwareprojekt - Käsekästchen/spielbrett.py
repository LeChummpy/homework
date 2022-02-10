import Stapel
import Bitboard
import PunktVisualisierung
import VerbindungVisualisierung
import copy
from turtle import *

class Spielbrett:
    def __init__(self, AnzahlKästchenHo, AnzahlKästchenVer):
        self.punkte = Bitboard.Bitboard(AnzahlKästchenHo, AnzahlKästchenVer)
        self.verbindungen = Stapel.Stapel()

        for i in range(1, AnzahlKästchenVer+1):
            innereliste = []
            for j in range(1, AnzahlKästchenHo+1):
                neuerPunkt = None

                if (i==1 and j==1) or (i==1 and j==AnzahlKästchenHo) or (i==AnzahlKästchenVer and j==1) or (i==AnzahlKästchenVer and j==AnzahlKästchenHo):
                    neuerPunkt = Eckpunkt((j*100-300, -i*100+300))

                elif ( (i==1 and (j!=1 and j!=AnzahlKästchenHo)) or ((i!=1 and i!=AnzahlKästchenVer) and j==1) or (i==AnzahlKästchenVer and (j!=1 and j!=AnzahlKästchenHo)) or ((i!=1 and i!=AnzahlKästchenVer) and j==AnzahlKästchenHo)  ):
                    neuerPunkt = Seitenpunkt((j*100-300, -i*100+300))

                else:
                    neuerPunkt = Innenpunkt((j*100-300, -i*100+300))

                self.punkte.ElementEinfuegen(j-1,i-1,neuerPunkt)

    #def VerbindungHinzufuegen(self):

class Punkt():
    def __init__(self, Koordinaten):
        self.Visualisierung = PunktVisualisierung.PunktVisualisierung(Koordinaten[0], Koordinaten[1], 20, "gray")
        self.Visualisierung.anschalten()
        self.id = id
        self.Koordinaten = Koordinaten

class Eckpunkt(Punkt):
    def __init__(self, Koordinaten):
        super().__init__(Koordinaten)
        self.Visualisierung.aendereFarbe("red")
        update()
        self.maxVerbindungen = 2

class Seitenpunkt(Punkt):
    def __init__(self, Koordinaten):
        super().__init__(Koordinaten)
        self.Visualisierung.aendereFarbe("yellow")
        update()
        self.maxVerbindungen = 3


class Innenpunkt(Punkt):
    maxVerbindungen = 4
    def __init__(self, Koordinaten):
        super().__init__(Koordinaten)
        self.Visualisierung.aendereFarbe("green")
        update()
        self.maxVerbindungen = 4

class Verbindung:
    def __init__(self, verbundenerPunkt1Nummer, verbundenerPunkt2Nummer):
        self.Visualisierung = VerbindungVisualisierung.VerbindungVisualisierung()
        self.verbundenerPunkt1 = verbundenerPunkt1Nummer
        self.verbundenerPunkt2 = verbundenerPunkt2Nummer

tracer(0, 0)
Spielbrett(4,4)
input()
