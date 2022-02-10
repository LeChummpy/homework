#maty dein passwort ist einfach zu leicht

class Verkehrskontrolle:
    class __Knoten:
        def __init__(self, kfz, typ, tauglich):
            self.kfz = kfz
            self.typ = typ
            self.tauglich = tauglich
            self.naechster = None

    def __init__(self):
        self.__laenge = 0
        self.__erster = None

    def Laenge(self):
        return self.__laenge

    def ErstesFahrzeugkfz(self):
        return self.__erster.kfz

    def ErsterFahrzeugtyp(self):
        return self.__erster.typ

    def einreihen(self, kfz, typ, tauglich):
        e =  self.__Knoten(kfz, typ, tauglich)
        x = self.__erster
        if x != None:
            while True:
                if x.naechster == None:
                    break
                x = x.naechster
            x.naechster = e
        else:
            self.__erster = e

        self.__laenge += 1

    def Schlangeverlassen(self):
        self.__erster = self.__erster.naechster

        self.__laenge -= 1

    def vorziehen(self, n):
        '''
        Vorr.: -n- darf nicht 0 sein und darf die Anzahl der Elemente in der Schlange um 1
               vermindert nicht überschreiten.
        Eff.: Das Element der Schlange an -n-ter Stelle ist nun an den Beginn der Schlange vorgezogen.
        '''
        x_minus_1 = self.__erster
        x = self.__erster
        for i in range(n):
            x = x.naechster
        for i in range(n-1):
            x_minus_1 = x_minus_1.naechster
        
        x_minus_1.naechster = x.naechster
        x.naechster = self.__erster
        self.__erster = x
            

    def __str__(self):
        out = "[ "
        x = self.__erster
        if x != None:
            while True:
                out += str((x.kfz, x.typ, x.tauglich))
                if x.naechster != None:
                    out += ", "
                if x.naechster == None:
                    break
                x = x.naechster
        out += " ]"
        return out





