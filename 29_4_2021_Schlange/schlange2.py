# Autor: J. Ostrzinski
# Datum: 28.04.2021
# Zweck: Klasse Schlange

class Schlange:
    class __Knoten:
      def __init__(self,e):
         self.inhalt=e
         self.naechster=None

    def __init__(self):
      self.__laenge=0
      self.__erster=None
      self.__letzter=None

    def IstLeer(self):
      # Vor.: keine
      # Erg.: True ist geliefert, wenn die Schlange leer war. Andernfalls ist False geliefert.
      if self.__laenge==0:
         return True
      return False

    def Hintenran(self,k):
      # Vor.: k ist vom Typ int.
      # Eff.: k ist am Ende der Schlange angehangen.
      n = self.__Knoten(k)
      if self.__laenge==0:
         self.__erster = n
         self.__letzter = n
      else:
         knotenzeiger = self.__erster
         for i in range(self.__laenge-1):
            knotenzeiger = knotenzeiger.naechster
         knotenzeiger.naechster = n
         self.__letzter = n
      self.__laenge=self.__laenge+1

    def Vorneab(self):
      # Vor.: Die Schlange ist nicht leer.
      # Eff.: Das erste Element wurde aus der Schlange entfernt.
      self.__erster = self.__erster.naechster
      self.__laenge=self.__laenge-1

    def Kopf(self):
      # Vor.: Die Schlange ist nicht leer.
      # Erg.: Eine Kopie des Kopfes der Schlange ist geliefert. Die Schlange ist unverändert.
      erg = self.__erster.inhalt
      return erg

    def Hintenab(self):

        x = self.__erster
        for i in range(self.__laenge-2):
            x = x.naechster
        x.naechster = None
        self.__laenge-=1
        self.__letzter=x

    def Hinterteil(self):
        erg = self.__letzter.inhalt
        return erg

    def Laenge(self):
      # Vor.: keine
      # Erg.: Die Länge der Schlange/die Anzahl der Elemente ist als int-Wert geliefert.
      return self.__laenge

    def __str__(self):
      # Vor.: keine
      # Eff.: Der Inhalt der Schlange ist als String geliefert.
      erg = ""
      knotenzeiger = self.__erster
      while knotenzeiger != None:
         erg = erg + " " + str(knotenzeiger.inhalt)
         knotenzeiger = knotenzeiger.naechster
      return ">>"+erg+"<<"

s = Schlange()
s.Hintenran(1)
s.Hintenran(5)
print(s)

