import pygame
import mainclasses
import datastructures
import colors
import networkutils
from helper import *

pygame.init()

#-----------------------------------------------------------
#fonts
prettyfont = pygame.font.SysFont('Arial', 60)
prettyfontsmaller = pygame.font.SysFont('Arial', 35)

#-----------------------------------------------------------

screen = pygame.display.set_mode((900, 600))
screen_height = screen.get_height()
screen_width = screen.get_width()

class Game():
    def __init__(self):
        self.current_view = None

class Menu():
    def view(self):
        text_raumbeitreten_x, text_raumbeitreten_y =screen_width//2-300, screen_height//2-150
        text_raumhosten_x, text_raumhosten_y = screen_width//2-275, screen_height//2-75
        text_lokal_x, text_lokal_y = screen_width//2-200, screen_height//2
        text_beenden_x, text_beenden_y = screen_width//2-100, screen_height//2+75

        screen.fill(colors.lime)

        Kords = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if Kords[0]>text_raumbeitreten_x and Kords[0]<text_raumbeitreten_x+650 and Kords[1]>text_raumbeitreten_y and Kords[1]<text_raumbeitreten_y+75:
                    G.current_view = MehrspielerRaumbeireten(5, 5)

                elif Kords[0]>text_raumhosten_x and Kords[0]<text_raumhosten_x+600 and Kords[1]>text_raumhosten_y and Kords[1]<text_raumhosten_y+75:
                    G.current_view = MehrspielerHosten(5, 5)

                elif Kords[0]>text_lokal_x and Kords[0]<text_lokal_x+400 and Kords[1]>text_lokal_y and Kords[1]<text_lokal_y+75:
                    G.current_view = MehrspielerLokal(5, 5)

                elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
                    pygame.quit()

        text_raumbeitreten = prettyfont.render("Mehrspieler - Raum beitreten", True, colors.orange)
        text_raumhosten = prettyfont.render("Mehrspieler - Raum hosten", True, colors.orange)
        text_lokal = prettyfont.render("Mehrspieler - lokal", True, colors.orange)
        text_beenden = prettyfont.render("Beenden", True, colors.orange)

        if Kords[0]>text_raumbeitreten_x and Kords[0]<text_raumbeitreten_x+650 and Kords[1]>text_raumbeitreten_y and Kords[1]<text_raumbeitreten_y+75:
            text_raumbeitreten = prettyfont.render("Mehrspieler - Raum beitreten", True, colors.orange_light)
            text_raumhosten = prettyfont.render("Mehrspieler - Raum hosten", True, colors.orange)
            text_lokal = prettyfont.render("Mehrspieler - lokal", True, colors.orange)
            text_beenden = prettyfont.render("Beenden", True, colors.orange)

        elif Kords[0]>text_raumhosten_x and Kords[0]<text_raumhosten_x+600 and Kords[1]>text_raumhosten_y and Kords[1]<text_raumhosten_y+75:
            text_raumbeitreten = prettyfont.render("Mehrspieler - Raum beitreten", True, colors.orange)
            text_raumhosten = prettyfont.render("Mehrspieler - Raum hosten", True, colors.orange_light)
            text_lokal = prettyfont.render("Mehrspieler - lokal", True, colors.orange)
            text_beenden = prettyfont.render("Beenden", True, colors.orange)

        elif Kords[0]>text_lokal_x and Kords[0]<text_lokal_x+400 and Kords[1]>text_lokal_y and Kords[1]<text_lokal_y+75:
            text_raumbeitreten = prettyfont.render("Mehrspieler - Raum beitreten", True, colors.orange)
            text_raumhosten = prettyfont.render("Mehrspieler - Raum hosten", True, colors.orange)
            text_lokal = prettyfont.render("Mehrspieler - lokal", True, colors.orange_light)
            text_beenden = prettyfont.render("Beenden", True, colors.orange)

        elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
            text_raumbeitreten = prettyfont.render("Mehrspieler - Raum beitreten", True, colors.orange)
            text_raumhosten = prettyfont.render("Mehrspieler - Raum hosten", True, colors.orange)
            text_lokal = prettyfont.render("Mehrspieler - lokal", True, colors.orange)
            text_beenden = prettyfont.render("Beenden", True, colors.orange_light)

        screen.blit(text_raumbeitreten, (text_raumbeitreten_x, text_raumbeitreten_y))
        screen.blit(text_raumhosten, (text_raumhosten_x, text_raumhosten_y))
        screen.blit(text_lokal, (text_lokal_x, text_lokal_y))
        screen.blit(text_beenden, (text_beenden_x, text_beenden_y))

        pygame.display.update()

class Spielende:

    def __init__(self, Gewinnerbezeichnung, Gewinnerfarbe):
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
                    G.current_view = MehrspielerLokal(5, 5)

                elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
                    pygame.quit()

        text_gewinneranzeige = prettyfont.render( str(self.Gewinnerbezeichnung) + " gewinnt!", True, self.Gewinnerfarbe)
        text_spielen = prettyfont.render("Spielen", True, colors.orange)
        text_beenden = prettyfont.render("Beenden", True, colors.orange)

        if Kords[0]>text_spielen_x and Kords[0]<text_spielen_x+200 and Kords[1]>text_spielen_y and Kords[1]<text_spielen_y+75:
            text_spielen = prettyfont.render("erneut spielen", True, colors.orange_light)
            text_beenden = prettyfont.render("Beenden", True, colors.orange)

        elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
            text_spielen = prettyfont.render("erneut spielen", True, colors.orange)
            text_beenden = prettyfont.render("Beenden", True, colors.orange_light)

        screen.blit(text_gewinneranzeige, (text_gewinneranzeige_x, text_gewinneranzeige_y))
        screen.blit(text_spielen, (text_spielen_x, text_spielen_y))
        screen.blit(text_beenden, (text_beenden_x, text_beenden_y))

        pygame.display.update()

class MehrspielerLokal():
    def __init__(self, AnzahlSpalten, AnzahlZeilen):

        self.current_Spielbrett = mainclasses.Spielbrett(AnzahlSpalten, AnzahlZeilen, 20)
        self.current_Spieler1 = mainclasses.Spieler(1, colors.lime_green)
        self.current_Spieler2 = mainclasses.Spieler(2, colors.dark_red)
        self.am_Zug = self.current_Spieler1

        self.indizes_paar_angeklickter_punkte = []

    def view(self):
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
                            gewonnenepunkte = self.current_Spielbrett.VerbindungHinzufuegen(self.indizes_paar_angeklickter_punkte, kordsangeklicktezweipunkte, self.am_Zug.ID, self.am_Zug.verbindungsfarbe)

                            if gewonnenepunkte>0:
                                self.am_Zug.Punkte += gewonnenepunkte

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

class MehrspielerHosten:
    def __init__(self, AnzahlSpalten, AnzahlZeilen):

        self.current_Spielbrett = mainclasses.Spielbrett(AnzahlSpalten, AnzahlZeilen, 20)
        self.current_Spieler1 = mainclasses.Spieler(1, colors.lime_green)
        self.current_Spieler2 = mainclasses.Spieler(2, colors.dark_red)
        self.am_Zug = self.current_Spieler1

        self.serverport = 55555
        self.server = networkutils.käsekästchenserver(self.serverport, AnzahlSpalten, AnzahlZeilen)
        self.server.start()

        #self.client = networkutils.käsekästchenclient(self, ("localhost", self.serverport))

        self.indizes_paar_angeklickter_punkte = []

    def view(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                Kords = pygame.mouse.get_pos()
                indices = self.current_Spielbrett.IndicesVonAngeklicktemPunktReturnieren(Kords[0], Kords[1])
                if indices!=None:
                    self.indizes_paar_angeklickter_punkte.append(indices)

                if (len(self.indizes_paar_angeklickter_punkte)==2):
                    self.client.sendeVerbindung(self.indizes_paar_angeklickter_punkte)



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

class MehrspielerRaumbeireten():
    def __init__(self, AnzahlSpalten, AnzahlZeilen):

        self.current_Spielbrett = mainclasses.Spielbrett(AnzahlSpalten, AnzahlZeilen, 20)
        self.current_Spieler1 = mainclasses.Spieler(1, colors.lime_green)
        self.current_Spieler2 = mainclasses.Spieler(2, colors.dark_red)
        self.am_Zug = self.current_Spieler1

        self.serverport = 55555

        self.client = networkutils.käsekästchenclient(self, ("localhost", self.serverport))

        self.indizes_paar_angeklickter_punkte = []

    def view(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                Kords = pygame.mouse.get_pos()
                indices = self.current_Spielbrett.IndicesVonAngeklicktemPunktReturnieren(Kords[0], Kords[1])
                if indices!=None:
                    self.indizes_paar_angeklickter_punkte.append(indices)

                if (len(self.indizes_paar_angeklickter_punkte)==2):
                    self.client.sendeVerbindung(self.indizes_paar_angeklickter_punkte)

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
    try:
        G.current_view.view()
        CLOCK.tick(30)

    except KeyboardInterrupt:
        if isinstance(G.current_view, MehrspielerHosten):
            G.current_view.server.stop()
        pygame.quit()
