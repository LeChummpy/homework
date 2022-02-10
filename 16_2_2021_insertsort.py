import math
def insertsort(liste):
    def getnewIndex(liste, n, old_index):
        arrea_to_sort_in = liste[0:old_index]
        if old_index == 0:
            return 0
        elif old_index == 1:
            if liste[old_index-1] > n:
                return 0
            else:
                return 1
        else:
            for i in range(len(arrea_to_sort_in)):
                if arrea_to_sort_in[i] > n:
                    return i
            return old_index

    for i in range(len(liste)):
        n = liste[i] #aktuelles Element

        old_index = i
        new_index = getnewIndex(liste, n, old_index)
        liste.pop(old_index)
        liste.insert(new_index, n)

    return liste

def insertsort2(liste):
    liste_2 = []
    for i in range(len(liste)):
        wert = liste[i]
        if (i==0):
            liste_2.append(wert)
        else:
            stelle_gefunden = False
            for j in range(len(liste_2)):
                if liste_2[j] > wert:
                    liste_2.insert(j, wert)
                    stelle_gefunden = True
                    break

            if stelle_gefunden == False:
                liste_2.append(wert)

    return liste_2

def Scheitelpunkt(a, b, c):

    if (a==0 and b==0):
        return "unendlich"

    elif (a==0 and not(b==0)):
        return None

    else:
        x = (-b)/(2*a)
        return float(round(x, 10))

def Scheitelpunkt_v2(a, b, c):
    if (a==0 and b==0):
        return "unendlich"

    elif (a==0 and not(b==0)):
        return None

    else:
        schrittweite = 0.001
        x = 1
        while True:
            g_term = schrittweite * (2*a*x + b)
            if (a>0):
                x -= g_term
            elif (a<0):
                x += g_term

            if (g_term<=1e-15):
                return float(round(x, 10))

def Nullstellen(a, b, c):
    if (a==0):
        return None

    else:
        p = b/a
        q = c/a

        try:
            x1 = -(p/2) - math.sqrt((p/2)**2 - q)
            x2 = -(p/2) + math.sqrt((p/2)**2 - q)

            if x1==x2:
                return [float(x2)]

            else:
                return [float(x1), float(x2)]

        except (ValueError):
            return None
