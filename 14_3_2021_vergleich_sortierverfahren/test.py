import listgenerator as rg
import timer as tm
import sortierverfahren

def testen(liste):
    Timer = tm.timer()

    '''
    Timer.start()
    sortierverfahren.bubblesort(liste)
    time = Timer.stop()
    print("Bubblesort: " + str(time))

    Timer.start()
    sortierverfahren.insertsort(liste)
    time = Timer.stop()
    print("Insertsort: " + str(time))
    '''

    Timer.start()
    sortierverfahren.selectsort(liste)
    time = Timer.stop()
    print("Selectsort: " + str(time))

    '''
    Timer.start()
    sortierverfahren.mergesort(liste)
    time = Timer.stop()
    print("Mergesort: " + str(time))
    '''
    print("")

laenge_liste = 25000

print("----------------Aufsteigend-----------------")
liste_auf_vorsortiert = rg.generiereListeAufVorsortiert(laenge_liste)
testen(liste_auf_vorsortiert)

print("----------------Absteigend-----------------")
liste_ab_vorsortiert = rg.generiereListeAbVorsortiert(laenge_liste)
testen(liste_ab_vorsortiert)

print("----------------Shuffled-----------------")
liste_shuffle_vorsortiert = rg.generiereListeShuffleVorsortiert(laenge_liste)
testen(liste_shuffle_vorsortiert)
