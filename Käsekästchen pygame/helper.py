import datastructures
from copy import *

def horizontaldervertikalbenachbart(indicesAngeklickteZweiPunkte):
    indicesPunkt1 = indicesAngeklickteZweiPunkte[0]
    indicesPunkt2 = indicesAngeklickteZweiPunkte[1]
    if (indicesPunkt1[0]==indicesPunkt2[0] and (indicesPunkt1[1]+1==indicesPunkt2[1] or indicesPunkt1[1]-1==indicesPunkt2[1])) or ((indicesPunkt1[0]+1==indicesPunkt2[0] or indicesPunkt1[0]-1==indicesPunkt2[0]) and indicesPunkt1[1]==indicesPunkt2[1]):
        return True
    else:
        return False

def returniereAlleVerbundenenPunkte(verbindungen, punktIndizes):
    indizesVerbundenePunkte = datastructures.Schlange()
    leange = verbindungen.Laenge()
    for i in range(leange):
        v = verbindungen.ElementReturnieren(i)
        if v.verbundenerPunkt1Indices[0]==punktIndizes[0] and v.verbundenerPunkt1Indices[1]==punktIndizes[1]:
            indizesVerbundenePunkte.einreihen(v.verbundenerPunkt2Indices)

        elif v.verbundenerPunkt2Indices[0]==punktIndizes[0] and v.verbundenerPunkt2Indices[1]==punktIndizes[1]:
            indizesVerbundenePunkte.einreihen(v.verbundenerPunkt1Indices)
    return indizesVerbundenePunkte


def neuespolygongebildet(verbindungen, verbindung, insgesamtBereitsÜberlaufenePfade):

    def punktinpunkteschlange(punkt, gegangenePunkte):
        laenge = gegangenePunkte.Laenge()
        for i in range(laenge):
            x = gegangenePunkte.ElementReturnieren(i)
            if x[0]==punkt[0] and x[1]==punkt[1]:
                return True
        return False

    def pfadInAbgelaufenenPfade(pfad, listeAbgelaufenePfade):
        for i in listeAbgelaufenePfade:
            if pfad.elementeentsprechensich(i):
                return True
        return False

    def einenPunktWeiter(punkt, startpunkt, gegangenePunkte, bereitsÜberlaufenePfade):
        gegangenePunkte.einreihen(punkt)
        verbundenePunkte = returniereAlleVerbundenenPunkte(verbindungen, punkt)

        laenge = verbundenePunkte.Laenge()
        for i in range(laenge): #alle verbundenen Punkte durchgehen
            p = verbundenePunkte.ElementReturnieren(i)
            if p[0]==startpunkt[0] and p[1]==startpunkt[1] and (gegangenePunkte.Laenge()==4) : #wenn man erneut bei Startpunkt angelangt #and not(ueberpruefeObPunktInPunktschlange(punkt, benachbartePunkteAnfangspunkt)
                if not(pfadInAbgelaufenenPfade(gegangenePunkte, insgesamtBereitsÜberlaufenePfade)):
                    #print("Pfad gefunden! ", gegangenePunkte, " --------> ", insgesamtBereitsÜberlaufenePfade)
                    neuergegangenerpfad = copy(gegangenePunkte)
                    bereitsÜberlaufenePfade.append(neuergegangenerpfad)
                    print(bereitsÜberlaufenePfade[0], "  ", bereitsÜberlaufenePfade[1])

            if not(punktinpunkteschlange(p,  gegangenePunkte)):
                 einenPunktWeiter(p, startpunkt, gegangenePunkte, bereitsÜberlaufenePfade)

        gegangenePunkte.letztesRaus()


    startpunkt = verbindung.verbundenerPunkt1Indices
    gegangenePunkte = datastructures.Schlange()
    bereitsÜberlaufenePfade = []
    einenPunktWeiter(startpunkt, startpunkt, gegangenePunkte, bereitsÜberlaufenePfade)
    return bereitsÜberlaufenePfade
