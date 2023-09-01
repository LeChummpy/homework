import gameclasses
import pygame
import numpy as np

class AI_against_AI:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        players_distance_to_wall = 40
        self.player_left = gameclasses.player(players_distance_to_wall, 10, 10, 100)
        self.player_right = gameclasses.player(SCREEN_WIDTH-players_distance_to_wall-10, 10, 10, 100)
        self.ball = gameclasses.ball(10, self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)

    def view(self, screen):

        events = pygame.event.get()
        for event in events:
            keys = pygame.key.get_pressed()
            #w: 119 s: 115 down: 1073741905 up: 1073741906
            if keys[119]: #w
                if self.player_left.y_orientation>0:
                    self.player_left.y_orientation -= 5

            if keys[115]: #s
                if self.player_left.y_orientation<self.SCREEN_HEIGHT-self.player_left.height:
                    self.player_left.y_orientation += 5

            if keys[112]: #arrowup
                if self.player_right.y_orientation>0:
                    self.player_right.y_orientation -= 5

            if keys[246]: #arrowdown
                if self.player_right.y_orientation<self.SCREEN_HEIGHT-self.player_right.height:
                    self.player_right.y_orientation += 5

        ball_pos = [self.ball.x_orientation, self.ball.y_orientation]
        new_ball_pos = np.round(ball_pos+self.ball.direction*self.ball.speed, 0)
        self.ball.x_orientation = new_ball_pos[0]
        self.ball.y_orientation = new_ball_pos[1]

        if (self.ball.x_orientation>self.SCREEN_WIDTH):
            self.player_right.score+=1
            self.ball = gameclasses.ball(10, self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)
        if (self.ball.x_orientation<0):
            self.player_right.score+=1
            self.ball = gameclasses.ball(10, self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)

        if self.ball.y_orientation>self.SCREEN_HEIGHT-self.ball.radius or self.ball.y_orientation<self.ball.radius:
            self.ball.direction[1] = self.ball.direction[1]*-1

        if self.ball.x_orientation<=self.player_left.x_orientation+self.ball.radius:
            if self.ball.y_orientation>=self.player_left.y_orientation and self.ball.y_orientation<=self.player_left.y_orientation+self.player_left.width

        if self.ball.x_orientation>=self.player_left.x_orientation-self.ball.radius:
            pass

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (self.player_left.x_orientation, self.player_left.y_orientation, self.player_left.width, self.player_left.height), 1)
        pygame.draw.rect(screen, (255, 255, 255), (self.player_right.x_orientation, self.player_right.y_orientation, self.player_right.width, self.player_right.height), 1)
        pygame.draw.circle(screen,  (255, 255, 255), (self.ball.x_orientation, self.ball.y_orientation), self.ball.radius, 1)

