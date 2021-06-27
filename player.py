import pygame
from bullet import Bullet
from pygame.constants import KEYDOWN, K_1, K_2, K_3, K_BACKSPACE, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP

class Player():

    def __init__(self, surface, vertices, name, points, lives):

        self.surface = surface
        self.vertices = vertices
        self.name = name
        self.points = points
        self.lives = lives

    def draw(self):
        pygame.draw.polygon(self.surface, (255,255,255), self.vertices)
        pygame.display.update()

    def move(self):
        pass

    def shoot(self):
        pass

#--TESTING CLASS--#

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))

# Triangle vertices
v1 = [400 , 290]
v2 = [390, 320]
v3 = [410, 320]

position = [v1, v2, v3]

player = Player(screen, position, 'Luís', 0, 3 )

running = True
while running:

    player.draw()
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False 
                pygame.quit()
            if event.key == K_RIGHT:
                player.vertices[0][0] += 10 
                player.vertices[1][0] += 10 
                player.vertices[2][0] += 10 
            if event.key == K_LEFT:
                player.vertices[0][0] -= 10 
                player.vertices[1][0] -= 10 
                player.vertices[2][0] -= 10 
    screen.fill((0, 0, 0))
                
