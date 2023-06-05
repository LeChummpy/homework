import pygame
import mainclasses
import datastructures
import colors
from helper import *

pygame.init()

#-----------------------------------------------------------
#fonts and sounds
prettyfont = pygame.font.SysFont('Arial', 70)
prettyfontsmaller = pygame.font.SysFont('Arial', 35)
click_sound = pygame.mixer.Sound("rsc//click_sound.wav")
win_sound = pygame.mixer.Sound("rsc//win_sound.wav")


#-----------------------------------------------------------

screen = pygame.display.set_mode((900, 600))
screen_height = screen.get_height()
screen_width = screen.get_width()

class Game():
    def __init__(self):
        self.current_view = None

class Menu():
    def view(self):
        text_spielen_x, text_spielen_y = screen_width//2-100, screen_height//2-100
        text_beenden_x, text_beenden_y = screen_width//2-110, screen_height//2-25
        text_trainKI_x, text_trainKI_y = screen_width//2-100, screen_height//2+50
        text_spielegegenKI_x, text_spielegegenKI_y = screen_width//2-100, screen_height//2+125

        screen.fill(colors.lime)

        Kords = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(click_sound)
                if Kords[0]>text_spielen_x and Kords[0]<text_spielen_x+200 and Kords[1]>text_spielen_y and Kords[1]<text_spielen_y+75:
                    G.current_view = Spielrunde(5, 5)

                elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
                    pygame.quit()

                elif Kords[0]>text_trainKI_x and Kords[0]<text_trainKI_x+250 and Kords[1]>text_trainKI_x and Kords[1]<text_trainKI_x+75:
                    pass

                elif Kords[0]>text_spielegegenKI_x and Kords[0]<text_spielegegenKI_x+250 and Kords[1]>text_spielegegenKI_y and Kords[1]<text_spielegegenKI_y+75:
                    pass

        text_spielen = prettyfont.render("Spielen", True, colors.orange)
        text_beenden = prettyfont.render("Beenden", True, colors.orange)
        text_trainKI = prettyfont.render("Train KI", True, colors.orange)
        text_spielegegenKI = prettyfont.render("Spiel KI", True, colors.orange)

        if Kords[0]>text_spielen_x and Kords[0]<text_spielen_x+200 and Kords[1]>text_spielen_y and Kords[1]<text_spielen_y+75:
            text_spielen = prettyfont.render("Spielen", True, colors.orange_light)
            text_beenden = prettyfont.render("Beenden", True, colors.orange)
            text_trainKI = prettyfont.render("Train KI", True, colors.orange)
            text_spielegegenKI = prettyfont.render("Spiel KI", True, colors.orange)

        elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
            text_spielen = prettyfont.render("Spielen", True, colors.orange)
            text_beenden = prettyfont.render("Beenden", True, colors.orange_light)
            text_trainKI = prettyfont.render("Train KI", True, colors.orange)
            text_spielegegenKI = prettyfont.render("Spiel KI", True, colors.orange)

        elif Kords[0]>text_trainKI_x and Kords[0]<text_trainKI_x+250 and Kords[1]>text_trainKI_x and Kords[1]<text_trainKI_x+75:
            text_spielen = prettyfont.render("Spielen", True, colors.orange)
            text_beenden = prettyfont.render("Beenden", True, colors.orange)
            text_trainKI = prettyfont.render("Train KI", True, colors.orange_light)
            text_spielegegenKI = prettyfont.render("Spiel KI", True, colors.orange)

        elif Kords[0]>text_spielegegenKI_x and Kords[0]<text_spielegegenKI_x+250 and Kords[1]>text_spielegegenKI_y and Kords[1]<text_spielegegenKI_y+75:
            text_spielen = prettyfont.render("Spielen", True, colors.orange)
            text_beenden = prettyfont.render("Beenden", True, colors.orange)
            text_trainKI = prettyfont.render("Train KI", True, colors.orange)
            text_spielegegenKI = prettyfont.render("Spiel KI", True, colors.orange_light)

        screen.blit(text_spielen, (text_spielen_x, text_spielen_y))
        screen.blit(text_beenden, (text_beenden_x, text_beenden_y))
        screen.blit(text_trainKI, (text_trainKI_x, text_trainKI_y))
        screen.blit(text_spielegegenKI, (text_spielegegenKI_x, text_spielegegenKI_y))

        pygame.display.update()

class Spielende:

    def __init__(self, Gewinnerbezeichnung, Gewinnerfarbe):
        pygame.mixer.Sound.play(win_sound)

        self.Gewinnerbezeichnung = Gewinnerbezeichnung
        self.Gewinnerfarbe = Gewinnerfarbe


    def view(self):
        text_gewinneranzeige_x, text_gewinneranzeige_y = screen_width//2-200, screen_height//2-225
        text_spielen_x, text_spielen_y = screen_width//2-100, screen_height//2-100
        text_beenden_x, text_beenden_y = screen_width//2-110, screen_height//2-25

        screen.fill(colors.lime)

        Kords = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Kords[0]>text_spielen_x and Kords[0]<text_spielen_x+200 and Kords[1]>text_spielen_y and Kords[1]<text_spielen_y+75:
                    G.current_view = Spielrunde(5, 5)

                elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
                    pygame.quit()

        text_gewinneranzeige = prettyfont.render( str(self.Gewinnerbezeichnung) + " gewinnt!", True, self.Gewinnerfarbe)
        text_spielen = prettyfont.render("Spielen", True, colors.orange)
        text_beenden = prettyfont.render("Beenden", True, colors.orange)

        if Kords[0]>text_spielen_x and Kords[0]<text_spielen_x+200 and Kords[1]>text_spielen_y and Kords[1]<text_spielen_y+75:
            text_spielen = prettyfont.render("Spielen", True, colors.orange_light)
            text_beenden = prettyfont.render("Beenden", True, colors.orange)

        elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
            text_spielen = prettyfont.render("Spielen", True, colors.orange)
            text_beenden = prettyfont.render("Beenden", True, colors.orange_light)

        screen.blit(text_gewinneranzeige, (text_gewinneranzeige_x, text_gewinneranzeige_y))
        screen.blit(text_spielen, (text_spielen_x, text_spielen_y))
        screen.blit(text_beenden, (text_beenden_x, text_beenden_y))

        pygame.display.update()

class Spielrunde():
    def __init__(self, AnzahlSpalten, AnzahlZeilen):
        #Vor.: -AnzahlSpalten-, -AnzahlZeilen- sind Integer
        #Eff.: Eine neue Objektinstanz der Klasse Spielrunde wird erzeugt. -AnzahlSpalten- mal -AnzahlZeilen- entspricht
        #      der Anzahl an Verbindungspunkten während der Spielrunde.
        self.current_Spielbrett = mainclasses.Spielbrett(AnzahlSpalten, AnzahlZeilen, 20)
        self.current_Spieler1 = mainclasses.Spieler(1, colors.lime_green)
        self.current_Spieler2 = mainclasses.Spieler(2, colors.dark_red)
        self.am_Zug = self.current_Spieler1

        self.indizes_paar_angeklickter_punkte = []

    def view(self):
        #Vor.: -
        #Eff.: Falls das Fenster geschlossen wird (x), wird das Spiel beendet. Falls ein Punkt angeklickt wird, so wird er der
        #      stets maximal 2-elementigen Liste indizes_paar_angeklickter_punkte hinzugefügt. Wenn 2 Elemente (Indizes zweier hintereinander angeklickter
        #      Punkte) in der Liste enthalten sind, so wird, insofern die Punkte horizontal oder vertikal benachbart sind, eine Verbindung zwischen den entsprechenden
        #      Punkten dem Spielbrett hinzugefügt-
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                Kords = pygame.mouse.get_pos()
                indices = self.current_Spielbrett.IndicesVonAngeklicktemPunktReturnieren(Kords[0], Kords[1])
                if indices!=None:
                    self.indizes_paar_angeklickter_punkte.append(indices)

                if (len(self.indizes_paar_angeklickter_punkte)==2):
                    if (horizontaldervertikalbenachbart(self.indizes_paar_angeklickter_punkte)):
                        if not(self.current_Spielbrett.angeklicktePunkteExistierenSchonAlsVerbindung(self.indizes_paar_angeklickter_punkte)):
                            kordsangeklicktezweipunkte = self.current_Spielbrett.KordsAngeklicktePunkteReturnieren(self.indizes_paar_angeklickter_punkte)
                            gewonnenepunkte = self.current_Spielbrett.VerbindungHinzufügen(self.indizes_paar_angeklickter_punkte, kordsangeklicktezweipunkte, self.am_Zug.ID, self.am_Zug.verbindungsfarbe)

                            if gewonnenepunkte>0:
                                self.am_Zug.Punkte += gewonnenepunkte
                                pygame.mixer.Sound.play(click_sound)

                            else:

                                if self.am_Zug.ID == self.current_Spieler1.ID:
                                    self.am_Zug = self.current_Spieler2
                                elif self.am_Zug.ID == self.current_Spieler2.ID:
                                    self.am_Zug = self.current_Spieler1

                    self.indizes_paar_angeklickter_punkte = []

                if self.current_Spielbrett.verbindungen.Laenge()==(self.current_Spielbrett.AnzahlKästchenHo-1)*(self.current_Spielbrett.AnzahlKästchenVer) + (self.current_Spielbrett.AnzahlKästchenVer-1)*(self.current_Spielbrett.AnzahlKästchenHo):
                    if (self.current_Spieler1.Punkte>self.current_Spieler2.Punkte):
                        G.current_view = Spielende("Spieler 1", self.current_Spieler1.verbindungsfarbe)
                    elif (self.current_Spieler2.Punkte>self.current_Spieler1.Punkte):
                        G.current_view = Spielende("Spieler 2", self.current_Spieler2.verbindungsfarbe)
                    else:
                        G.current_view = Spielende("Unentschiden", colors.white)


        screen.fill(colors.orange)

        text_amzug = None
        if (self.am_Zug.ID==1):
            text_amzug = prettyfontsmaller.render("Spieler 1 ist dran!", True, self.am_Zug.verbindungsfarbe)
        elif (self.am_Zug.ID==2):
            text_amzug = prettyfontsmaller.render("Spieler 2 ist dran!", True, self.am_Zug.verbindungsfarbe)
        screen.blit(text_amzug, (600, 200))

        text_Spieler1Punkte = prettyfont.render(str(self.current_Spieler1.Punkte), True, self.current_Spieler1.verbindungsfarbe)
        text_Spieler2Punkte = prettyfont.render(str(self.current_Spieler2.Punkte), True, self.current_Spieler2.verbindungsfarbe)
        screen.blit(text_Spieler1Punkte, (640, 75))
        screen.blit(text_Spieler2Punkte, (740, 75))

        self.current_Spielbrett.show(screen)
        pygame.display.update()

class SpielrundeKItrainieren:
    def __init__(self, AnzahlSpalten, AnzahlZeilen):

        self.current_Spielbrett = mainclasses.Spielbrett(AnzahlSpalten, AnzahlZeilen, 20)
        self.current_Spieler1 = mainclasses.SpielerKI(1, colors.lime_green, AnzahlSpalten, AnzahlZeilen)
        self.current_Spieler2 = mainclasses.SpielerKI(2, colors.dark_red, AnzahlSpalten, AnzahlZeilen)
        self.am_Zug = self.current_Spieler1

        self.indizes_paar_angeklickter_punkte = []

    def view(self):

        indices = self.amZug.getIndicesOfPointsNextDraw(Spielbrett) #berechne nächsten Zug auf Basis von aktuellem Zustand
                                                                    #--> Kords dürfen nur hor. o. ver. benachbart sein 
                                                                    #--> und nicht schon existieren
        score = self.amZug.evaluate(newSpielbrett, indices)
        self.amZug.giveFeedback(score)

        kordsangeklicktezweipunkte = self.current_Spielbrett.KordsAngeklicktePunkteReturnieren(self.indizes_paar_angeklickter_punkte)
        gewonnenepunkte = self.current_Spielbrett.VerbindungHinzufügen(self.indizes_paar_angeklickter_punkte, kordsangeklicktezweipunkte, self.am_Zug.ID, self.am_Zug.verbindungsfarbe)

        if gewonnenepunkte>0:
            self.am_Zug.Punkte += gewonnenepunkte
            pygame.mixer.Sound.play(click_sound)

        else:

            if self.am_Zug.ID == self.current_Spieler1.ID:
                self.am_Zug = self.current_Spieler2
            elif self.am_Zug.ID == self.current_Spieler2.ID:
                self.am_Zug = self.current_Spieler1

        self.indizes_paar_angeklickter_punkte = []

        if self.current_Spielbrett.verbindungen.Laenge()==(self.current_Spielbrett.AnzahlKästchenHo-1)*(self.current_Spielbrett.AnzahlKästchenVer) + (self.current_Spielbrett.AnzahlKästchenVer-1)*(self.current_Spielbrett.AnzahlKästchenHo):
            if (self.current_Spieler1.Punkte>self.current_Spieler2.Punkte):
                G.current_view = Spielende("Spieler 1", self.current_Spieler1.verbindungsfarbe)
            elif (self.current_Spieler2.Punkte>self.current_Spieler1.Punkte):
                G.current_view = Spielende("Spieler 2", self.current_Spieler2.verbindungsfarbe)
            else:
                G.current_view = Spielende("Unentschieden", colors.white)


        screen.fill(colors.orange)

        text_amzug = None
        if (self.am_Zug.ID==1):
            text_amzug = prettyfontsmaller.render("Spieler 1 ist dran!", True, self.am_Zug.verbindungsfarbe)
        elif (self.am_Zug.ID==2):
            text_amzug = prettyfontsmaller.render("Spieler 2 ist dran!", True, self.am_Zug.verbindungsfarbe)
        screen.blit(text_amzug, (600, 200))

        text_Spieler1Punkte = prettyfont.render(str(self.current_Spieler1.Punkte), True, self.current_Spieler1.verbindungsfarbe)
        text_Spieler2Punkte = prettyfont.render(str(self.current_Spieler2.Punkte), True, self.current_Spieler2.verbindungsfarbe)
        screen.blit(text_Spieler1Punkte, (640, 75))
        screen.blit(text_Spieler2Punkte, (740, 75))

        self.current_Spielbrett.show(screen)
        pygame.display.update()




class SpielrundeKI():
    def __init__(self, AnzahlSpalten, AnzahlZeilen):
        #Vor.: -AnzahlSpalten-, -AnzahlZeilen- sind Integer
        #Eff.: Eine neue Objektinstanz der Klasse Spielrunde wird erzeugt. -AnzahlSpalten- mal -AnzahlZeilen- entspricht
        #      der Anzahl an Verbindungspunkten während der Spielrunde.
        self.current_Spielbrett = mainclasses.Spielbrett(AnzahlSpalten, AnzahlZeilen, 20)
        self.current_Spieler1 = mainclasses.Spieler(1, colors.lime_green)
        self.current_Spieler2 = mainclasses.SpielerKI(2, colors.dark_red)
        self.am_Zug = self.current_Spieler1

        self.indizes_paar_angeklickter_punkte = []

    def view(self):
        #Vor.: -
        #Eff.: Falls das Fenster geschlossen wird (x), wird das Spiel beendet. Falls ein Punkt angeklickt wird, so wird er der
        #      stets maximal 2-elementigen Liste indizes_paar_angeklickter_punkte hinzugefügt. Wenn 2 Elemente (Indizes zweier hintereinander angeklickter
        #      Punkte) in der Liste enthalten sind, so wird, insofern die Punkte horizontal oder vertikal benachbart sind, eine Verbindung zwischen den entsprechenden
        #      Punkten dem Spielbrett hinzugefügt-
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and type(self.am_Zug).__name__=="Spieler": #wenn menschlicher Spieler am Zug
                Kords = pygame.mouse.get_pos()
                indices = self.current_Spielbrett.IndicesVonAngeklicktemPunktReturnieren(Kords[0], Kords[1])
                if indices!=None:
                    self.indizes_paar_angeklickter_punkte.append(indices)

            else: #KI ist dran

                self.indizes_paar_angeklickter_punkte = self.current_Spieler2.setNextMove()
                self.current_Spieler2.getFeedback()
                self.current.getState()

            if (len(self.indizes_paar_angeklickter_punkte)==2):
                if (horizontaldervertikalbenachbart(self.indizes_paar_angeklickter_punkte)):
                    if not(self.current_Spielbrett.angeklicktePunkteExistierenSchonAlsVerbindung(self.indizes_paar_angeklickter_punkte)):
                        kordsangeklicktezweipunkte = self.current_Spielbrett.KordsAngeklicktePunkteReturnieren(self.indizes_paar_angeklickter_punkte)
                        gewonnenepunkte = self.current_Spielbrett.VerbindungHinzufügen(self.indizes_paar_angeklickter_punkte, kordsangeklicktezweipunkte, self.am_Zug.ID, self.am_Zug.verbindungsfarbe)

                        if gewonnenepunkte>0:
                            self.am_Zug.Punkte += gewonnenepunkte
                            pygame.mixer.Sound.play(click_sound)

                        else:

                            if self.am_Zug.ID == self.current_Spieler1.ID:
                                self.am_Zug = self.current_Spieler2
                            elif self.am_Zug.ID == self.current_Spieler2.ID:
                                self.am_Zug = self.current_Spieler1

                self.indizes_paar_angeklickter_punkte = []

            if self.current_Spielbrett.verbindungen.Laenge()==(self.current_Spielbrett.AnzahlKästchenHo-1)*(self.current_Spielbrett.AnzahlKästchenVer) + (self.current_Spielbrett.AnzahlKästchenVer-1)*(self.current_Spielbrett.AnzahlKästchenHo):
                if (self.current_Spieler1.Punkte>self.current_Spieler2.Punkte):
                    G.current_view = Spielende("Spieler 1", self.current_Spieler1.verbindungsfarbe)
                elif (self.current_Spieler2.Punkte>self.current_Spieler1.Punkte):
                    G.current_view = Spielende("Spieler 2", self.current_Spieler2.verbindungsfarbe)
                else:
                    G.current_view = Spielende("Unentschieden", colors.white)


        screen.fill(colors.orange)

        text_amzug = None
        if (self.am_Zug.ID==1):
            text_amzug = prettyfontsmaller.render("Spieler 1 ist dran!", True, self.am_Zug.verbindungsfarbe)
        elif (self.am_Zug.ID==2):
            text_amzug = prettyfontsmaller.render("Spieler 2 ist dran!", True, self.am_Zug.verbindungsfarbe)
        screen.blit(text_amzug, (600, 200))

        text_Spieler1Punkte = prettyfont.render(str(self.current_Spieler1.Punkte), True, self.current_Spieler1.verbindungsfarbe)
        text_Spieler2Punkte = prettyfont.render(str(self.current_Spieler2.Punkte), True, self.current_Spieler2.verbindungsfarbe)
        screen.blit(text_Spieler1Punkte, (640, 75))
        screen.blit(text_Spieler2Punkte, (740, 75))

        self.current_Spielbrett.show(screen)
        pygame.display.update()


CLOCK = pygame.time.Clock()

G = Game()
G.current_view = Menu()
while True:
    G.current_view.view()
    CLOCK.tick(30)
