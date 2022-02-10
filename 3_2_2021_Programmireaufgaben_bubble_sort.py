import math
import random as rd

def bubblesort(liste):
    for h in range(len(liste)): #Wiederhole so oft, wie liste lang ist
        for i in range(len(liste)-1): #gehe liste von Anfang an durch
            wert = liste[i]
            nächster_wert = liste[i+1]
            if (nächster_wert<wert): #Wenn nächster Wert kleiner als aktueller, tausche Werte
                liste[i]=nächster_wert
                liste[i+1]=wert

    return liste

def Abstand(a, b):
    return float(abs(a-b))

def min4(u, x, y, z):
    liste=[u,x,y,z]
    return float(min(liste))

def Nullstelle(p, q):
    #Liefert entsprechende Nullstelle, bei keiner Nullstelle None
    
    try:
        x1 = -(p/2) - math.sqrt((p/2)**2 - q)
        x2 = -(p/2) + math.sqrt((p/2)**2 - q)

        if x1==x2:
            return x2
    
        else:
            return x1, x2
        
    except (ValueError):
        return None

def Extremstelle(a, b, c):

    if (a==0 and b==0):
        return "unendlich"

    elif (a==0 and not(b==0)):
        return None
    
    else:
        x = (-b)/(2*a)
        return x
    
#-----------------------------------------------------------------------------------------------------------

def Nullstelle_v2(a, b, c):
    #Liefert entsprechende Nullstelle, bei keiner Nullstelle None
    
    p = b/a
    q = c/a
    
    try:
        x1 = -(p/2) - math.sqrt((p/2)**2 - q)
        x2 = -(p/2) + math.sqrt((p/2)**2 - q)

        if x1==x2:
            return x2
    
        else:
            return x1, x2
        
    except (ValueError):
        return None

def Extremstelle_v2(a, b, c):
    #liefert näherungsweise Extremstelle von quadratischer Gleichung
    #Extremstelle mit Gradientenverfahren

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
                
            if (abs(g_term)<=1e-15):
                return round(x, 10)


