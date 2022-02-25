
from mainclasses import *
import Stapel
import Bitboard
import PunktVisualisierung
import VerbindungVisualisierung
from turtle import *

def click(x,y):
    indexAngeklickterPunkt = s.IndicesVonAngeklicktemPunktReturnieren(x,y)
    global indicesAngeklickteZweiPunkte
    if indicesAngeklickteZweiPunkte[0]==None:
        indicesAngeklickteZweiPunkte[0] = indexAngeklickterPunkt
    else:
        indicesAngeklickteZweiPunkte[1] = indexAngeklickterPunkt
        if indicesAngeklickteZweiPunkte[1] != None:
            s.VerbindungHinzufuegen(indicesAngeklickteZweiPunkte, 1)
            indicesAngeklickteZweiPunkte = [None, None]

onscreenclick(click)
tracer(0, 0)
eingabe = input("Spielfeldgroeße: ")
eingabe = eingabe.split(", ")
breite = int(eingabe[0])
hoehe = int(eingabe[1])
s = Spielbrett(breite, hoehe, 20)
indicesAngeklickteZweiPunkte = [None, None]
input()
