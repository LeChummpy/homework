
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
