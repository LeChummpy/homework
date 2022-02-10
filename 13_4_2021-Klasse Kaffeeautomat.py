class Kaffeeautomat:
    def __init__(self):
        self.__angeschaltet = False
        self.__Guthaben = 0

    def anschalten(self):
        '''
        Vor.: -
        Eff.: Der Kaffeeautomat ist, ungeachtet des vorherigen Zustandes, in den angeschalteten Zustand versetzt.
        '''
        self.__angeschaltet = True

    def ausschalten(self):
        '''
        Vor.: -
        Eff.: Der Kaffeeautomat ist, ungeachtet des vorherigen Zustandes, in den ausgeschalteten Zustand versetzt.
              Zudem verfällt das bisher eingeworfene Guthaben.
        '''
        self.__Guthaben = 0
        self.__angeschaltet = False

    def GeldEinWerfen(self, Betrag):
        '''
        Vor.: -Betrag- ist als Argument vom Typ integer geliefert
        Eff.: Falls der Automat angeschaltet ist und eine 10- oder 20-Cent-Münzen eingeworfen wurde,
              so wird das aktuelle Guthaben um das eingeworfene Geld erhöht. Wenn mit dem neuen __Guthaben
              nun 30 Cent überschritten sind, so wird Kaffe gekocht und abgefüllt. Rückgeld gibt es keins.
        '''
        if (self.__angeschaltet):
            if (Betrag==10 or Betrag==20):
                self.__Guthaben += Betrag
                if (self.__Guthaben>=30):
                    print("Kaffee gekocht und in Tasse gefüllt!")
                    self.__Guthaben = 0
