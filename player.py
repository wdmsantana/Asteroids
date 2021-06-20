import pygame
from bullet import Bullet

class Player():

    def __init__(self, x, y, name, points, lives):

        self.x = x
        self.y = y
        self.name = name
        self.points = points
        self.lives = lives

    def move(self):
        pass

    def shoot(self):
        pass