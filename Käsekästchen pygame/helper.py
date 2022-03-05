import datastructures
import mainclasses

def horizontaldervertikalbenachbart(indicesAngeklickteZweiPunkte):
    indicesPunkt1 = indicesAngeklickteZweiPunkte[0]
    indicesPunkt2 = indicesAngeklickteZweiPunkte[1]
    if (indicesPunkt1[0]==indicesPunkt2[0] and (indicesPunkt1[1]+1==indicesPunkt2[1] or indicesPunkt1[1]-1==indicesPunkt2[1])) or ((indicesPunkt1[0]+1==indicesPunkt2[0] or indicesPunkt1[0]-1==indicesPunkt2[0]) and indicesPunkt1[1]==indicesPunkt2[1]):
        return True
    else:
        return False

def neuespolygongebildet(verbindungen, verbindung):
    indicespunkt1 = verbindung.verbundenerPunkt1Indices
    indicespunkt2 = verbindung.verbundenerPunkt2Indices

    dx = verbindung.kordsVerbundenerPunkt2[0] - verbindung.kordsVerbundenerPunkt1[0]
    dy = verbindung.kordsVerbundenerPunkt2[1] - verbindung.kordsVerbundenerPunkt1[1]

    if dx==0: #wenn Verbindung vertikal verläuft
        #zu überprüfende Verbindungen falls Viereck links von Verbindung liegt
        indicespunktrechtsebenepunkt1 = (indicespunkt1[0]+1, indicespunkt1[1])
        indicespunktrechtsebenepunkt2 = (indicespunkt2[0]+1, indicespunkt2[1])

        rechts = mainclasses.Verbindung(indicespunktrechtsebenepunkt1, indicespunktrechtsebenepunkt2, None, None, None, None )
        horizontalrechts1 = mainclasses.Verbindung(indicespunkt1, indicespunktrechtsebenepunkt1, None, None, None, None )
        horizontalrechts2 = mainclasses.Verbindung(indicespunkt2, indicespunktrechtsebenepunkt2, None, None, None, None )

        #Verbindungen falls Viereck rechts von Verbindung liegt
        indicespunktlinksebenepunkt1 = (indicespunkt1[0]-1, indicespunkt1[1])
        indicespunktlinksebenepunkt2 = (indicespunkt2[0]-1, indicespunkt2[1])

        links = mainclasses.Verbindung(indicespunktlinksebenepunkt1, indicespunktlinksebenepunkt2, None, None, None, None )
        horizontallinks1 = mainclasses.Verbindung(indicespunkt1, indicespunktlinksebenepunkt1, None, None, None, None )
        horizontallinks2 = mainclasses.Verbindung(indicespunkt2, indicespunktlinksebenepunkt2, None, None, None, None )

        if (verbindungen.verbindungenthalten(rechts) and verbindungen.verbindungenthalten(horizontalrechts1) and verbindungen.verbindungenthalten(horizontalrechts1)) and (verbindungen.verbindungenthalten(links) and verbindungen.verbindungenthalten(horizontallinks1) and verbindungen.verbindungenthalten(horizontallinks2)):
            return [(verbindung, rechts, horizontalrechts1, horizontalrechts2), (verbindung, links, horizontallinks1, horizontallinks2)]

        elif (verbindungen.verbindungenthalten(rechts) and verbindungen.verbindungenthalten(horizontalrechts1) and verbindungen.verbindungenthalten(horizontalrechts2)):
            return [(verbindung, rechts, horizontalrechts1, horizontalrechts2)]

        elif(verbindungen.verbindungenthalten(links) and verbindungen.verbindungenthalten(horizontallinks1) and verbindungen.verbindungenthalten(horizontallinks2)):
            return [(verbindung, links, horizontallinks1, horizontallinks2)]



        else:
            return None


    elif dy==0: #wenn Verbindung horizontal verläuft
        #zu überprüfende Verbindungen falls Viereck über Verbindung liegt
        indicespunktuntenebenepunkt1 = (indicespunkt1[0], indicespunkt1[1]+1)
        indicespunktuntenebenepunkt2 = (indicespunkt2[0], indicespunkt2[1]+1)

        unten = mainclasses.Verbindung(indicespunktuntenebenepunkt1, indicespunktuntenebenepunkt2, None, None, None, None )
        vertikalunten1 = mainclasses.Verbindung(indicespunkt1, indicespunktuntenebenepunkt1, None, None, None, None )
        vertikalunten2 = mainclasses.Verbindung(indicespunkt2, indicespunktuntenebenepunkt2, None, None, None, None )

        #zu überprüfende Verbindungen falls Viereck unter Verbindung liegt
        indicespunktobenebenepunkt1 = (indicespunkt1[0], indicespunkt1[1]-1)
        indicespunktobenebenepunkt2 = (indicespunkt2[0], indicespunkt2[1]-1)

        oben = mainclasses.Verbindung(indicespunktobenebenepunkt1, indicespunktobenebenepunkt2, None, None, None, None )
        vertikaloben1 = mainclasses.Verbindung(indicespunkt1, indicespunktobenebenepunkt1, None, None, None, None )
        vertikaloben2 = mainclasses.Verbindung(indicespunkt2, indicespunktobenebenepunkt2, None, None, None, None )

        if (verbindungen.verbindungenthalten(unten) and verbindungen.verbindungenthalten(vertikalunten1) and verbindungen.verbindungenthalten(vertikalunten2)) and (verbindungen.verbindungenthalten(oben) and verbindungen.verbindungenthalten(vertikaloben1) and verbindungen.verbindungenthalten(vertikaloben2)):
            return [(verbindung, unten, vertikalunten1, vertikalunten2), (verbindung, oben, vertikaloben1, vertikaloben2)]


        elif (verbindungen.verbindungenthalten(unten) and verbindungen.verbindungenthalten(vertikalunten1) and verbindungen.verbindungenthalten(vertikalunten2)):
            return [(verbindung, unten, vertikalunten1, vertikalunten2)]

        elif (verbindungen.verbindungenthalten(oben) and verbindungen.verbindungenthalten(vertikaloben1) and verbindungen.verbindungenthalten(vertikaloben2)):
            return [(verbindung, oben, vertikaloben1, vertikaloben2)]

        else:
            return None
