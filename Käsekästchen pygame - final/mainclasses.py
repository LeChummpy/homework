import datastructures
import pygame
import colors
from helper import *

class Spielbrett:
    def __init__(self, AnzahlKästchenHo, AnzahlKästchenVer, RadiusPunkte):
        self.AnzahlKästchenHo = AnzahlKästchenHo
        self.AnzahlKästchenVer = AnzahlKästchenVer
        self.punkte = datastructures.Bitboard(AnzahlKästchenHo, AnzahlKästchenVer)
        self.verbindungen = datastructures.Schlange()

        for i in range(1, AnzahlKästchenVer+1):
            innereliste = []
            for j in range(1, AnzahlKästchenHo+1):
                neuerPunkt = None

                if (i==1 and j==1) or (i==1 and j==AnzahlKästchenHo) or (i==AnzahlKästchenVer and j==1) or (i==AnzahlKästchenVer and j==AnzahlKästchenHo):
                    neuerPunkt = Eckpunkt((j*100, i*100), RadiusPunkte)

                elif ( (i==1 and (j!=1 and j!=AnzahlKästchenHo)) or ((i!=1 and i!=AnzahlKästchenVer) and j==1) or (i==AnzahlKästchenVer and (j!=1 and j!=AnzahlKästchenHo)) or ((i!=1 and i!=AnzahlKästchenVer) and j==AnzahlKästchenHo)  ):
                    neuerPunkt = Seitenpunkt((j*100, i*100), RadiusPunkte)

                else:
                    neuerPunkt = Innenpunkt((j*100, i*100), RadiusPunkte)

                self.punkte.ElementEinfuegen(j-1,i-1,neuerPunkt)

    def IndicesVonAngeklicktemPunktReturnieren(self, x, y):
        dimsPunkteBitboard = self.punkte.DimensionenReturnieren()
        for i in range(dimsPunkteBitboard[0]):
            for j in range(dimsPunkteBitboard[1]):
                aktuellerPunkt = self.punkte.ElementReturnieren(i, j)
                KoordinatenAktuellerPunkt = aktuellerPunkt.KoordinatenReturnieren()
                if (x>KoordinatenAktuellerPunkt[0]-aktuellerPunkt.Radius and x<KoordinatenAktuellerPunkt[0]+aktuellerPunkt.Radius and y>KoordinatenAktuellerPunkt[1]-aktuellerPunkt.Radius and y<KoordinatenAktuellerPunkt[1]+aktuellerPunkt.Radius):
                    return (i, j)

        return None

    def KordsAngeklicktePunkteReturnieren(self, indizes_paar):
        indizes_Punkt1 = indizes_paar[0]
        indizes_Punkt2 = indizes_paar[1]
        return (self.punkte.ElementReturnieren(indizes_Punkt1[0], indizes_Punkt1[1]).Koordinaten, self.punkte.ElementReturnieren(indizes_Punkt2[0], indizes_Punkt2[1]).Koordinaten)

    def angeklicktePunkteExistierenSchonAlsVerbindung(self, indizes_paar_angeklickter_punkte):
        laenge = self.verbindungen.Laenge()
        for i in range(laenge):
            verbindung = self.verbindungen.ElementReturnieren(i)
            indicesPunkt1Verbindung = verbindung.verbundenerPunkt1Indices
            indicesPunkt2Verbindung = verbindung.verbundenerPunkt2Indices
            indicesPunkt1Angeklickt = indizes_paar_angeklickter_punkte[0]
            indicesPunkt2Angeklickt = indizes_paar_angeklickter_punkte[1]

            punkt1gleich1undpunkt2gleich2 = (indicesPunkt1Verbindung[0]==indicesPunkt1Angeklickt[0] and indicesPunkt1Verbindung[1]==indicesPunkt1Angeklickt[1]) and (indicesPunkt2Verbindung[0]==indicesPunkt2Angeklickt[0] and indicesPunkt2Verbindung[1]==indicesPunkt2Angeklickt[1])
            punkt1gleich2undpunkt2gleich1 = (indicesPunkt1Verbindung[0]==indicesPunkt2Angeklickt[0] and indicesPunkt1Verbindung[1]==indicesPunkt2Angeklickt[1]) and (indicesPunkt2Verbindung[0]==indicesPunkt1Angeklickt[0] and indicesPunkt2Verbindung[1]==indicesPunkt1Angeklickt[1])

            if (punkt1gleich1undpunkt2gleich2 or punkt1gleich2undpunkt2gleich1):
                return True
        return False


    def VerbindungHinzufuegen(self, indicesAngeklickteZweiPunkte, kordsindicesAngeklickteZweiPunkte, spielerID, spielerVerbindungsfarbe):

        v = Verbindung(indicesAngeklickteZweiPunkte[0], indicesAngeklickteZweiPunkte[1], kordsindicesAngeklickteZweiPunkte[0], kordsindicesAngeklickteZweiPunkte[1], spielerID, spielerVerbindungsfarbe)
        self.verbindungen.einreihen(v)

        verbindungenentstandeneneuevierecke = neuespolygongebildet(self.verbindungen, v)
        if verbindungenentstandeneneuevierecke!=None:
            for i in verbindungenentstandeneneuevierecke:
                for j in i:
                    j.Farbe = colors.pretty_green

            if len(verbindungenentstandeneneuevierecke)==1:
                return 1
            elif len(verbindungenentstandeneneuevierecke)==2:
                return 2
        else:
            return 0

    def show(self, screen):
        #show punkte
        AnzahlZeilen, AnzahlSpalten = self.punkte.DimensionenReturnieren()
        for i in range(AnzahlZeilen):
            for j in range(AnzahlSpalten):
                punkt = self.punkte.ElementReturnieren(j, i)
                pygame.draw.circle(screen, punkt.Farbe, punkt.Koordinaten, punkt.Radius)

        #show verbindungen
        Laenge = self.verbindungen.Laenge()
        for i in range(Laenge):
            verbindung = self.verbindungen.ElementReturnieren(i)
            dx = verbindung.kordsVerbundenerPunkt2[0] - verbindung.kordsVerbundenerPunkt1[0]
            dy = verbindung.kordsVerbundenerPunkt2[1] - verbindung.kordsVerbundenerPunkt1[1]

            drawingkords_x = 0
            drawingkords_y = 0
            drawing_width = 10
            drawing_heigth = 10

            if dx==0:
                drawing_heigth = 60
                if dy>0:
                    drawingkords_x = verbindung.kordsVerbundenerPunkt1[0]-5
                    drawingkords_y = verbindung.kordsVerbundenerPunkt1[1]+20

                elif dy<0:
                    drawingkords_x = verbindung.kordsVerbundenerPunkt2[0]-5
                    drawingkords_y = verbindung.kordsVerbundenerPunkt2[1]+20

            elif dy==0:
                drawing_width = 60
                if dx>0:
                    drawingkords_x = verbindung.kordsVerbundenerPunkt1[0]+20
                    drawingkords_y = verbindung.kordsVerbundenerPunkt1[1]-5

                elif dx<0:
                    drawingkords_x = verbindung.kordsVerbundenerPunkt2[0]+20
                    drawingkords_y = verbindung.kordsVerbundenerPunkt2[1]-5

            pygame.draw.rect(screen, verbindung.Farbe, (drawingkords_x, drawingkords_y, drawing_width, drawing_heigth), 0)

class Punkt:
    def __init__(self, Koordinaten, Radius, Farbe):
        self.Koordinaten = Koordinaten
        self.Radius = Radius
        self.Farbe = Farbe

    def KoordinatenReturnieren(self):
        return self.Koordinaten

class Eckpunkt(Punkt):
    def __init__(self, Koordinaten, Radius):
        super().__init__(Koordinaten, Radius, colors.orange_light)
        self.maxVerbindungen = 2

class Seitenpunkt(Punkt):
    def __init__(self, Koordinaten, Radius):
        super().__init__(Koordinaten, Radius, colors.lime)
        self.maxVerbindungen = 3

class Innenpunkt(Punkt):
    maxVerbindungen = 4
    def __init__(self, Koordinaten, Radius):
        super().__init__(Koordinaten, Radius, colors.white)
        self.maxVerbindungen = 4

class Verbindung:
    def __init__(self, verbundenerPunkt1Indices, verbundenerPunkt2Indices, kordsVerbundenerPunkt1, kordsVerbundenerPunkt2, SpielerID, spielerVerbindungsfarbe):
        self.verbundenerPunkt1Indices = verbundenerPunkt1Indices
        self.verbundenerPunkt2Indices = verbundenerPunkt2Indices
        self.kordsVerbundenerPunkt1 = kordsVerbundenerPunkt1
        self.kordsVerbundenerPunkt2 = kordsVerbundenerPunkt2
        self.spielerID = SpielerID
        self.Farbe = spielerVerbindungsfarbe

    def __str__(self):
        return ("[ " + str(self.verbundenerPunkt1Indices) + " , " + str(self.verbundenerPunkt2Indices) + " ]")

class Spieler:
    def __init__(self, ID, Verbindungsfarbe):
        self.Punkte = 0
        self.ID = ID
        self.verbindungsfarbe = Verbindungsfarbe
