def horizontaldervertikalbenachbart(indicesAngeklickteZweiPunkte):
    indicesPunkt1 = indicesAngeklickteZweiPunkte[0]
    indicesPunkt2 = indicesAngeklickteZweiPunkte[1]
    if (indicesPunkt1[0]==indicesPunkt2[0] and (indicesPunkt1[1]+1==indicesPunkt2[1] or indicesPunkt1[1]-1==indicesPunkt2[1])) or ((indicesPunkt1[0]+1==indicesPunkt2[0] or indicesPunkt1[0]-1==indicesPunkt2[0]) and indicesPunkt1[1]==indicesPunkt2[1]):
        return True
    else:
        return False


#def neuespolygongebildet(verbindungen):
