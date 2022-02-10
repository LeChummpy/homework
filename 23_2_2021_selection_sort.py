import math

def selectionsort(liste):

    def minimum(liste, x):
        #returns tuple of minimum in liste[x:len(liste)] and index of minimum
        kandidat = (liste[x], x)
        for i in range(x, len(liste)):
            if (liste[i]<kandidat[0]):
                kandidat = (liste[i], i)

        return kandidat

    sorted_partition = []
    for i in range(len(liste)):
        min_tuple = minimum(liste, i)
        liste[min_tuple[1]] = liste[i]
        liste[i] = min_tuple[0]

    return liste

def Nullstellen(a, b, c, d):

    def holzweiteNullstelle(a, b, c):
        if (a==0):
            if (b==0 and c!=0):
                return None

            elif (b==0 and c==0):
                return "unendlich"

        else:
            p = b/a
            q = c/a

            try:
                x = -(p/2) - math.sqrt((p/2)**2 - q)
                return x
            except (ValueError):
                return None

    def holdritteNullstelle(a, b, c):
        if (a==0):
            if (b==0 and c!=0):
                return None

            elif (b==0 and c==0):
                return "unendlich"

        else:
            p = b/a
            q = c/a

            try:
                x = -(p/2) + math.sqrt((p/2)**2 - q)
                return x
            except (ValueError):
                return None


    def MaximaStammfunktion(a, b, c, d, startwert):
        x = startwert
        schrittweite = 0.001
        while True:
            g_term = schrittweite * (a*(x**3) + b*(x**2) + c*x + d)
            x += g_term
            if (abs(g_term)<=1e-12):
                return round(x, 15)

    def MinimaStammfunktion(a, b, c, d, startwert):
        x = startwert
        schrittweite = 0.001
        while True:
            g_term = schrittweite * (a*(x**3) + b*(x**2) + c*x + d)
            x -= g_term
            if (abs(g_term)<=1e-12):
                return round(x, 15)

    def finde1Nullstelle(a, b, c, d):
        if (a>0):
            x = MinimaStammfunktion(a, b, c, d, 1)
            return x
        elif (a<0):
            x = MaximaStammfunktion(a, b, c, d, 1)
            return x

    if (a==0): #verhält sich wie quadratische Funktion
        return (holersteNullstelle(b, c, d), holzweiteNullstelle(b, c, d))

    else:
        x1 = finde1Nullstelle(a, b, c, d) #eine Nullstelle mit Gradientenverfahren näherungsweise berechnen, nun mit Hornaverfahern weitere Nullstellen berechnen
        # die nächsten zwei Nullstellen mit Horner-Verfahren, sehr ungenau deswegen sehr ungenaue Werte :(
        _a= a
        _b = a*x1+b
        _c = (a*x1+b)*x1+c
        _d = ((a*x1+b)*x1+c)*x1+d #zum gegenchecken ob null oder nähreungsweise 0

        x2 = holzweiteNullstelle(_a, _b, _c)
        x3 = holdritteNullstelle(_a, _b, _c)
        return [x1, x2, x3]

#sorry deutlich ausbaufähig die letzte
