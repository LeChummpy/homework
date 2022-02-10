def istZahlenliste(liste):
    numbers=True
    for i in liste:
        if(isinstance(i, int) or isinstance(i, float)):
            continue
        else:
            numbers=False
            break
    return numbers


def mittel(liste):
    def istZahlenliste(liste):
        numbers=True
        for i in liste:
            if(isinstance(i, int) or isinstance(i, float)):
                continue
            else:
                numbers=False
                break
        return numbers

    if (not(istZahlenliste(liste))): #Wenn liste keine reine Zahlenliste, dann ist None geliefert
        return None

    else: #andernfalls
        summe=0
        for i in liste:
            summe=summe+i
        return summe/len(liste)

def istTypreineliste(liste):
    typ_erstes_element=type(liste[0])
    for i in liste:
        if not(type(i)==typ_erstes_element):
            return False

    return True

def kriterium(a):
    return len(a)



            
