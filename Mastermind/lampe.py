# Autor: J. Ostrzinski
# Datum: 03.11.2020
# Zweck: Klasse Lampe

# Die Klasse Lampe dient der Simulation einer zweidimensionalen Lampe im
# Turtle-Grafikfenster, dargestellt als schwarz ausgefüllter Kreis, wenn
# die Lampe aus ist, oder als farbig ausgefüllter Kreis, wenn sie an ist.
# Der Mittelpunkt der Lampe ist bei M(x,y), der Radius ist 'radius'. Mit
# 'farbe' wird ihre Leuchtfarbe angegeben. Dabei muss der Farbstring für
# 'farbe', der beim Instanzieren einer Lampe übergeben werden muss, ein
# gültiger Farbstring des Moduls 'turtle' sein.
# Mit der Instanzierung erscheint die anfangs ausgeschaltete Lampe im
# Grafikfenster.

from turtle import *

class Lampe:

    def __init__(self,x,y,radius,farbe):
        self.__x = x
        self.__y = y
        self.__leuchtet = False
        self.__radius = radius
        self.__farbe = farbe
        self.__bild = Turtle ()
        self.__bild.speed(0)
        self.__bild.hideturtle ()
        self.__bild.penup ()
        self.__bild.goto(x,y)
        self.__bild.shape("circle")
        self.__bild.shapesize(radius/10)
        self.__bild.fillcolor("black")
        self.__bild.showturtle()

    def anschalten (self):
        # Vor.: -
        # Eff.: Die Lampe ist angeschaltet. Ihre Darstellung ist ein ausgefüllter Kreis mit
        #       dem bei der Instanzierung übergegebenen Radius und (evtl. verschobenen)
        #       Mittelpunktskoordinaten im Grafikfenster.
        self.__bild.fillcolor(self.__farbe)
        self.__leuchtet = True

    def ausschalten(self):
        # Vor.: -
        # Eff.: Die Lampe ist ausgeschaltet. Ihre Darstellung ist ein ausgefüllter schwarzer Kreis mit
        #       dem bei der Instanzierung übergegebenen Radius und (evtl. verschobenen)
        #       Mittelpunktskoordinaten im Grafikfenster.
        self.__bild.fillcolor("black")
        self.__leuchtet = False

    def verschieben (self,xneu,yneu):
        # Vor.: 'xneu' und 'yneu' sind int-Werte.
        # Eff.: Die Lampe hat ihre Position verändert, ihr neuer Mittelpunkt hat die Koordinaten 'xneu' und 'yneu'.
        self.__x = xneu
        self.__y = yneu
        self.__bild.goto(xneu,yneu)

    def gibPos (self):
        # Vor.: -
        # Erg.: Die x- und y-Koordinaten der Lampe sind geliefert.
        return self.__x, self.__y

    def gibRadius(self):
        return self.__radius

    def istAn (self):
        # Vor.: -
        # Erg.: True ist geliefert, wenn die Lampe an war. Andernfalls ist False geliefert.
        return self.__leuchtet

    def aendereFarbe(self,farbe):
        # Vor.: 'farbe' ist ein gültiger Farbstring aus dem turtle-Modul
        # Eff.: Die Leuchtfarbe der Lampe ist nun 'farbe'.
        self.__farbe = farbe
        self.__bild.fillcolor(farbe)
