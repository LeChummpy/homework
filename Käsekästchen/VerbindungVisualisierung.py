from turtle import *

class VerbindungVisualisierung:

    def __init__(self,x1,y1,x2,y2,farbe):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        dx = x1 - x2
        dy = y1 - y2

        self.__leuchtet = False
        self.__radius = radius
        self.__farbe = farbe
        self.__bild = Turtle()
        self.__bild.speed(0)
        self.__bild.hideturtle ()
        self.__bild.penup ()
        self.__bild.goto(x1,y1)
        self.__bild.pendown ()
        self.__bild.fillcolor(farbe)
        self.__bild.width(10)
        self.__bild.forward(dx)
        self.__bild.forward(dy)

    def anschalten (self):
        self.__bild.fillcolor(self.__farbe)
        self.__leuchtet = True

    def ausschalten(self):
        self.__bild.fillcolor("black")
        self.__leuchtet = False

    def verschieben (self,xneu,yneu):
        self.__x = xneu
        self.__y = yneu
        self.__bild.goto(xneu,yneu)

    def gibPos (self):
        return self.__x, self.__y

    def gibRadius(self):
        return self.__radius

    def istAn (self):
        return self.__leuchtet

    def aendereFarbe(self,farbe):
        self.__farbe = farbe
        self.__bild.fillcolor(farbe)
