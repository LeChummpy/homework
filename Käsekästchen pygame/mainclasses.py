import datastructures
import pygame
import colors


class Spielbrett:
    def __init__(self, AnzahlKästchenHo, AnzahlKästchenVer, RadiusPunkte):
        self.punkte = datastructures.Bitboard(AnzahlKästchenHo, AnzahlKästchenVer)
        self.verbindungen = datastructures.Stapel()

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

    def show(self, screen):
        AnzahlZeilen, AnzahlSpalten = self.punkte.DimensionenReturnieren()
        for i in range(AnzahlZeilen):
            for j in range(AnzahlSpalten):
                punkt = self.punkte.ElementReturnieren(j, i)
                pygame.draw.circle(screen, punkt.Farbe, punkt.Koordinaten, punkt.Radius)


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
