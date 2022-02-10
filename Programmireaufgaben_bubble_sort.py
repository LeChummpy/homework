import random as rd
import math

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
        
    except (ValueError):
        return None

    return x1, x2

def Extremstelle(a, b, c):
    #liefert Extremstelle auf zehnte Kommastelle gerundet
    
    schrittweite = 0.001
    x = 1
    if (a>0):
        while True:
            g_term = schrittweite * (2*a*x + b)
            x -= g_term
            if (abs(g_term)<=1e-13):
                return round(x, 10)
            
    elif (a<0):
        while True:
            g_term = schrittweite * (2*a*x + b)
            x += g_term
            if (abs(g_term)<=1e-13):
                return round(x, 10)

def Nullstelle_v2(a, b, c):
    #Nullstellen mit Gradientenverfahren finden (Gradientenverfahren, um 1/3a + 1/2bx^2 + cx zu minimieren --> Nullstellen) 
    
    def getExtremstelle(X, a, b, c):
        schrittweite = 0.001
        x = X

        if (a>0):
            while True:
                g_term = schrittweite * (a*(x**2) + b*x + c)
                x -= g_term
                if (abs(g_term)<=1e-13):
                    return round(x, 10)
                
        elif (a<0):
            while True:
                g_term = schrittweite * (a*(x**2) + b*x + c)
                x += g_term
                if (abs(g_term)<=1e-13):
                    return round(x, 10)

    
    if (b==0 and c==0): #Wenn eine Nullstelle
        return 0
        
    else: #Wenn zwei Nullstellen
        Nullstellen=[]
        Nullstellen.append(getExtremstelle(1, a, b, c))

        suchbereich=1
        while True: #Suche zweite Nullstelle
            suchbereich=suchbereich*2
            for i in range(10):
                x=rd.randint(-suchbereich, suchbereich)
                potenzielle_Nullstelle=getExtremstelle(x, a, b, c)

            print(str(suchbereich) + " --> " + str(Nullstellen))


            

    

