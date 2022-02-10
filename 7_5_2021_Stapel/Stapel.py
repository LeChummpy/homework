class Stapel:
    class __Knoten:
        def __init__(self, k):
            self.inhalt = k
            self.vorheriger = None

    def __init__(self):
        self.__laenge = 0
        self.__oberster = None

    def IstLeer(self):
        return self.__laenge==0

    def Draufpacken(self, k):
        n = self.__Knoten(k)
        if (self.__laenge==0):
            self.__oberster = n
        else:
            n.vorheriger = self.__oberster
            self.__oberster = n
        self.__laenge += 1

    def Bedienen(self):
        self.__oberster = self.__oberster.vorheriger
        self.__laenge -= 1

    def Top(self):
        return self.__oberster.inhalt

    def Laenge(self):
        return self.__laenge

    def __str__(self):
        erg = ""
        x = self.__oberster
        while x != None:
            erg += " ~ " + str(x.inhalt)
            x = x.vorheriger
        return ("[" + erg + "]")
