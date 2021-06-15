import pygame
import random

from pygame.constants import KEYDOWN, K_1, K_2, K_3, K_BACKSPACE, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP
class Asteroid:
    def __init__(self, surface, position, color, size, type, dx, dy, speed):
        self.surface = surface
        self.position= position
        self.color = color
        self.size= size
        self.type= type
        self.dx = dx
        self.dy = dy
        self.speed = speed
    def draw_asteroid(self):
        if self.type == 3:
            self.size = 20
        if self.type == 2:
            self.size = 12
        if self.type == 1:
            self.size = 8

        pygame.draw.circle(self.surface, self.color, self.position, self.size)
        pygame.display.flip()

    def move_asteroid(self):

        if self.dx == 'RIGHT':
            self.position[0] += self.speed
        if self.dx == 'LEFT':
            self.position[0] -= self.speed
        
        if self.dy == 'UP':
            self.position[1] -= self.speed
        if self.dy == 'DOWN':
            self.position[1] += self.speed
        
        

        # Asteroid crossing movements through screen
        if self.position[0] > 800: # Crossing horizontally
            self.position[0] = 0
        if self.position[0] < 0:
            self.position[0] = 800

        if self.position[1] > 600: # Crossing vertically
            self.position[1] = 0
        if self.position[1] < 0:
            self.position[1] = 600

        pygame.display.flip()
    def split_asteroid():
        pass
    
    # Adapt to collision with bullet later

    '''def collision_with_wall(self):
        
        if self.position[0] == 0:
            self.dx = 'RIGHT'
            return 'COLISION'

        if self.position[0] == 800:
            self.dx = 'LEFT'
            return 'COLISION'

        if self.position[1] == 0:
            self.dy = 'DOWN'
            return 'COLISION'

        if self.position[1] == 600:
            self.dy = 'UP'
            return 'COLISION'
            
        pygame.display.flip()'''

    # Adapt to change asteroid when hit by bullet

    '''def change_asteroid_type(self):
        
        if self.collision_with_wall():
            self.type = random.randrange(1, 4)'''
            
# --TESTING CLASS-- #

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))

init_dx = ['RIGHT', 'LEFT']
init_dy = ['UP', 'DOWN']
position = [400, 300]
asteroid = Asteroid(screen, position,
                    (255, 0 , 0), 20, 3,
                    random.choice(init_dx), random.choice(init_dy), 0.25)


running = True
while running:

    asteroid.draw_asteroid()
    asteroid.move_asteroid()
    #asteroid.collision_with_wall()
    #asteroid.change_asteroid_type()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False 
                pygame.quit()
            if event.key == K_1:
                asteroid.type = 1
            if event.key == K_2:
                asteroid.type = 2
            if event.key == K_3:
                asteroid.type = 3
        
        # Change direction just for mechanics testing
            if event.key == K_RIGHT:
                asteroid.dx = 'RIGHT'
            if event.key == K_LEFT:
                asteroid.dx = 'LEFT'
            if event.key == K_UP:
                asteroid.dy = 'UP'
            if event.key == K_DOWN:
                asteroid.dy = 'DOWN'
        # Change asteroid speed for mechanics testing
            if event.key == K_BACKSPACE:
                asteroid.speed = 0.125
            if event.key == K_SPACE:
                asteroid.speed = 0.5
            
    screen.fill((0,0,0))