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
        indicesErsterAngeklickterPunkt = indicesAngeklickteZweiPunkte[0]
        indicesZweiterAngeklickterPunkt = indicesAngeklickteZweiPunkte[1]
        kordsErsterAngeklickterPunkt = kordsindicesAngeklickteZweiPunkte[0]
        kordsZweiterAngeklickterPunkt = kordsindicesAngeklickteZweiPunkte[1]

        if indicesErsterAngeklickterPunkt[0]>indicesZweiterAngeklickterPunkt[0] or (indicesErsterAngeklickterPunkt[0]==indicesZweiterAngeklickterPunkt[0] and indicesErsterAngeklickterPunkt[1]>indicesZweiterAngeklickterPunkt[1]):
            #falls der erste Punkt in der Reihenfolge erst nach dem zweiten angeklickten Punkt kommt, dann werden beide Punkte auch im Tuple getauscht.
            #so ist jede Verbindung eindeutig, was wichtig für das neuronale Netz ist.
            indicesAngeklickteZweiPunkte = (indicesZweiterAngeklickterPunkt, indicesErsterAngeklickterPunkt)
            kordsindicesAngeklickteZweiPunkte = (kordsZweiterAngeklickterPunkt, kordsErsterAngeklickterPunkt)

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
    def __init__(self, AnzahlZeilen, AnzahlSpalten):
        super.__init__()
        self.AnzahlZeilen = AnzahlZeilen
        self.AnzahlSpalten = AnzahlSpalten

        self.sizeInputLayer = AnzahlZeilen*AnzahlSpalten*2
        self.sizeHiddenLayer = int(round(self.sizeInputLayer*1.5, 0))
        self.sizeOutputLayer = 2
        
        self.w_L1 = np.random.rand(sizeHiddenLayer, sizeInputLayer)
        self.w_L2 = np.random.rand(sizeOutputLayer, sizeHiddenLayer)

        self.x = None
        self.z_L2 = None
        self.a_L2 = None
        self.z_L3 = None
        self.a_L3 = None

    def getIndicesOfPointsNextDraw(VerbindungenArray):
        def turnNumbersInTwoIndices(numberArray, anzahl_spalten, anzahl_zeilen):
            pass
        
        self.x = VerbindungArrays.flatten()
        self.z_L2 = np.einsum("i,hi->h", self.x, self.w_L1)
        self.a_L2 = self.sigmoid(self.z_L2)

        self.z_L3 = np.einsum("i,hi->h", self.x, self.w_L2)
        self.a_L3 = self.softmax(self.z_L3)

        out = np.copy(self.a_L3)
        out = out * self.sizeInputLayer
        numpy.around(out, decimals=0)

        return turnNumbersInTwoIndices(out, self.AnzahlSpalten, self.AnzahlZeilen)

    def evaluate(VerbindungenArray, indices):
        #1 connection pattern : 0
        #2 connections pattern : 1
        #3 connections pattern : 2
        #4 connections pattern / sqaure : 3
        #preventing enemy from making square : 4

        #not making 2 connections pattern : -1
        #not making 3 connections pattern : -2
        #not making 4 connections pattern / sqaure : -3
        #not making preventing enemy from making square : -4
        
        #things that don't make sense : -10
        #       -> connection already exists
        #       -> indices are on the same spot
        #       -> indices are diagonal

        pass

    
    def giveFeedback(score):
        '''
        y = None
        stepsize = -0.01
        stepsize = stepsize * score

        dL__dw_L2 = np.dot(2*(self.a_L3-y).transpose(), self.a_L2)
        dL__dw_L1 = 2*(self.a_L3-y).transpose() * self.w_L2 #.....

        w_L1 = w_L1 - stepsize * dL__dw_L1
        w_L2 = w_L2 - stepsize * dL__dw_L2
        '''

    def sigmoid(x):
        return (1 / (1 + np.exp(-x)) )

    def softmax(x):
        return np.exp(x) / sum(np.exp(x))

