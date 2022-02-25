import pygame
import mainclasses
import datastructures
import colors

pygame.init()

#-----------------------------------------------------------
#fonts
prettyfont = pygame.font.SysFont('Arial', 70)

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

        screen.fill(colors.lime)

        Kords = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Kords[0]>text_spielen_x and Kords[0]<text_spielen_x+200 and Kords[1]>text_spielen_y and Kords[1]<text_spielen_y+75:
                    G.current_view = ActualGame(5, 5)

                elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
                    pygame.quit()

        text_spielen = prettyfont.render("Spielen", True, colors.orange)
        text_beenden = prettyfont.render("Beenden", True, colors.orange)

        if Kords[0]>text_spielen_x and Kords[0]<text_spielen_x+200 and Kords[1]>text_spielen_y and Kords[1]<text_spielen_y+75:
            text_spielen = prettyfont.render("Spielen", True, colors.orange_light)
            text_beenden = prettyfont.render("Beenden", True, colors.orange)

        elif Kords[0]>text_beenden_x and Kords[0]<text_beenden_x+250 and Kords[1]>text_beenden_y and Kords[1]<text_beenden_y+75:
            text_spielen = prettyfont.render("Spielen", True, colors.orange)
            text_beenden = prettyfont.render("Beenden", True, colors.orange_light)

        screen.blit(text_spielen, (text_spielen_x, text_spielen_y))
        screen.blit(text_beenden, (text_beenden_x, text_beenden_y))

        pygame.display.update()

class ActualGame():
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
                def horizontaldervertikalbenachbart(indicesAngeklickteZweiPunkte):
                    indicesPunkt1 = indicesAngeklickteZweiPunkte[0]
                    indicesPunkt2 = indicesAngeklickteZweiPunkte[1]
                    if (indicesPunkt1[0]==indicesPunkt2[0] and (indicesPunkt1[1]+1==indicesPunkt2[1] or indicesPunkt1[1]-1==indicesPunkt2[1])) or ((indicesPunkt1[0]+1==indicesPunkt2[0] or indicesPunkt1[0]-1==indicesPunkt2[0]) and indicesPunkt1[1]==indicesPunkt2[1]):
                        return True
                    else:
                        return False

                Kords = pygame.mouse.get_pos()
                indices = self.current_Spielbrett.IndicesVonAngeklicktemPunktReturnieren(Kords[0], Kords[1])
                if indices!=None:
                    self.indizes_paar_angeklickter_punkte.append(indices)

                if (len(self.indizes_paar_angeklickter_punkte)==2):
                    if (horizontaldervertikalbenachbart(self.indizes_paar_angeklickter_punkte)):
                        kordsangeklicktezweipunkte = self.current_Spielbrett.KordsAngeklicktePunkteReturnieren(self.indizes_paar_angeklickter_punkte)
                        self.current_Spielbrett.VerbindungHinzufuegen(self.indizes_paar_angeklickter_punkte, kordsangeklicktezweipunkte, self.am_Zug.ID, self.am_Zug.verbindungsfarbe)


                        if self.am_Zug.ID == self.current_Spieler1.ID:
                            self.am_Zug = self.current_Spieler2
                        elif self.am_Zug.ID == self.current_Spieler2.ID:
                            self.am_Zug = self.current_Spieler1

                    self.indizes_paar_angeklickter_punkte = []

        screen.fill(colors.orange)
        self.current_Spielbrett.show(screen)
        pygame.display.update()


CLOCK = pygame.time.Clock()

G = Game()
G.current_view = Menu()
while True:
    G.current_view.view()
    CLOCK.tick(30)
