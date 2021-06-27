import pygame
from bullet import Bullet
from pygame.constants import KEYDOWN, K_1, K_2, K_3, K_BACKSPACE, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP


class Player:

    def __init__(self, surface, vertices, name, points, lives):
        self.surface = surface
        self.vertices = vertices
        self.name = name
        self.points = points
        self.lives = lives

    def draw(self):
        pygame.draw.polygon(self.surface, (255, 255, 255), self.vertices)
        pygame.display.update()

    def move(self, key):
        if key == K_RIGHT:
            self.vertices[0][0] += 10
            self.vertices[1][0] += 10
            self.vertices[2][0] += 10
        if key == K_LEFT:
            self.vertices[0][0] -= 10
            self.vertices[1][0] -= 10
            self.vertices[2][0] -= 10

    def shoot(self):
        pass

