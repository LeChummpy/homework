class Schlange:
    class __Knoten:
        def __init__(self, e):
            self.element = e
            self.naechster = None

    def __init__(self):
        #Vor.: -
        #Eff.: Eine Objektinstanz der Klasse Schlange ist erzeugt. Die Schlange ist zunächst leer.
        self.__laenge = 0
        self.__erster = None
        self.asInputArray = None

    def Laenge(self):
       #Vor.: keine
       #Erg.: Die Länge der Schlange/die Anzahl der Elemente ist als Integer geliefert.
        return self.__laenge

    def ElementReturnieren(self, index):
        #Vor.: Die Schlange hat eine Länge von -index- plus 1 Elementen
        #Erg.: Das Element mit dem Index -index- ist geliefert.
        x = self.__erster
        for i in range(index):
            x = x.naechster
        return x.element

    def verbindungenthalten(self, v):
        #Vor.: -v- ist eine Objektinstanz der Klasse Verbindung.
        #Erg.: Falls die Verbindung als Element im Bitboard mindestens
        #      einmal enthalten ist, ist die erste in der Schlange auftauchende
        #      Verbindung, die v gleicht, als 2-elementiger Tuple (der aus 2-elementigen
        #      Tuples besteht) geliefert. Andernfalls ist False geliefert.
        for i in range(self.__laenge):
            vschlange = self.ElementReturnieren(i)
            if (v.verbundenerPunkt1Indices[0]==vschlange.verbundenerPunkt1Indices[0] and v.verbundenerPunkt1Indices[1]==vschlange.verbundenerPunkt1Indices[1]) and (v.verbundenerPunkt2Indices[0]==vschlange.verbundenerPunkt2Indices[0] and v.verbundenerPunkt2Indices[1]==vschlange.verbundenerPunkt2Indices[1]):
                    return vschlange
            elif (v.verbundenerPunkt2Indices[0]==vschlange.verbundenerPunkt1Indices[0] and v.verbundenerPunkt2Indices[1]==vschlange.verbundenerPunkt1Indices[1]) and (v.verbundenerPunkt1Indices[0]==vschlange.verbundenerPunkt2Indices[0] and v.verbundenerPunkt1Indices[1]==vschlange.verbundenerPunkt2Indices[1]):
                    return vschlange
        return None

    def einreihen(self, e):
        #Vor.: -
        #Eff.: Ein Element -e- (z.B. Vebindung, kann aber auch ein anderes Objekt sein)
        #      wird am Ende der Schlange angehangen.
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

        self.update_asInputArray()

    def letztesRaus(self):
        #Vor.: Mindestens ein Element ist in der Schlange
        #Eff.: Das letzte Element ist aus der Schlange entfernt.
        if (self.__laenge==1):
            self.__erster = None
            self.__laenge = 0

        elif (self.__laenge>1):
            x = self.__erster
            for i in range(self.__laenge-2):
                x = x.naechster
            x.naechster = None
            self.__laenge -= 1

        self.update_asInputArray()

    def Schlangeverlassen(self):
        #Vor.: Mindestens ein Element ist in der Schlange
        #Eff.: Das erste Element ist aus der Schlange entfernt.
        self.__erster = self.__erster.naechster
        self.__laenge -= 1

        self.update_asInputArray()

    def vorziehen(self, n):
        #Vor.: -n- darf nicht 0 sein und darf die Anzahl der Elemente in der Schlange
        #      minus 1 nicht überschreiten
        #Eff.: Das Element der Schlange an -n-ter Stelle ist nun an den Beginn der Schlange vorgezogen.

        x_minus_1 = self.__erster
        x = self.__erster
        for i in range(n):
            x = x.naechster
        for i in range(n-1):
            x_minus_1 = x_minus_1.naechster

        x_minus_1.naechster = x.naechster
        x.naechster = self.__erster
        self.__erster = x

        self.update_asInputArray()

    def update_asInputArray(self):
        array = []
        for i in range(self.__laenge):
            vschlange = self.ElementReturnieren(i)
            array.append([vschlange.verbundenerPunkt1Indices, vschlange.verbundenerPunkt2Indices])

        self.asInputArray = np.array(array).flatten()


    def __str__(self):
        #Vor.: -
        #Erg.: Ein String, der den Inhalt der Schlange eindimensional repräsentiert, ist geliefert.
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
        #Vor.:: -AnzahlSpalten- und -AnzahlZeilen- sind Integer größer als 1.
        #Eff.: Eine Objektinstanz der Klasse Bitboard wird erstellt. Bitboard ist eine Datenstruktur,
        #      die zweidimensionale Schlangen repräsentiert (jedes Element der Schlange ist eine Schlange).
        #      Die Länge der Schlangen (Kontrollblock) in der Hauptschlange ist hierbei stets gleich.
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
        #Vor.: Das Bitboard hat beinhaltet bereits -spaltenindex- minus 1 Schlangen mit einer Länge von jeweils -zeilenindex- minus 1 Elementen.
        #Eff. Ein Elment an horizontalem Index -spaltenindex- und vertikalem Index -zeilenindex- wird in das Bitboard eingefügt.
        x = self.obersterKontrollblock
        for i in range(zeilenindex):
            x = x.naechsterKontrollblock

        y = x.ersterInhaltsblock
        for j in range(spaltenindex):
            y = y.naechsterInhaltsblock

        y.inhalt = inhalt

    def ElementReturnieren(self, spaltenindex, zeilenindex):
        #Vor.: Das Bitboard hat eine Höhe von -zeilenindex- Elementen und eine Breite von -spaltenindex- Elementen
        #Erg.: Das Element mit Spaltenindex -spaltenindex- und Zeilenindex -zeilenindex- ist geliefert.
        x = self.obersterKontrollblock
        for i in range(zeilenindex):
            x = x.naechsterKontrollblock

        y = x.ersterInhaltsblock
        for j in range(spaltenindex):
            y = y.naechsterInhaltsblock

        return y.inhalt

    def __str__(self):
        #Vor.: -
        #Erg.: Ein String, der den Inhalt des Bitboardes zweidimensional repräsentiert, ist geliefert.
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
        #Vor.: -
        #Erg.: Die Dimensionen des Bitboards (Höhe, Breite) sind als 2-elementiger Tuple geliefert.
        return (self.AnzahlSpalten, self.AnzahlZeilen)
