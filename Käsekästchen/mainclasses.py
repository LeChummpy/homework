import Stapel
import Bitboard
import PunktVisualisierung
import VerbindungVisualisierung
from turtle import *

class Spielbrett:
    def __init__(self, AnzahlKästchenHo, AnzahlKästchenVer, RadiusPunkte):
        self.radiusPunkte = RadiusPunkte
        self.punkte = Bitboard.Bitboard(AnzahlKästchenHo, AnzahlKästchenVer)
        self.verbindungen = Stapel.Stapel()

        for i in range(1, AnzahlKästchenVer+1):
            innereliste = []
            for j in range(1, AnzahlKästchenHo+1):
                neuerPunkt = None

                if (i==1 and j==1) or (i==1 and j==AnzahlKästchenHo) or (i==AnzahlKästchenVer and j==1) or (i==AnzahlKästchenVer and j==AnzahlKästchenHo):
                    neuerPunkt = Eckpunkt((j*100-300, -i*100+300), self.radiusPunkte)

                elif ( (i==1 and (j!=1 and j!=AnzahlKästchenHo)) or ((i!=1 and i!=AnzahlKästchenVer) and j==1) or (i==AnzahlKästchenVer and (j!=1 and j!=AnzahlKästchenHo)) or ((i!=1 and i!=AnzahlKästchenVer) and j==AnzahlKästchenHo)  ):
                    neuerPunkt = Seitenpunkt((j*100-300, -i*100+300), self.radiusPunkte)

                else:
                    neuerPunkt = Innenpunkt((j*100-300, -i*100+300), self.radiusPunkte)

                self.punkte.ElementEinfuegen(j-1,i-1,neuerPunkt)

    def IndicesVonAngeklicktemPunktReturnieren(self, x, y):
        dimsPunkteBitboard = self.punkte.DimensionenReturnieren()
        for i in range(dimsPunkteBitboard[0]):
            for j in range(dimsPunkteBitboard[1]):
                aktuellerPunkt = self.punkte.ElementReturnieren(i, j)
                KoordinatenAktuellerPunkt = aktuellerPunkt.KoordinatenReturnieren()
                if (x>KoordinatenAktuellerPunkt[0]-self.radiusPunkte and x<KoordinatenAktuellerPunkt[0]+self.radiusPunkte and y>KoordinatenAktuellerPunkt[1]-self.radiusPunkte and y<KoordinatenAktuellerPunkt[1]+self.radiusPunkte):
                    return (i,j)

        return None

    def VerbindungHinzufuegen(self, indicesAngeklickteZweiPunkte, SpielerID):
        def horizontalderverticalbenachbart(indicesAngeklickteZweiPunkte):
            indicesPunkt1 = indicesAngeklickteZweiPunkte[0]
            indicesPunkt2 = indicesAngeklickteZweiPunkte[1]
            if (indicesPunkt1[0]==indicesPunkt2[0] and (indicesPunkt1[1]+1==indicesPunkt2[1] or indicesPunkt1[1]-1==indicesPunkt2[1])) or ((indicesPunkt1[0]+1==indicesPunkt2[0] or indicesPunkt1[0]-1==indicesPunkt2[0]) and indicesPunkt1[1]==indicesPunkt2[1]):
                return True
            else:
                return False

        if horizontalderverticalbenachbart(indicesAngeklickteZweiPunkte):
            v = Verbindung(indicesAngeklickteZweiPunkte[0], indicesAngeklickteZweiPunkte[1], SpielerID)
            self.verbindungen.Draufpacken(v)

class Punkt:
    def __init__(self, Koordinaten, Radius, Farbe):
        self.Visualisierung = PunktVisualisierung.PunktVisualisierung(Koordinaten[0], Koordinaten[1], Radius, Farbe)
        self.Visualisierung.anschalten()
        update()
        self.id = id
        self.Koordinaten = Koordinaten

    def KoordinatenReturnieren(self):
        return self.Koordinaten

class Eckpunkt(Punkt):
    def __init__(self, Koordinaten, Radius):
        super().__init__(Koordinaten, Radius, "red")
        self.maxVerbindungen = 2

class Seitenpunkt(Punkt):
    def __init__(self, Koordinaten, Radius):
        super().__init__(Koordinaten, Radius, "blue")
        self.maxVerbindungen = 3

class Innenpunkt(Punkt):
    maxVerbindungen = 4
    def __init__(self, Koordinaten, Radius):
        super().__init__(Koordinaten, Radius, "green")
        self.maxVerbindungen = 4

class Verbindung:
    def __init__(self, verbundenerPunkt1Indices, verbundenerPunkt2Indices, SpielerID):
        punkt1Koordinaten = self.punkte.ElementReturnieren(verbundenerPunkt1Indices[0], verbundenerPunkt1Indices[1]).Koordinaten
        punkt2Koordinaten = self.punkte.ElementReturnieren(verbundenerPunkt2Indices[0], verbundenerPunkt2Indices[1]).Koordinaten

        self.Visualisierung = VerbindungVisualisierung.VerbindungVisualisierung(punkt1Koordinaten[0],punkt1Koordinaten[1], punkt2Koordinaten[0],punkt2Koordinaten[1], 10, "black")
        self.SpielerID = SpielerID
        self.verbundenerPunkt1Indices = verbundenerPunkt1Indices
        self.verbundenerPunkt2Indices = verbundenerPunkt2Indices

class Spieler:
    def __init__(self, ID):
        self.Punkte = 0
        self.ID = ID
