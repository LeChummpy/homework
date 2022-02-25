import datastructures
import pygame
import colors


class Spielbrett:
    def __init__(self, AnzahlKästchenHo, AnzahlKästchenVer, RadiusPunkte):
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

    def VerbindungHinzufuegen(self, indicesAngeklickteZweiPunkte, kordsindicesAngeklickteZweiPunkte, spielerID, spielerVerbindungsfarbe):

        v = Verbindung(indicesAngeklickteZweiPunkte[0], indicesAngeklickteZweiPunkte[1], kordsindicesAngeklickteZweiPunkte[0], kordsindicesAngeklickteZweiPunkte[1], spielerID, spielerVerbindungsfarbe)
        self.verbindungen.einreihen(v)

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
            pygame.draw.rect(screen, verbindung.Farbe, (verbindung.kordsVerbundenerPunkt1[0], verbindung.kordsVerbundenerPunkt1[1], 10, 10), 1)

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

class Spieler:
    def __init__(self, ID, Verbindungsfarbe):
        self.Punkte = 0
        self.ID = ID
        self.verbindungsfarbe = Verbindungsfarbe
