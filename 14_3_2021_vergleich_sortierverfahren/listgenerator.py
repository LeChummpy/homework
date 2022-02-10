import random as rd

def generiereListeAufVorsortiert(length):
    liste = []
    for i in range(length):
        liste.append(i+1)
    return liste

def generiereListeAbVorsortiert(length):
    liste = []
    for i in range(length):
        liste.append(length-i)
    return liste

def generiereListeShuffleVorsortiert(length):
    liste = []
    for i in range(length):
        liste.append(i+1)

    for i in range(len(liste)):
        index1 = i
        index2 = rd.randint(0, len(liste)-1)

        element1 = liste[index1]
        element2 = liste[index2]

        liste[index1] = element2
        liste[index2] = element1

    return liste
