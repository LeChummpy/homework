def Ist2MalEnthalten(Eingabe1, Eingabe2):
    liste = Eingabe1
    x = Eingabe2

    Anzahlx = 0
    for i in range(len(liste)):
        if (liste[i]==x):
            Anzahlx=Anzahlx+1

    if Anzahlx>=2:
        return True
    else:
        return False
