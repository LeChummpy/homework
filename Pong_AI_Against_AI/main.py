import pygame
import views

pygame.init()

prettyfont = pygame.font.SysFont('Arial', 70)
prettyfontsmaller = pygame.font.SysFont('Arial', 35)
SCREEN = pygame.display.set_mode((900, 600))
SCREEN_HEIGHT = SCREEN.get_height()
SCREEN_WIDTH = SCREEN.get_width()

class Game():
    def __init__(self):
        self.current_view = None

CLOCK = pygame.time.Clock()

G = Game()
G.current_view = views.AI_against_AI(SCREEN_WIDTH, SCREEN_HEIGHT)
while True:
    G.current_view.view(SCREEN)
    pygame.display.update()
    CLOCK.tick(30)
