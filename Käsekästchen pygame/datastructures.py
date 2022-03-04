class Schlange:
    class __Knoten:
        def __init__(self, e):
            self.element = e
            self.naechster = None

    def __init__(self):
        self.__laenge = 0
        self.__erster = None

    def Laenge(self):
        return self.__laenge

    def gleicht(self, andereSchlange):
        eigeneLaenge = self.__laenge
        andereLange = andereSchlange.Laenge()
        if eigeneLaenge!=andereLange:
            return False
        else:

            for i in range(eigeneLaenge):
                eigenesElementAnIndex = self.ElementReturnieren(i)
                fremdesElementAnIndex = andereSchlange.ElementReturnieren(i)
                if eigenesElementAnIndex!=fremdesElementAnIndex:
                    return False
            return True

    def elemententhalten(self, element):
        eigeneLaenge = self.__laenge
        for i in range(eigeneLaenge):
            eigenesElementAnIndex = self.ElementReturnieren(i)
            if eigenesElementAnIndex==element:
                return True
        return False

    def elementeentsprechensich(self, andereSchlange):
        #print(self, "  ----->   ", andereSchlange)
        eigeneLaenge = self.__laenge
        andereLange = andereSchlange.Laenge()
        #print(eigeneLaenge, " ", andereLange)

        if eigeneLaenge!=andereLange:
            return False
        else:
            for i in range(eigeneLaenge):
                eigenesElementAnIndex = self.ElementReturnieren(i)
                if not(andereSchlange.elemententhalten(eigenesElementAnIndex)):
                    return False
            return True

    def ElementReturnieren(self, index):
        x = self.__erster
        for i in range(index):
            x = x.naechster
        return x.element


    def einreihen(self, e):
        e =  self.__Knoten(e)
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

    def letztesRaus(self):
        if (self.__laenge==1):
            self.__erster = None
            self.__laenge = 0

        elif (self.__laenge>1):
            x = self.__erster
            for i in range(self.__laenge-2):
                x = x.naechster
            x.naechster = None
            self.__laenge -= 1


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
                out += str((x.element))
                if x.naechster != None:
                    out += ", "
                if x.naechster == None:
                    break
                x = x.naechster
        out += " ]"
        return out


class Bitboard:
    class __Kontrollblock:
        def __init__(self):
            self.naechsterKontrollblock = None
            self.ersterInhaltsblock = None

    class __Inhaltsblock:
        def __init__(self):
            self.naechsterInhaltsblock = None
            self.inhalt = None

    def __init__(self, AnzahlSpalten, AnzahlZeilen):
        self.AnzahlSpalten = AnzahlSpalten
        self.AnzahlZeilen = AnzahlZeilen

        self.obersterKontrollblock = self.__Kontrollblock()
        x = self.obersterKontrollblock
        for i in range(AnzahlZeilen):

            x.ersterInhaltsblock = self.__Inhaltsblock()
            y = x.ersterInhaltsblock
            for j in range(AnzahlSpalten-1):

                m = self.__Inhaltsblock()
                y.naechsterInhaltsblock = m
                y = y.naechsterInhaltsblock

            n = self.__Kontrollblock()
            x.naechsterKontrollblock = n
            x = n

    def ElementEinfuegen(self, spaltenindex, zeilenindex, inhalt):
        x = self.obersterKontrollblock
        for i in range(zeilenindex):
            x = x.naechsterKontrollblock

        y = x.ersterInhaltsblock
        for j in range(spaltenindex):
            y = y.naechsterInhaltsblock

        y.inhalt = inhalt

    def ElementReturnieren(self, spaltenindex, zeilenindex):
        x = self.obersterKontrollblock
        for i in range(zeilenindex):
            x = x.naechsterKontrollblock

        y = x.ersterInhaltsblock
        for j in range(spaltenindex):
            y = y.naechsterInhaltsblock

        return y.inhalt

    def __str__(self):
        erg = ""
        x = self.obersterKontrollblock
        while x != None:
            erg_oneline = " "
            y = x.ersterInhaltsblock
            while y != None:
                erg_oneline = erg_oneline[:-1] + str(y.inhalt) + " "  + erg_oneline[-1:]
                y = y.naechsterInhaltsblock
            if (erg_oneline != " "):
                erg += "{" + erg_oneline + "}\n"
            x = x.naechsterKontrollblock
        return erg

    def DimensionenReturnieren(self):
        return (self.AnzahlSpalten, self.AnzahlZeilen)
