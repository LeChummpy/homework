from schlangenimpl import *
from copy import copy

def produkt(s):
    copy = copy(s)
    x = 1
    while not(copy.IstLeer()):
        x = x * copy.Kopf()
        copy.Bedienen()
    return x

def minimum(s):
    copy = copy(s)
    minimum = s.Kopf()
    while not(copy.IstLeer()):
        aktuellerWert = copy.Kopf()
        if (aktuellerWert<minimum):
            minimum = aktuellerWert
        copy.Bedienen()
    return minimum

def Schlangenvergleich(s1, s2):
    s1Copy = copy(s1)
    s2Copy = copy(s2)
    if (s1Copy.Laenge()==s2Copy.Laenge()):
        while not(s1Copy.IstLeer()):
            werts1 = s1Copy.Kopf()
            werts2 = s2Copy.Kopf()
            if (werts1!=werts2):
                return False
            s1Copy.Bedienen()
            s2Copy.Bedienen()
        return True

    else:
        return False

def umkehren(s):
    erg = Schlange()
    for i in range(s.Laenge()):
        aktuellerIndex = s.Laenge() - i

        Kopie = copy(s)
        for j in range(aktuellerIndex-1):
            Kopie.Bedienen()
        erg.Einreihen(Kopie.Kopf())

    return (erg)

s = Schlange()
s.Einreihen(1)
s.Einreihen(2)
s.Einreihen(3)
