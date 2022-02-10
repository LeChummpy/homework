class Waschmaschine():

    def __init__(self):
        self.__Wasser = False
        self.__Waschmittelstand = 0
        self.__Schleudern = False
        self.__Geschlossen = True
        self.__Programm = 0

    def WasserschlauchAnschliessen(self):
        self.__Wasser = True

    def WaschmittelNachfuellen(self, menge):
        if(menge<=120 and menge>=0): #Zwischen 0 und 120?
            if (self.__Waschmittelstand+menge<=120): #Passt noch in Maschine?
                self.__Waschmittelstand+=menge

    def Schliessen(self):
        self.__Geschlossen = True

    def Oeffnen(self):
        self.__Geschlossen = False

    def ProgrammWaehlen(self, x):
        if (x<=12 and x>=1):
            if (x>=1 and x<=6):
                self.__Schleudern = False
            else:
                self.__Schleudern = True

            self.__Programm = x

    def Status(self):
        print("Wasseranschluss: " + str(self.__Wasser))
        print("Waschmittelstand: " + str(self.__Waschmittelstand))
        print("Schleudern: " + str(self.__Schleudern))
        print("Tür geschlossen: " + str(self.__Geschlossen))
        print("Programm: " + str(self.__Programm))


    def starten(self):
        if (self.__Wasser==True and self.__Waschmittelstand>=50 and self.__Geschlossen==True and self.__Programm>=1 and self.__Programm<=12):
            print("Die Wäsche wurde gewaschen.")
            if (self.__Schleudern):
                print("Die Wäsche wurde geschleudert.")

            self.__Waschmittelstand = 0
            self.__Programm = 0
            self.__Schleudern = False
        else:
            print("Sorry! Das geht nicht!")
