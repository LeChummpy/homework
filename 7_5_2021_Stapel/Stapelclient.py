from copy import copy
from Stapel import *

def produkt(s):
    erg = 1
    i = copy(s)
    while i.Laenge()!=0:
        erg = erg*i.Top()
        i.Bedienen()
    return erg

def minimum(s):
    i = copy(s)
    minimum = i.Top()
    while i.Laenge()!=0:
        knoten = i.Top()
        if (knoten<minimum):
            minimum = knoten
        i.Bedienen()
    return minimum

def stapelvergleich(s1, s2):
    copy1 = copy(s1)
    copy2 = copy(s2)

    if (copy1.Laenge()!=copy2.Laenge()):
        return False
    else: #Wenn beide Stacks gleiche Länge haben
        while copy1.Laenge()!=0:
            element1 = copy1.Top()
            element2 = copy2.Top()
            if (element1!=element2):
                return False
            copy1.Bedienen()
            copy2.Bedienen()
        return True

def umkehren(s):
    erg = Stapel()
    laenge = s.Laenge()
    for i in range(laenge):
        Kopie = copy(s)
        for j in range(i):
            Kopie.Bedienen()
        erg.Draufpacken(Kopie.Top())
    return erg

s = Stapel()
s.Draufpacken(3)
s.Draufpacken(4)
s.Draufpacken(5)
print(s)
print(umkehren(s))
