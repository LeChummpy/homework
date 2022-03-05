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

        verbindunggleichmitrechts = verbindungen.verbindungenthalten(rechts)
        verbindunggleichmithorizintalrechts1 = verbindungen.verbindungenthalten(horizontalrechts1)
        verbindunggleichmithorizintalrechts2 = verbindungen.verbindungenthalten(horizontalrechts2)

        verbindunggleichmitlinks = verbindungen.verbindungenthalten(links)
        verbindunggleichmithorizintallinks1= verbindungen.verbindungenthalten(horizontallinks1)
        verbindunggleichmithorizintallinks2 = verbindungen.verbindungenthalten(horizontallinks2)


        if (verbindunggleichmitrechts!=None and verbindunggleichmithorizintalrechts1!=None and verbindunggleichmithorizintalrechts2!=None) and (verbindunggleichmitlinks!=None and verbindunggleichmithorizintallinks1!=None and verbindunggleichmithorizintallinks2!=None):
            return [(verbindung, verbindunggleichmitrechts, verbindunggleichmithorizintalrechts1, verbindunggleichmithorizintalrechts2), (verbindung, verbindunggleichmitlinks, verbindunggleichmithorizintallinks1, verbindunggleichmithorizintallinks2)]

        elif (verbindunggleichmitrechts!=None and verbindunggleichmithorizintalrechts1!=None and verbindunggleichmithorizintalrechts2!=None):
            return [(verbindung, verbindunggleichmitrechts, verbindunggleichmithorizintalrechts1, verbindunggleichmithorizintalrechts2)]

        elif (verbindunggleichmitlinks!=None and verbindunggleichmithorizintallinks1!=None and verbindunggleichmithorizintallinks2!=None):
            return [(verbindung, verbindunggleichmitlinks, verbindunggleichmithorizintallinks1, verbindunggleichmithorizintallinks2)]

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

        verbindunggleichmitunten = verbindungen.verbindungenthalten(unten)
        verbindunggleichmitvertikalunten1 = verbindungen.verbindungenthalten(vertikalunten1)
        verbindunggleichmitvertikalunten2 = verbindungen.verbindungenthalten(vertikalunten2)

        verbindunggleichmitoben = verbindungen.verbindungenthalten(oben)
        verbindunggleichmitvertikaloben1= verbindungen.verbindungenthalten(vertikaloben1)
        verbindunggleichmitvertikaloben2 = verbindungen.verbindungenthalten(vertikaloben2)

        if (verbindunggleichmitunten!=None and verbindunggleichmitvertikalunten1!=None and verbindunggleichmitvertikalunten2!=None) and (verbindunggleichmitoben!=None and verbindunggleichmitvertikaloben1!=None and verbindunggleichmitvertikaloben2!=None):
            return [(verbindung, verbindunggleichmitunten, verbindunggleichmitvertikalunten1, verbindunggleichmitvertikalunten2), (verbindung, verbindunggleichmitoben, verbindunggleichmitvertikaloben1, verbindunggleichmitvertikaloben2)]

        elif (verbindunggleichmitunten!=None and verbindunggleichmitvertikalunten1!=None and verbindunggleichmitvertikalunten2!=None):
            return [(verbindung, verbindunggleichmitunten, verbindunggleichmitvertikalunten1, verbindunggleichmitvertikalunten2)]

        elif (verbindunggleichmitoben!=None and verbindunggleichmitvertikaloben1!=None and verbindunggleichmitvertikaloben2!=None):
            return [(verbindung, verbindunggleichmitoben, verbindunggleichmitvertikaloben1, verbindunggleichmitvertikaloben2)]

        else:
            return None
