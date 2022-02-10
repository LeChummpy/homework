# Autor: J. Ostrzinski
# Datum: 21.08.2018
# Zweck: Klasse Lampe

from turtle import *

class Lampe:
    def __init__(self,x,y,radius,farbe):
        self.__x = x
        self.__y = y
        self.__leuchtet = False
        self.__radius = radius
        self.__farbe = farbe
        self.__bild = Turtle ()
        self.__bild.hideturtle ()
        self.__bild.penup ()
        self.__bild.goto(x,y)
        self.__bild.shape("circle")
        self.__bild.shapesize(radius/10)
        self.__bild.fillcolor("black")
        self.__bild.showturtle ()

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

    def istAn (self):
        return self.__leuchtet
    
        
        
