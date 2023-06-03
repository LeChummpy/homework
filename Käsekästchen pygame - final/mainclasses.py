import datastructures
import pygame
import colors
from helper import *
import numpy as np

class Spielbrett:
    def __init__(self, AnzahlKästchenHo, AnzahlKästchenVer, RadiusPunkte):
        #Vor.: -AnzahlKästchenHo-, -AnzahlKästchenVer- und -RadiusPunkte- sind Integer
        #Eff.: Eine neue Objektinstanz der Klasse Spielbrett mit einer Höhe von -AnzahlKästchenVer- Punkten und einer Breite von -AnzahlKästchenHo- Punkten ist erzeugt.
        self.AnzahlKästchenHo = AnzahlKästchenHo
        self.AnzahlKästchenVer = AnzahlKästchenVer
        self.punkte = datastructures.Bitboard(AnzahlKästchenHo, AnzahlKästchenVer)
        self.verbindungen = datastructures.Schlange()

        for i in range(1, AnzahlKästchenVer+1):
            innereliste = []
            for j in range(1, AnzahlKästchenHo+1):
                neuerPunkt = None

                #ein Eckpunkt mit der Farbe "helles Orange" wird erzeugt
                if (i==1 and j==1) or (i==1 and j==AnzahlKästchenHo) or (i==AnzahlKästchenVer and j==1) or (i==AnzahlKästchenVer and j==AnzahlKästchenHo):
                    neuerPunkt = Punkt((j*100, i*100), RadiusPunkte, colors.orange_light)

                #ein Seitenpunkt mit der Farbe "Weiß" wird erzeugt
                elif ( (i==1 and (j!=1 and j!=AnzahlKästchenHo)) or ((i!=1 and i!=AnzahlKästchenVer) and j==1) or (i==AnzahlKästchenVer and (j!=1 and j!=AnzahlKästchenHo)) or ((i!=1 and i!=AnzahlKästchenVer) and j==AnzahlKästchenHo)  ):
                    neuerPunkt = Punkt((j*100, i*100), RadiusPunkte, colors.white )

                #ein Innenpunkt mit der Farbe "Olivgrün" wird erzeugt
                else:
                    neuerPunkt = Punkt((j*100, i*100), RadiusPunkte, colors.lime)

                self.punkte.ElementEinfuegen(j-1,i-1,neuerPunkt)

    def IndicesVonAngeklicktemPunktReturnieren(self, x, y):
        #Vor.: -x- und -y- sind Integer
        #Erg.: Falls ein Punkt es einen Punkt gibt, der auf den angeklickten Koordinanten liegt, sind
        #      die Indices des angeklickten Punktes geliefert. Andernfalls ist None geliefert
        dimsPunkteBitboard = self.punkte.DimensionenReturnieren()
        for i in range(dimsPunkteBitboard[0]):
            for j in range(dimsPunkteBitboard[1]):
                aktuellerPunkt = self.punkte.ElementReturnieren(i, j)
                KoordinatenAktuellerPunkt = aktuellerPunkt.Koordinaten
                if (x>KoordinatenAktuellerPunkt[0]-aktuellerPunkt.Radius and x<KoordinatenAktuellerPunkt[0]+aktuellerPunkt.Radius and y>KoordinatenAktuellerPunkt[1]-aktuellerPunkt.Radius and y<KoordinatenAktuellerPunkt[1]+aktuellerPunkt.Radius):
                    return (i, j)

        return None

    def KordsAngeklicktePunkteReturnieren(self, indizes_paar):
        #Vor.: -indizes_paar- ist ein 2-elementiges Tuple, dessen Elemente 2-elementige Tuples sind. Sie entsprechen
        #      den Indices zweier Punkte, die i.d.R. eine Verbindung bilden.
        #Erg.: Die Koordinaten der Punkte, auf die die Punktindizes verweisen, ist geliefert.
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


    def VerbindungHinzufügen(self, indicesAngeklickteZweiPunkte, kordsindicesAngeklickteZweiPunkte, spielerID, spielerVerbindungsfarbe):
        #Vor.: -indicesAngeklickteZweiPunkte- und -kordsindicesAngeklickteZweiPunkte- sind  2-elementige Tuples bestehend aus 2-elementigen Tuples, -spielerID- ist
        #      ein Integer und -spielerVerbindungsfarbe- ist ein 3-elementiger Tuple (R,G,B)
        #Erg.: Die Koordinaten der Punkte, auf die die Punktindizes verweisen, ist geliefert.
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
        #Vor.:
        #Eff.: Alle Bestandteile der Spielrunde sind auf dem Bildschirm gezeichnet.
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
        #Vor.: -Koordinaten- ist ein 2-elementiger Tuple, Farbe ist ein 3-elementiger Tuple (R,G,B) und Radius ist ein Integer
        #Eff.: Eine neue Objektinstanz der Klasse Punkt mit den Koordinanten -Koordinaten-, dem Radius -Radius- und der Farbe -Farbe- ist erzeugt.
        self.Koordinaten = Koordinaten
        self.Radius = Radius
        self.Farbe = Farbe

class Verbindung:
    def __init__(self, verbundenerPunkt1Indices, verbundenerPunkt2Indices, kordsVerbundenerPunkt1, kordsVerbundenerPunkt2, SpielerID, spielerVerbindungsfarbe):
        #Vor.: -verbundenerPunkt1Indices-, -verbundenerPunkt1Indices-, -kordsVerbundenerPunkt1- und -kordsVerbundenerPunkt2- sind 2-elementige Tuples, -SpielerID-
        #      ist ein Integer und spielerVerbindungsfarbe ist ein 3-elementiger Tuple (R,G,B)
        #Eff.: Eine neue Objektinstanz der Klasse Verbindung vom Punkt mit Index -verbundenerPunkt1Indices- und Koordinanten -kordsVerbundenerPunkt1-
        #      zum Punkt mit Index -verbundenerPunkt2Indices- und Koordinanten -kordsVerbundenerPunkt2- ist erzeugt.
        self.verbundenerPunkt1Indices = verbundenerPunkt1Indices
        self.verbundenerPunkt2Indices = verbundenerPunkt2Indices
        self.kordsVerbundenerPunkt1 = kordsVerbundenerPunkt1
        self.kordsVerbundenerPunkt2 = kordsVerbundenerPunkt2
        self.spielerID = SpielerID
        self.Farbe = spielerVerbindungsfarbe

    def __str__(self):
        #Vor.: -
        #Erg.: Ein String, der die Indices der beiden Verbindungspunkte der Verbindung repräsentiert, ist geliefert.
        return ("[ " + str(self.verbundenerPunkt1Indices) + " , " + str(self.verbundenerPunkt2Indices) + " ]")

class Spieler:
    def __init__(self, ID, Verbindungsfarbe):
        #Vor.: -ID- ist ein Integer und -Verbindungsfarbe- ist ein 3-elementiger Tuple (R,G,B)
        #Eff.: Eine neue Objektinstanz der Klasse Spieler mit der ID -ID-, der Verbindungsfarbe -Verbindungsfarbe- und zunächst 0 Punkten ist erzeugt.
        self.Punkte = 0
        self.ID = ID
        self.verbindungsfarbe = Verbindungsfarbe

class SpielerKI(Spieler): #Q-Learning Implementierung
    def __init__(self):
        super.__init__()

    def getFeedback(points):
        pass

    def getState(current_Spielbrett):
        pass
        
    def setNextMove(self):
        pass
