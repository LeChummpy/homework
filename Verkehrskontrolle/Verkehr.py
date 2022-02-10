import Schlange

def LKWnotieren(Verkehrskontrolle):
    out = []

    while Verkehrskontrolle.Laenge()!=0:
        if Verkehrskontrolle.ErsterFahrzeugtyp()=="L":
            out.append(Verkehrskontrolle.ErstesFahrzeugkfz())
        Verkehrskontrolle.Schlangeverlassen()

    return out

v = Schlange.Verkehrskontrolle()
v.einreihen("kfz", "PKW", True)
v.einreihen("kfz2", "PKW", False)
v.einreihen("lkw", "L", False)
v.einreihen("kfz3", "PKW", False)
v.einreihen("lkw1", "L", False)
